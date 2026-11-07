
# Importamos Path para gestionar rutas de archivos.
from pathlib import Path

# Importamos joblib para cargar el modelo de Machine Learning.
import joblib

# Importamos FastAPI y las herramientas necesarias para nuestra API.
from fastapi import FastAPI, Query, HTTPException

# Importamos las funciones que consultan Open-Meteo.
from open_meteo import obtener_tiempo, obtener_prevision_horaria

# Importamos los modelos Pydantic.
from schemas import Prevision, ListadoPrevisiones, IrisInput, IrisPrediction



# Creamos una instancia de FastAPI llamada "app".
# Esta variable representa nuestra aplicación y contiene sus endpoints.
app = FastAPI(
    title="Proyecto Final - APIs y Servicios de Datos",  # Nombre de la API.
    version="1.0.0"  # Versión de nuestra aplicación.
)


# Definimos un endpoint llamado "/health".
# @app.get indica que responde a peticiones HTTP de tipo GET.
# Cuando alguien accede a http://127.0.0.1:8000/health,
# FastAPI ejecuta automáticamente la función health().
@app.get("/health")
def health():
    # Devolvemos un diccionario de Python con el estado de la API.
    # FastAPI lo convierte automáticamente a formato JSON.
    # El navegador recibirá: {"status": "ok"}
    return {"status": "ok"}



# Creamos un endpoint GET para consultar el tiempo de León.
@app.get("/v1/tiempo")
def consultar_tiempo():

    # Llamamos a nuestra función de open_meteo.py.
    datos = obtener_tiempo()

    # Devolvemos los datos meteorológicos en formato JSON.
    return datos



# Endpoint GET para listar las previsiones con paginación.

@app.get("/v1/previsiones", response_model=ListadoPrevisiones)
def listar_previsiones(
    pagina: int = Query(default=1, ge=1, description="Número de página"),
    limite: int = Query(default=10, ge=1, le=48, description="Registros por página"),
    temperatura_min: float | None = Query(
        default=None,
        description="Temperatura mínima en grados Celsius"
    )
):

    # Obtenemos los registros de Open-Meteo.
    registros = obtener_prevision_horaria()
    

    # Si el usuario indica una temperatura mínima,
    # filtramos los registros antes de aplicar la paginación.
    if temperatura_min is not None:
        registros = [
            registro
            for registro in registros
            if registro["temperatura"] is not None
            and registro["temperatura"] >= temperatura_min
        ]



    # Calculamos desde qué posición empezar.
    inicio = (pagina - 1) * limite

    # Calculamos dónde termina la página.
    fin = inicio + limite

    # Seleccionamos únicamente los registros de esa página.
    resultados = registros[inicio:fin]

    # Devolvemos los datos paginados y los metadatos.
    return {
        "total": len(registros),
        "pagina": pagina,
        "limite": limite,
        "resultados": resultados
    }


# Endpoint GET para consultar una previsión concreta mediante su ID.
@app.get("/v1/previsiones/{prevision_id}", response_model=Prevision)
def detalle_prevision(prevision_id: str):

    # Obtenemos las previsiones horarias de Open-Meteo.
    registros = obtener_prevision_horaria()

    # Recorremos los registros buscando el ID solicitado.
    for registro in registros:

        # Si encontramos el ID, devolvemos ese registro.
        if registro["id"] == prevision_id:
            return registro

    # Si no encontramos el ID, devolvemos un error HTTP 404.
    raise HTTPException(
        status_code=404,
        detail="No existe una previsión con ese ID"
    )



# Cargamos el modelo Iris entrenado desde su archivo.
# La ruta se calcula a partir de la ubicación de main.py.
RUTA_MODELO = Path(__file__).resolve().parent / "modelo_iris.joblib"

# Cargamos el modelo una sola vez al iniciar la aplicación.
modelo_iris = joblib.load(RUTA_MODELO)


# Endpoint POST para realizar predicciones con el modelo Iris.
@app.post("/predict", response_model=IrisPrediction)
def predecir_iris(datos: IrisInput):

    # Convertimos las medidas recibidas en una lista.
    # El orden debe coincidir con el utilizado en el entrenamiento.
    caracteristicas = [[
        datos.sepal_length,
        datos.sepal_width,
        datos.petal_length,
        datos.petal_width
    ]]

    # Realizamos la predicción.
    prediccion = modelo_iris.predict(caracteristicas)[0]

    # Convertimos el resultado numérico en el nombre de la especie.
    especies = ["setosa", "versicolor", "virginica"]

    # Devolvemos la especie predicha.
    return {"especie": especies[int(prediccion)]}

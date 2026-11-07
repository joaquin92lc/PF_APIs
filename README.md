
# Proyecto Final — APIs y Servicios de Datos

Máster en Data Engineering, MLOps y Arquitecturas Cloud.

## 1. Descripción

API REST desarrollada con FastAPI que permite consultar
datos meteorológicos de León (Castilla y León, España)
obtenidos mediante la API pública de Open-Meteo.

Además, incorpora un modelo de Machine Learning
entrenado con scikit-learn para clasificar flores del
dataset Iris.

## 2. Tecnologías

- Python
- FastAPI y Pydantic
- Requests
- scikit-learn y joblib
- Uvicorn
- Git y GitHub
- Render

## 3. Fuente de datos

Open-Meteo: https://open-meteo.com/

La API consulta previsiones meteorológicas horarias
de León, incluyendo:

- Temperatura (°C).
- Humedad relativa (%).
- Velocidad del viento (km/h).

## 4. Endpoints

| Método | Endpoint | Descripción |
|---|---|---|
| GET | /health | Estado de la API |
| GET | /v1/tiempo | Meteorología actual de León |
| GET | /v1/previsiones | Listado con filtros y paginación |
| GET | /v1/previsiones/{prevision_id} | Detalle por ID |
| POST | /predict | Clasificación de flores Iris |

El listado admite los parámetros `pagina`, `limite`
y `temperatura_min`.

La API utiliza modelos Pydantic para validar datos
y devuelve errores HTTP 404 y 422 cuando corresponde.

## 5. Ejecución en local

### Clonar el repositorio

```bash
git clone https://github.com/joaquin92lc/PF_APIs.git
cd PF_APIs
```

### Crear el entorno virtual

```bash
python -m venv .venv
```

### Activar el entorno virtual

En Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

En Linux/macOS:

```bash
source .venv/bin/activate
```

### Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

### Iniciar FastAPI

```bash
uvicorn main:app --reload
```

Documentación local:

http://127.0.0.1:8000/docs

## 6. Modelo de Machine Learning

Se utiliza el dataset Iris de scikit-learn y un
RandomForestClassifier para clasificar flores en:

- Setosa
- Versicolor
- Virginica

El modelo entrenado se encuentra en
`modelo_iris.joblib`.

Para volver a entrenarlo:

```bash
python train_model.py
```

Ejemplo de petición a POST /predict:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Respuesta esperada:

```json
{
  "especie": "setosa"
}
```

## 7. Despliegue

Aplicación desplegada en Render.

Documentación pública:

https://pf-apis.onrender.com/docs

Endpoint de salud:

https://pf-apis.onrender.com/health

El servicio utiliza el plan gratuito de Render,
por lo que puede tardar en responder tras un
periodo de inactividad.

## 8. Repositorio

https://github.com/joaquin92lc/PF_APIs

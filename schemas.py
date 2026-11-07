
# Importamos BaseModel para definir modelos de datos con Pydantic.
from pydantic import BaseModel, Field


# Modelo que representa una previsión meteorológica.
# Define los campos y tipos de datos de cada registro.
class Prevision(BaseModel):
    id: str                 # Identificador: fecha y hora.
    fecha: str              # Fecha y hora de la previsión.
    temperatura: float | None  # Temperatura en °C.
    humedad: int | None        # Humedad relativa en %.
    viento: float | None       # Velocidad del viento en km/h.


# Modelo que representa un listado paginado de previsiones.
class ListadoPrevisiones(BaseModel):
    total: int                 # Número total de registros filtrados.
    pagina: int                # Página solicitada.
    limite: int                # Máximo de registros por página.
    resultados: list[Prevision]  # Lista de previsiones meteorológicas.



# Modelo Pydantic para validar los datos de entrada de /predict.
class IrisInput(BaseModel):

    # Medidas de la flor en centímetros.
    # Field(gt=0) exige que sean números mayores que cero.
    sepal_length: float = Field(gt=0, description="Longitud del sépalo en cm")
    sepal_width: float = Field(gt=0, description="Anchura del sépalo en cm")
    petal_length: float = Field(gt=0, description="Longitud del pétalo en cm")
    petal_width: float = Field(gt=0, description="Anchura del pétalo en cm")


# Modelo Pydantic para validar la respuesta de /predict.
class IrisPrediction(BaseModel):
    especie: str

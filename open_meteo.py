
# Importamos requests para realizar peticiones HTTP a APIs externas.
import requests


# Dirección del endpoint de Open-Meteo.
URL = "https://api.open-meteo.com/v1/forecast"

# Parámetros que enviaremos a la API.
PARAMETROS = {
    "latitude": 42.5987,  # Latitud de León.
    "longitude": -5.5671,  # Longitud de León.
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "timezone": "Europe/Madrid"  # Horario local de León.
}


# Función que consulta los datos meteorológicos.
def obtener_tiempo():

    # Realizamos una petición HTTP GET.
    # timeout=10 evita esperar indefinidamente si la API no responde.
    respuesta = requests.get(URL, params=PARAMETROS, timeout=10)

    # Comprueba el código HTTP.
    # Si hay un error (404, 500, etc.), lanza una excepción.
    respuesta.raise_for_status()

    # Convertimos la respuesta JSON en un diccionario de Python.
    datos = respuesta.json()

    # Devolvemos los datos obtenidos.
    return datos


# Este bloque solo se ejecuta si iniciamos directamente este archivo.
# No se ejecutará cuando importemos la función desde main.py.
if __name__ == "__main__":

    # Consultamos Open-Meteo.
    datos = obtener_tiempo()

    # Mostramos los datos en la terminal.
    print(datos)



# Función que obtiene las previsiones meteorológicas por horas.
def obtener_prevision_horaria():

    # Parámetros para solicitar 2 días de previsiones.
    parametros_horarios = {
        "latitude": 42.5987,
        "longitude": -5.5671,
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "forecast_days": 2,
        "timezone": "Europe/Madrid"
    }

    # Consultamos Open-Meteo mediante una petición GET.
    respuesta = requests.get(
        URL,
        params=parametros_horarios,
        timeout=10
    )

    # Comprobamos si la petición HTTP ha tenido éxito.
    respuesta.raise_for_status()

    # Convertimos el JSON recibido en un diccionario Python.
    datos = respuesta.json()

    # Extraemos los arrays de las variables meteorológicas.
    hourly = datos["hourly"]

    # Creamos una lista para almacenar las observaciones.
    registros = []

    # Recorremos cada hora y agrupamos sus valores meteorológicos.
    for i, fecha in enumerate(hourly["time"]):

        registro = {
            "id": fecha,
            "fecha": fecha,
            "temperatura": hourly["temperature_2m"][i],
            "humedad": hourly["relative_humidity_2m"][i],
            "viento": hourly["wind_speed_10m"][i]
        }

        registros.append(registro)

    # Devolvemos una lista de registros meteorológicos.
    return registros

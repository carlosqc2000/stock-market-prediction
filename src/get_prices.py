import requests
import json  # ¡Esta línea faltaba!
from decouple import config

def get_prices(symbol):
    """
    Descarga los precios históricos de una empresa específica.

    Args:
        symbol (str): Símbolo de la empresa (e.g., AAPL).

    Raises:
        Exception: Si ocurre un error al obtener los datos.
    """
    try:
        # Cargar la clave API desde el archivo .env
        api_key = config("ALPHA_VANTAGE_API_KEY")

        # Construir la URL para la API
        url = f"https://www.alphavantage.co/query"
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": api_key
        }

        # Realizar la solicitud
        response = requests.get(url, params=params)
        response.raise_for_status()

        # Procesar y guardar los datos
        data = response.json()
        with open(f"data/{symbol}_prices.json", "w") as file:
            json.dump(data, file)

        print(f"Datos de precios descargados para {symbol}.")
    except Exception as e:
        raise Exception(f"Error al obtener los precios para {symbol}: {e}")

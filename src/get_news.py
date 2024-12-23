import requests
import json
from decouple import config

def get_news_sentiment(symbol):
    """
    Descarga las noticias y analiza su sentimiento para una empresa específica.

    Args:
        symbol (str): Símbolo de la empresa (e.g., AAPL).

    Raises:
        Exception: Si ocurre un error al obtener las noticias o calcular el sentimiento.
    """
    try:
        # Cargar la clave API desde el archivo .env
        api_key = config("ALPHA_VANTAGE_API_KEY")

        # Construir la URL para la API
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "NEWS_SENTIMENT",
            "tickers": symbol,
            "apikey": api_key
        }

        # Realizar la solicitud
        response = requests.get(url, params=params)
        response.raise_for_status()

        # Procesar y guardar los datos
        news_data = response.json()
        with open(f"data/{symbol}_news.json", "w") as file:
            json.dump(news_data, file)

        print(f"Noticias descargadas para {symbol}.")
    except Exception as e:
        raise Exception(f"Error al obtener noticias para {symbol}: {e}")

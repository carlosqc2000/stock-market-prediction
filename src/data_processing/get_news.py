import requests
import pandas as pd
import os

# Tu clave API de Alpha Vantage
API_KEY = "TB3O6NJ1VBQSCW3R"

# Función para obtener noticias de Alpha Vantage
def get_news_sentiment(symbol, save_path="data/raw"):
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "NEWS_SENTIMENT",
        "tickers": symbol,
        "apikey": API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        news_feed = data.get("feed", [])
        
        # Crear un DataFrame con las noticias
        news_df = pd.DataFrame(news_feed)
        
        # Convertir y limpiar datos
        if not news_df.empty:
            news_df['date'] = pd.to_datetime(news_df['time_published']).dt.date
            news_df = news_df[['date', 'title', 'summary', 'overall_sentiment_score', 'overall_sentiment_label']]
        
        # Guardar las noticias en un archivo CSV
        file_path = os.path.join(save_path, f"{symbol}_news.csv")
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        news_df.to_csv(file_path, index=False)
        print(f"Noticias guardadas en {file_path}")
    else:
        print(f"Error al obtener noticias: {response.status_code}")
        return None

# Ejecutar para un símbolo
if __name__ == "__main__":
    symbol = input("Introduce el símbolo de la empresa (e.g., AAPL): ").strip().upper()
    get_news_sentiment(symbol)

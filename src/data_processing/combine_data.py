import pandas as pd
import os

# Ruta de los datos
RAW_DATA_PATH = "data/raw/"
PROCESSED_DATA_PATH = "data/processed/"

# Función para combinar noticias y datos históricos
def combine_news_and_prices(symbol):
    try:
        # Cargar datos históricos
        price_file = os.path.join(RAW_DATA_PATH, f"{symbol}_daily.csv")
        prices = pd.read_csv(price_file)
        prices['date'] = pd.to_datetime(prices['date']).dt.date

        # Cargar datos de noticias
        news_file = os.path.join(RAW_DATA_PATH, f"{symbol}_news.csv")
        news = pd.read_csv(news_file)
        news['date'] = pd.to_datetime(news['date']).dt.date

        # Combinar los datos
        combined_data = pd.merge(prices, news, on='date', how='left')

        # Guardar los datos combinados
        combined_file = os.path.join(PROCESSED_DATA_PATH, f"{symbol}_combined.csv")
        if not os.path.exists(PROCESSED_DATA_PATH):
            os.makedirs(PROCESSED_DATA_PATH)
        combined_data.to_csv(combined_file, index=False)
        print(f"Datos combinados guardados en {combined_file}")
    except Exception as e:
        print(f"Error al combinar datos: {e}")

# Ejecutar para un símbolo
if __name__ == "__main__":
    symbol = input("Introduce el símbolo de la empresa (e.g., AAPL): ").strip().upper()
    combine_news_and_prices(symbol)

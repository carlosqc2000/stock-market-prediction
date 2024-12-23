import argparse
from src.get_prices import get_prices
from src.get_news import get_news_sentiment
from src.train_model import train_model
from src.make_prediction import make_prediction

def download_data(symbol):
    """
    Descarga los datos de precios y noticias para una empresa específica.

    Args:
        symbol (str): Símbolo de la empresa (e.g., AAPL).

    Raises:
        Exception: Si ocurre un error al descargar los datos.
    """
    try:
        get_prices(symbol)
        get_news_sentiment(symbol)
        print(f"Datos descargados exitosamente para {symbol}.")
    except Exception as e:
        print(f"Error al descargar datos para {symbol}: {e}")
        raise

def train(symbol):
    """
    Entrena un modelo de predicción para una empresa específica.

    Args:
        symbol (str): Símbolo de la empresa (e.g., AAPL).

    Raises:
        Exception: Si ocurre un error durante el entrenamiento.
    """
    try:
        train_model(symbol)
        print(f"Modelo entrenado exitosamente para {symbol}.")
    except Exception as e:
        print(f"Error al entrenar el modelo para {symbol}: {e}")
        raise

def predict(symbol):
    """
    Genera una predicción basada en el modelo entrenado para una empresa específica.

    Args:
        symbol (str): Símbolo de la empresa (e.g., AAPL).

    Returns:
        str: Predicción generada por el modelo.

    Raises:
        Exception: Si ocurre un error durante la predicción.
    """
    try:
        prediction = make_prediction(symbol)
        print(f"Predicción para {symbol}: {prediction}")
        return prediction
    except Exception as e:
        print(f"Error al generar predicción para {symbol}: {e}")
        raise

def main():
    """
    Punto de entrada principal del programa. Administra la lógica principal y los comandos desde la línea de comandos.
    """
    # Configurar argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Herramienta para predicción del mercado bursátil.")
    parser.add_argument("action", choices=["download", "train", "predict"], help="Acción a realizar")
    parser.add_argument("symbol", help="Símbolo de la empresa (e.g., AAPL)")
    args = parser.parse_args()

    try:
        if args.action == "download":
            download_data(args.symbol)
        elif args.action == "train":
            train(args.symbol)
        elif args.action == "predict":
            result = predict(args.symbol)
            print(f"Predicción para {args.symbol}: {result}")
        else:
            print("Acción no válida. Usa 'download', 'train' o 'predict'.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()

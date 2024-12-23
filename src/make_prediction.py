import pickle
import pandas as pd

def make_prediction(symbol):
    """
    Genera una predicción para una empresa específica usando su modelo entrenado.

    Args:
        symbol (str): Símbolo de la empresa (e.g., AAPL).

    Returns:
        str: Predicción generada por el modelo.

    Raises:
        Exception: Si ocurre un error durante la predicción.
    """
    try:
        # Cargar el modelo guardado
        with open(f"models/{symbol}_model.pkl", "rb") as file:
            model = pickle.load(file)

        # Cargar nuevos datos de entrada
        recent_data = pd.read_csv(f"data/{symbol}_recent.csv")

        # Generar predicción
        prediction = model.predict(recent_data)
        print(f"Predicción generada para {symbol}: {prediction}")

        return prediction
    except Exception as e:
        raise Exception(f"Error al generar predicción para {symbol}: {e}")

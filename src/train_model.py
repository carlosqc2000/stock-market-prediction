from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle

def train_model(symbol):
    """
    Entrena un modelo de predicción basado en datos históricos de precios y noticias.

    Args:
        symbol (str): Símbolo de la empresa (e.g., AAPL).

    Raises:
        Exception: Si ocurre un error durante el entrenamiento.
    """
    try:
        # Cargar datos previamente procesados
        data = pd.read_csv(f"data/{symbol}_processed.csv")
        
        # Separar características y etiqueta
        X = data.drop(columns=["target"])
        y = data["target"]

        # Dividir en conjunto de entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Entrenar modelo
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        # Evaluar modelo
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Precisión del modelo para {symbol}: {accuracy:.2f}")

        # Guardar modelo
        with open(f"models/{symbol}_model.pkl", "wb") as file:
            pickle.dump(model, file)

        print(f"Modelo guardado para {symbol}.")
    except Exception as e:
        raise Exception(f"Error al entrenar el modelo para {symbol}: {e}")

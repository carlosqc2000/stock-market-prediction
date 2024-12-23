from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import os

# Tu clave API de Alpha Vantage
API_KEY = "TB3O6NJ1VBQSCW3R"

# Función para recolectar datos históricos
def fetch_historical_data(symbol, outputsize="full", save_path="data/raw"):
    ts = TimeSeries(key=API_KEY, output_format="pandas")
    try:
        # Obtener datos diarios del símbolo
        data, metadata = ts.get_daily(symbol=symbol, outputsize=outputsize)
        
        # Renombrar columnas explícitamente
        data.columns = ['open', 'high', 'low', 'close', 'volume']
        data.reset_index(inplace=True)  # Mover la fecha al DataFrame
        data.rename(columns={"index": "date"}, inplace=True)

        # Crear el directorio si no existe
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # Guardar los datos en un archivo CSV
        file_path = os.path.join(save_path, f"{symbol}_daily.csv")
        data.to_csv(file_path, index=False)
        print(f"Datos guardados para {symbol} en {file_path}")
    except Exception as e:
        print(f"Error al obtener datos para {symbol}: {e}")

if __name__ == "__main__":
    # Solicitar el símbolo de la empresa al usuario
    symbol = input("Introduce el símbolo de la empresa (e.g., AAPL, MSFT, GOOGL): ").strip().upper()
    fetch_historical_data(symbol)

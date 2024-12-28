import requests
import json
from decouple import config

def get_prices(symbol: str, interval: str = "30min") -> list:
    """
    Fetch intraday price data for a specific company.

    Args:
        symbol (str): The stock symbol (e.g., AAPL).
        interval (str): The time interval for the data (e.g., 1min, 5min, 30min).

    Returns:
        list: A list of intraday price data dictionaries.

    Raises:
        Exception: If an error occurs while fetching the data.
    """
    try:
        # Load API key from .env
        api_key = config("ALPHA_VANTAGE_API_KEY")

        # Build the API URL
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": interval,
            "apikey": api_key,
            "outputsize": "full"  # Fetch full data (last 30 days)
        }

        # Make the request
        response = requests.get(url, params=params)
        response.raise_for_status()

        # Parse the response
        data = response.json()
        if f"Time Series ({interval})" not in data:
            raise ValueError(f"Unexpected API response format: {data}")

        # Extract and format the data
        prices = []
        for datetime, values in data[f"Time Series ({interval})"].items():
            prices.append({
                "datetime": datetime,
                "open": float(values["1. open"]),
                "high": float(values["2. high"]),
                "low": float(values["3. low"]),
                "close": float(values["4. close"]),
                "volume": int(values["5. volume"]),
                "symbol": symbol
            })

        # Save to local JSON file for reference
        with open(f"data/raw/{symbol}_intraday_prices_{interval}.json", "w") as file:
            json.dump(prices, file, indent=4)

        print(f"Intraday price data downloaded for {symbol} ({interval}).")
        return prices
    except Exception as e:
        raise Exception(f"Error fetching intraday prices for {symbol}: {e}")

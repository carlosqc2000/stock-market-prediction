import requests
import json
from decouple import config
from datetime import datetime

def get_news(symbol: str) -> list:
    """
    Fetch news articles and sentiment analysis for a specific company.

    Args:
        symbol (str): The stock symbol (e.g., AAPL).

    Returns:
        list: A list of news articles with sentiment analysis.

    Raises:
        Exception: If an error occurs while fetching the news data.
    """
    try:
        # Load API key from .env
        api_key = config("ALPHA_VANTAGE_API_KEY")

        # Build the API URL
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "NEWS_SENTIMENT",
            "tickers": symbol,
            "apikey": api_key
        }

        # Make the request
        response = requests.get(url, params=params)
        response.raise_for_status()

        # Parse the response
        data = response.json()
        if "feed" not in data:
            raise ValueError(f"Unexpected API response format: {data}")

        # Extract and format the news data
        news_list = []
        for article in data["feed"]:
            # Parse the time_published into a datetime object
            time_published = datetime.strptime(article.get("time_published", ""), "%Y%m%dT%H%M%S")

            news_list.append({
                "title": article.get("title", ""),
                "summary": article.get("summary", ""),
                "url": article.get("url", ""),
                "time_published": time_published,  # Store as datetime
                "overall_sentiment_score": float(article.get("overall_sentiment_score", 0)),
                "overall_sentiment_label": article.get("overall_sentiment_label", ""),
                "ticker": symbol
            })

        # Save to local JSON file for reference
        with open(f"data/raw/{symbol}_news.json", "w") as file:
            json.dump(news_list, file, indent=4, default=str)  # Convert datetime to string for JSON

        print(f"News and sentiment data downloaded for {symbol}.")
        return news_list
    except Exception as e:
        raise Exception(f"Error fetching news for {symbol}: {e}")
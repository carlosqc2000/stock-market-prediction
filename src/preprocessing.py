import pandas as pd
from datetime import datetime
from database.mongo_db.repository import MongoRepository

# Initialize repository instance
repo = MongoRepository()

def fetch_prices(symbol: str) -> pd.DataFrame:
    """
    Fetch price data from MongoDB for the given symbol.

    Args:
        symbol (str): The stock symbol (e.g., AAPL).

    Returns:
        pd.DataFrame: DataFrame containing price data.
    """
    prices = list(repo.db.Prices.find({"symbol": symbol}))
    return pd.DataFrame(prices)

def fetch_news(symbol: str) -> pd.DataFrame:
    """
    Fetch news data from MongoDB for the given symbol.

    Args:
        symbol (str): The stock symbol (e.g., AAPL).

    Returns:
        pd.DataFrame: DataFrame containing news data.
    """
    news = list(repo.db.News.find({"ticker": symbol}))
    return pd.DataFrame(news)

def align_news_with_prices(prices_df, news_df):
    # Convert time_published to datetime and extract date
    news_df["time_published"] = pd.to_datetime(news_df["time_published"])
    news_df["news_date"] = news_df["time_published"].dt.date

    # Aggregate news sentiment by date
    sentiment_agg = news_df.groupby("news_date").agg({
        "overall_sentiment_score": "mean",
        "overall_sentiment_label": lambda x: x.value_counts().idxmax(),
        "title": "count"
    }).reset_index()
    sentiment_agg.rename(columns={
        "overall_sentiment_score": "avg_sentiment_score",
        "overall_sentiment_label": "dominant_sentiment",
        "title": "news_count"
    }, inplace=True)

    # Convert price dates to datetime
    prices_df["datetime"] = pd.to_datetime(prices_df["datetime"]).dt.date

    # Merge price data with sentiment data
    merged_df = pd.merge(prices_df, sentiment_agg, left_on="datetime", right_on="news_date", how="left")
    merged_df.drop(columns=["news_date"], inplace=True)

    # Fill missing sentiment data with default values
    merged_df["avg_sentiment_score"].fillna(0, inplace=True)
    merged_df["dominant_sentiment"].fillna("Neutral", inplace=True)
    merged_df["news_count"].fillna(0, inplace=True)

    return merged_df


def save_preprocessed_data(df: pd.DataFrame, symbol: str) -> None:
    """
    Save the preprocessed data to a CSV file.

    Args:
        df (pd.DataFrame): Preprocessed DataFrame.
        symbol (str): Stock symbol.

    Returns:
        None
    """
    df.to_csv(f"data/processed/{symbol}_preprocessed.csv", index=False)
    print(f"Preprocessed data saved to data/processed/{symbol}_preprocessed.csv")

def preprocess_data(symbol: str) -> None:
    """
    Full pipeline to preprocess data for a specific symbol.

    Args:
        symbol (str): Stock symbol (e.g., AAPL).
    """
    # Step 1: Fetch data
    prices_df = fetch_prices(symbol)
    news_df = fetch_news(symbol)

    # Step 2: Align news with prices
    merged_df = align_news_with_prices(prices_df, news_df)

    # Step 3: Save preprocessed data
    save_preprocessed_data(merged_df, symbol)

from pymongo import MongoClient
from decouple import config
from bson.objectid import ObjectId
from typing import Optional, Dict

class MongoRepository:
    def __init__(self):
        """
        Initializes the connection to the MongoDB database.
        """
        try:
            self.mongo_uri = config("MONGO_URI")
            self.client = MongoClient(self.mongo_uri)
            self.db = self.client["Data_Fondos"]
            print("Connection to MongoDB established.")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")

    def list_collections(self):
        """
        Lists all collections available in the database.
        """
        try:
            collections = self.db.list_collection_names()
            return collections
        except Exception as e:
            print(f"Error listing collections: {e}")
            return []

    # ------------------------- CRUD FOR PRICES -------------------------

    def create_price(self, price_data: Dict) -> None:
        """
        Inserts a price document into the 'Prices' collection.

        Args:
            price_data (Dict): Dictionary containing price data.
        """
        try:
            self.db.Prices.insert_one(price_data)
            print(f"Price inserted: {price_data['date']}")
        except Exception as e:
            print(f"Error inserting price: {e}")

    def read_price_by_id(self, price_id: ObjectId) -> Optional[Dict]:
        """
        Retrieves a price document by its ID from the 'Prices' collection.

        Args:
            price_id (ObjectId): ID of the document to retrieve.

        Returns:
            Optional[Dict]: The price document or None if not found.
        """
        try:
            price = self.db.Prices.find_one({"_id": price_id})
            return price
        except Exception as e:
            print(f"Error retrieving price by ID: {e}")
            return None

    def update_price_by_id(self, price_id: ObjectId, new_data: Dict) -> None:
        """
        Updates a price document in the 'Prices' collection by its ID.

        Args:
            price_id (ObjectId): ID of the document to update.
            new_data (Dict): New data to update.
        """
        try:
            result = self.db.Prices.update_one({"_id": price_id}, {"$set": new_data})
            if result.modified_count > 0:
                print(f"Price updated: {price_id}")
            else:
                print(f"No price found with ID: {price_id}")
        except Exception as e:
            print(f"Error updating price by ID: {e}")

    def delete_price_by_id(self, price_id: ObjectId) -> None:
        """
        Deletes a price document from the 'Prices' collection by its ID.

        Args:
            price_id (ObjectId): ID of the document to delete.
        """
        try:
            result = self.db.Prices.delete_one({"_id": price_id})
            if result.deleted_count > 0:
                print(f"Price deleted: {price_id}")
            else:
                print(f"No price found with ID: {price_id}")
        except Exception as e:
            print(f"Error deleting price by ID: {e}")

    # ------------------------- CRUD FOR NEWS -------------------------

    def create_news(self, news_data: Dict) -> None:
        """
        Inserts a news document into the 'News' collection.

        Args:
            news_data (Dict): Dictionary containing news data.
        """
        try:
            self.db.News.insert_one(news_data)
            print(f"News inserted: {news_data['title']}")
        except Exception as e:
            print(f"Error inserting news: {e}")

    def read_news_by_id(self, news_id: ObjectId) -> Optional[Dict]:
        """
        Retrieves a news document by its ID from the 'News' collection.

        Args:
            news_id (ObjectId): ID of the document to retrieve.

        Returns:
            Optional[Dict]: The news document or None if not found.
        """
        try:
            news = self.db.News.find_one({"_id": news_id})
            return news
        except Exception as e:
            print(f"Error retrieving news by ID: {e}")
            return None

    def update_news_by_id(self, news_id: ObjectId, new_data: Dict) -> None:
        """
        Updates a news document in the 'News' collection by its ID.

        Args:
            news_id (ObjectId): ID of the document to update.
            new_data (Dict): New data to update.
        """
        try:
            result = self.db.News.update_one({"_id": news_id}, {"$set": new_data})
            if result.modified_count > 0:
                print(f"News updated: {news_id}")
            else:
                print(f"No news found with ID: {news_id}")
        except Exception as e:
            print(f"Error updating news by ID: {e}")

    def delete_news_by_id(self, news_id: ObjectId) -> None:
        """
        Deletes a news document from the 'News' collection by its ID.

        Args:
            news_id (ObjectId): ID of the document to delete.
        """
        try:
            result = self.db.News.delete_one({"_id": news_id})
            if result.deleted_count > 0:
                print(f"News deleted: {news_id}")
            else:
                print(f"No news found with ID: {news_id}")
        except Exception as e:
            print(f"Error deleting news by ID: {e}")

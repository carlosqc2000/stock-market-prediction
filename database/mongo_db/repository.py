from pymongo import MongoClient
from decouple import config

class MongoRepository:
    def __init__(self):
        """
        Inicializa la conexión a la base de datos MongoDB.
        """
        try:
            self.mongo_uri = config("MONGO_URI")
            self.client = MongoClient(self.mongo_uri)
            self.db = self.client["Data_Fondos"]
            print("Conexión a MongoDB establecida.")
        except Exception as e:
            print(f"Error al conectar con MongoDB: {e}")


    def list_collections(self):
        """
        Lista todas las colecciones disponibles en la base de datos.
        """
        try:
            collections = self.db.list_collection_names()
            return collections
        except Exception as e:
            print(f"Error al listar colecciones: {e}")
            return []

    # ------------------------- CRUD PARA PRECIOS -------------------------

    def create_price(self, price_data):
        """
        Inserta un documento de precio en la colección 'Prices'.

        Args:
            price_data (dict): Diccionario con los datos del precio.
        """
        try:
            self.db.Prices.insert_one(price_data)
            print(f"Precio insertado: {price_data['date']}")
        except Exception as e:
            print(f"Error al insertar precio: {e}")

    def read_price_by_id(self, price_id):
        """
        Recupera un documento de precio por su ID en la colección 'Prices'.

        Args:
            price_id (ObjectId): ID del documento a recuperar.

        Returns:
            dict: Documento del precio o None si no se encuentra.
        """
        try:
            price = self.db.Prices.find_one({"_id": price_id})
            return price
        except Exception as e:
            print(f"Error al recuperar precio por ID: {e}")
            return None

    def update_price_by_id(self, price_id, new_data):
        """
        Actualiza un documento de precio en la colección 'Prices' por su ID.

        Args:
            price_id (ObjectId): ID del documento a actualizar.
            new_data (dict): Datos nuevos para actualizar.
        """
        try:
            result = self.db.Prices.update_one({"_id": price_id}, {"$set": new_data})
            if result.modified_count > 0:
                print(f"Precio actualizado: {price_id}")
            else:
                print(f"No se encontró un precio con ID: {price_id}")
        except Exception as e:
            print(f"Error al actualizar precio por ID: {e}")

    def delete_price_by_id(self, price_id):
        """
        Elimina un documento de precio de la colección 'Prices' por su ID.

        Args:
            price_id (ObjectId): ID del documento a eliminar.
        """
        try:
            result = self.db.Prices.delete_one({"_id": price_id})
            if result.deleted_count > 0:
                print(f"Precio eliminado: {price_id}")
            else:
                print(f"No se encontró un precio con ID: {price_id}")
        except Exception as e:
            print(f"Error al eliminar precio por ID: {e}")

    # ------------------------- CRUD PARA NOTICIAS -------------------------

    def create_news(self, news_data):
        """
        Inserta un documento de noticia en la colección 'News'.

        Args:
            news_data (dict): Diccionario con los datos de la noticia.
        """
        try:
            self.db.News.insert_one(news_data)
            print(f"Noticia insertada: {news_data['title']}")
        except Exception as e:
            print(f"Error al insertar noticia: {e}")

    def read_news(self, symbol):
        """
        Recupera todas las noticias para un símbolo específico de la colección 'News'.

        Args:
            symbol (str): Símbolo de la empresa (e.g., 'AAPL').

        Returns:
            list: Lista de documentos de noticias.
        """
        try:
            news = list(self.db.News.find({"symbol": symbol}))
            return news
        except Exception as e:
            print(f"Error al recuperar noticias: {e}")
            return []

    def update_news(self, news_id, new_data):
        """
        Actualiza un documento de noticia en la colección 'News'.

        Args:
            news_id (ObjectId): ID del documento a actualizar.
            new_data (dict): Datos nuevos para actualizar.
        """
        try:
            result = self.db.News.update_one({"_id": news_id}, {"$set": new_data})
            if result.modified_count > 0:
                print(f"Noticia actualizada: {news_id}")
            else:
                print(f"No se encontró una noticia con ID: {news_id}")
        except Exception as e:
            print(f"Error al actualizar noticia: {e}")

    def delete_news(self, news_id):
        """
        Elimina un documento de noticia de la colección 'News'.

        Args:
            news_id (ObjectId): ID del documento a eliminar.
        """
        try:
            result = self.db.News.delete_one({"_id": news_id})
            if result.deleted_count > 0:
                print(f"Noticia eliminada: {news_id}")
            else:
                print(f"No se encontró una noticia con ID: {news_id}")
        except Exception as e:
            print(f"Error al eliminar noticia: {e}")

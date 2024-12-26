class Price:
    """
    Clase que representa un registro de precio de una acción.
    """
    def __init__(self, symbol, date, open_price, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open_price = open_price
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def to_dict(self):
        return {
            "symbol": self.symbol,
            "date": self.date,
            "open": self.open_price,
            "high": self.high,
            "low": self.low,
            "close": self.close,
            "volume": self.volume
        }

class News:
    """
    Clase que representa un registro de una noticia financiera.
    """
    def __init__(self, symbol, title, summary, time_published, sentiment):
        self.symbol = symbol
        self.title = title
        self.summary = summary
        self.time_published = time_published
        self.sentiment = sentiment

    def to_dict(self):
        return {
            "symbol": self.symbol,
            "title": self.title,
            "summary": self.summary,
            "time_published": self.time_published,
            "sentiment": self.sentiment
        }

from databases import Database
from datetime import datetime

DATABASE_URL = "sqlite:///./prices.db"

database = Database(DATABASE_URL)


async def create_price_table():
    query = """
    CREATE TABLE IF NOT EXISTS prices (
        id INTEGER PRIMARY KEY,
        ticker TEXT,
        price REAL,
        timestamp INTEGER
    )
    """
    await database.execute(query)


async def save_price(ticker: str, price: float, timestamp: int):
    query = "INSERT INTO prices (ticker, price, timestamp) VALUES (:ticker, :price, :timestamp)"
    await database.execute(query, {"ticker": ticker, "price": price, "timestamp": timestamp})


async def get_all_prices(ticker: str):
    query = """
    SELECT * FROM prices
    WHERE ticker = :ticker
    """
    return await database.fetch_all(query, {"ticker": ticker})


async def get_prices_in_range(ticker: str, start: int, end: int):
    query = """
    SELECT * FROM prices
    WHERE timestamp BETWEEN :start AND :end
    AND ticker = :ticker
    """
    return await database.fetch_all(query, {"ticker": ticker,"start": start, "end": end})


async def get_last_price(ticker: str):
    query = """
    SELECT * FROM prices
    WHERE ticker = :ticker
    ORDER BY timestamp DESC LIMIT 1
    """
    return await database.fetch_one(query, {"ticker": ticker})

from databases import Database
from datetime import datetime

DATABASE_URL = "sqlite:///./prices.db"

database = Database(DATABASE_URL)

# Создание таблицы цен
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

# Сохранение цены
async def save_price(ticker: str, price: float, timestamp: int):
    query = "INSERT INTO prices (ticker, price, timestamp) VALUES (:ticker, :price, :timestamp)"
    await database.execute(query, {"ticker": ticker, "price": price, "timestamp": timestamp})

# Получение всех цен
async def get_all_prices():
    query = "SELECT * FROM prices"
    return await database.fetch_all(query)

# Получение цен за промежуток времени
async def get_prices_in_range(start: int, end: int):
    query = """
    SELECT * FROM prices
    WHERE timestamp BETWEEN :start AND :end
    """
    return await database.fetch_all(query, {"start": start, "end": end})

# Получение последней цены для конкретного тикера
async def get_last_price(ticker: str):
    query = """
    SELECT * FROM prices
    WHERE ticker = :ticker
    ORDER BY timestamp DESC LIMIT 1
    """
    return await database.fetch_one(query, {"ticker": ticker})

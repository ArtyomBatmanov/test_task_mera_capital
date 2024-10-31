import sqlite3
from typing import List, Dict, Optional

conn = sqlite3.connect('prices.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS prices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticker TEXT NOT NULL,
        price REAL NOT NULL,
        timestamp INTEGER NOT NULL
    )
""")
conn.commit()


def save_price(ticker: str, price: float, timestamp: int):
    cursor.execute("INSERT INTO prices (ticker, price, timestamp) VALUES (?, ?, ?)", (ticker, price, timestamp))
    conn.commit()


def get_all_prices(ticker: str) -> List[Dict]:
    cursor.execute("SELECT ticker, price, timestamp FROM prices WHERE ticker = ?", (ticker,))
    rows = cursor.fetchall()
    return [{"ticker": row[0], "price": row[1], "timestamp": row[2]} for row in rows]


def get_last_price(ticker: str) -> Optional[Dict]:
    cursor.execute("SELECT ticker, price, timestamp FROM prices WHERE ticker = ? ORDER BY timestamp DESC LIMIT 1",
                   (ticker,))
    row = cursor.fetchone()
    if row:
        return {"ticker": row[0], "price": row[1], "timestamp": row[2]}
    return None


def get_prices_by_date(ticker: str, date_from: int, date_to: int) -> List[Dict]:
    cursor.execute("""
        SELECT ticker, price, timestamp 
        FROM prices 
        WHERE ticker = ? AND timestamp BETWEEN ? AND ? 
        ORDER BY timestamp
    """, (ticker, date_from, date_to))
    rows = cursor.fetchall()
    return [{"ticker": row[0], "price": row[1], "timestamp": row[2]} for row in rows]


from fastapi import FastAPI, HTTPException, Query
from typing import List
from client import fetch_all_prices
from database import database, create_price_table, get_all_prices, get_prices_in_range, get_last_price
import asyncio

app = FastAPI()

# Подключение к БД при запуске
@app.on_event("startup")
async def startup():
    await database.connect()
    await create_price_table()  # Создаем таблицу, если еще нет
    asyncio.create_task(fetch_all_prices())  # Запускаем сбор данных в фоне

# Отключение от БД при завершении
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Endpoint для получения всей истории цен
@app.get("/prices", response_model=List[dict])
async def get_price_history():
    prices = await get_all_prices()
    return [dict(price) for price in prices]

# Endpoint для получения цен за определенный промежуток времени
@app.get("/prices/range")
async def get_prices_by_range(start: int = Query(...), end: int = Query(...)):
    prices = await get_prices_in_range(start, end)
    return [dict(price) for price in prices]

# Endpoint для получения последней цены
@app.get("/prices/latest")
async def get_latest_price(ticker: str):
    price = await get_last_price(ticker)
    if price:
        return dict(price)
    else:
        raise HTTPException(status_code=404, detail="Price not found")

from fastapi import FastAPI, HTTPException, Query
from typing import List
from client import fetch_all_prices
from database import database, create_price_table, get_all_prices, get_prices_in_range, get_last_price
import asyncio

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    await create_price_table()
    asyncio.create_task(fetch_all_prices())


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/prices", response_model=List[dict])
async def get_price_history(ticker: str):
    prices = await get_all_prices(ticker)
    return [dict(price) for price in prices]

@app.get("/prices/range")
async def get_prices_by_range(ticker: str, start: int = Query(...), end: int = Query(...)):
    prices = await get_prices_in_range(ticker, start, end)
    return [dict(price) for price in prices]

@app.get("/prices/latest")
async def get_latest_price(ticker: str):
    price = await get_last_price(ticker)
    if price:
        return dict(price)
    else:
        raise HTTPException(status_code=404, detail="Price not found")

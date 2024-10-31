from fastapi import FastAPI, Query, HTTPException
from database import get_all_prices, get_last_price, get_prices_by_date

app = FastAPI()


@app.get("/prices/")
async def api_get_all_prices(ticker: str = Query(None, description="Ticker of the currency (e.g., btc_usd, eth_usd)")):
    if not ticker:
        raise HTTPException(status_code=422, detail="Ticker parameter is required")
    prices = get_all_prices(ticker)
    if not prices:
        raise HTTPException(status_code=404, detail="No data found for the given ticker")
    return prices


@app.get("/prices/last")
async def api_get_last_price(ticker: str = Query(None, description="Ticker of the currency (e.g., btc_usd, eth_usd)")):
    if not ticker:
        raise HTTPException(status_code=422, detail="Ticker parameter is required")
    price = get_last_price(ticker)
    if not price:
        raise HTTPException(status_code=404, detail="No data found for the given ticker")
    return price


@app.get("/prices/by_date")
async def api_get_price_by_date(
        ticker: str = Query(None, description="Ticker of the currency (e.g., btc_usd, eth_usd)"),
        date_from: int = Query(..., description="Starting UNIX timestamp for the price filter"),
        date_to: int = Query(..., description="Ending UNIX timestamp for the price filter")
):
    if not ticker:
        raise HTTPException(status_code=422, detail="Ticker parameter is required")
    prices = get_prices_by_date(ticker, date_from, date_to)
    if not prices:
        raise HTTPException(status_code=404, detail="No data found for the given ticker and date range")
    return prices

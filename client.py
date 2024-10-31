import aiohttp
import asyncio
from database import save_price

async def fetch_price(ticker: str):
    url = "https://www.deribit.com/api/v2/public/get_index_price"
    params = {"index_name": ticker}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                price = data['result']['index_price']
                timestamp = data['usIn']
                print(f"Current {ticker.upper()} price: {price}, Timestamp: {timestamp}")
                save_price(ticker, price, timestamp)
            else:
                print(f"Failed to fetch price for {ticker}. Status code: {response.status}")

async def fetch_all_prices():
    while True:
        await asyncio.gather(
            fetch_price("btc_usd"),
            fetch_price("eth_usd")
        )
        await asyncio.sleep(60)


asyncio.run(fetch_all_prices())

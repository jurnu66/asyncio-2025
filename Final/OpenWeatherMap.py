import os
import asyncio
import httpx

API_KEY = os.getenv("8ccbace690f41485739b2a56cf572ed8")
CITY = "Bangkok"

async def fetch_all_weather():
    async with httpx.AsyncClient() as client:
        r = await client.get(
            "http://api.openweathermap.org/data/2.5/weather",
            params={"q": CITY, "appid": API_KEY, "units": "metric"},
            timeout=10.0,
        )
        r.raise_for_status()
        return r.json()

if __name__ == "__main__":
    data = asyncio.run(fetch_all_weather())
    print("Temperature:", data["main"]["temp"], "°C")
    print("Description:", data["weather"][0]["description"])

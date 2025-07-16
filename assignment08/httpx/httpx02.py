
import asyncio
import httpx

async def fetch(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.status_code, url

async def main():
    urls = [
        "https://www.example.com",
        "https://httpbin.org",
        "https://api.github.com"
    ]
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for status, url in results:
        print(f"{url} - {status}")

if __name__ == "__main__":
    asyncio.run(main())
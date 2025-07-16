import asyncio
import httpx

async def fetch_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        print(f"Name: {data['name']}")
        print(f"ID: {data['id']}")
        print(f"Height: {data['height']}")
        print(f"Weight: {data['weight']}")
        types = [t['type']['name'] for t in data['types']]
        print(f"Types: {', '.join(types)}")

async def main():
    pokemon_names = ['pikachu']
    tasks = [fetch_pokemon(name) for name in pokemon_names]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
    
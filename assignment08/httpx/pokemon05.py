import asyncio
import httpx

#รายการชื่อโปเกมอน
pokemon_names = [
    "pikachu", "bulbasaur", "charmander", "squirtle", "eevee",
    "snorlax", "gengar", "mewtwo", "psyduck", "jigglypuff"
]

#ฟังก์ชันดึงข้อมูลโปเกมอน 
async def fetch_pokemon_data(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return {
            "name": data["name"],
            "id": data["id"],
            "base_experience": data["base_experience"]
        }

#ฟังก์ชันหลักสำหรับดึงข้อมูลโปเกมอนทั้งหมด
async def main():
    tasks = [fetch_pokemon_data(name) for name in pokemon_names]
    results = await asyncio.gather(*tasks)

    # จัดเรียงผลลัพธ์ตาม base_experience
    sorted_results = sorted(results, key=lambda x: x["base_experience"], reverse=True)  #lambda ฟังก์ชันสำหรับเรียงลำดับ

    # แสดงผลลัพธ์
    print(f"{'Name':<12} {'ID':<5} {'Base Experience'}")
    print("-" * 30)
    for p in sorted_results:
        print(f"{p['name']:<12} {p['id']:<5} {p['base_experience']}")

if __name__ == "__main__":
    asyncio.run(main())

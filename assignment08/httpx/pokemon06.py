import asyncio
import httpx

# ใช้ URL หลักเพื่อดึง 20 abilities แรก
API_URL = "https://pokeapi.co/api/v2/ability/?limit=20"

#รับ URL ของ ability และ client ที่ใช้ส่งคำขอ ดึงข้อมูล JSON ของ ability นั้น

async def fetch_ability_details(url, client):
    response = await client.get(url)
    data = response.json()
    ability_name = data["name"]
    pokemon_count = len(data["pokemon"])
    return ability_name, pokemon_count

async def main():
    async with httpx.AsyncClient() as client:
        # ดึงรายการ abilities
        response = await client.get(API_URL)
        abilities_data = response.json()["results"]
        first_10_abilities = abilities_data[:10]  # ดึง 10 abilities แรก 

        # สร้าง tasks สำหรับดึงรายละเอียดแต่ละ ability
        tasks = [
            fetch_ability_details(ability["url"], client)
            for ability in first_10_abilities
        ]
        results = await asyncio.gather(*tasks)

        # แสดงผล
        print(f"{'Ability':<20} {'# Pokémon'}")
        print("-" * 30)
        for ability_name, count in results:
            print(f"{ability_name:<20} {count}")

if __name__ == "__main__":
    asyncio.run(main())

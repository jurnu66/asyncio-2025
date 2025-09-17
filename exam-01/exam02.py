# Hint:
# แก้โค้ดให้สามารถรัน หลาย task พร้อมกัน ได้ถูกต้อง
# Result:
# Processing data
# Processing data
# Processing data
# Processing data
# Processing data

import asyncio

async def fetch_data():
    await asyncio.sleep(2)
    return "data"

async def process():
    data = await fetch_data()
    print("Processing", data)

process = [process() for _ in range(5)]
async def main():
    
    
    for task in process:
        asyncio.create_task(task)
    await asyncio.sleep(3)
asyncio.run(main())
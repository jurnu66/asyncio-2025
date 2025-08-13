import asyncio
import time

async def workre_ok():
    print(f"{time.ctime()}: Starting work...")
    await asyncio.sleep(2)  # Simulate non-blocking work
    print(f"{time.ctime()}: Work completed.")
    
async def main():
    asyncio.create_task(workre_ok())
    await asyncio.sleep(2)  

asyncio.run(main())
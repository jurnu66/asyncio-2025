# Asynchronous breakfast
import asyncio
import time

async def make_coffee():
    print("coffee: prepare ingredients")
    await asyncio.sleep(1)
    print("coffee: waiting...")
    await asyncio.sleep(5)
    print("coffee: ready")

async def fry_eggs():
    print("eggs: prepare ingredients")
    await asyncio.sleep(1)
    print("eggs: frying...")
    await asyncio.sleep(3)
    print("eggs: ready")

async def main():
    start = time.time()
    await asyncio.(make_coffee(), fry_eggs())
    print(f"breakfast is ready in {time.time() - start:.2f} seconds.")

asyncio.run(main())


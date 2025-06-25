# get result
import asyncio
async def some_task():
    await asyncio.sleep(1)
    return "เสร็จสิ้น!"

async def main():
    task = asyncio.create_task(some_task())
    await task
    print("ผลลัพธ์:", await task)
# run the main coroutine
asyncio.run(main())
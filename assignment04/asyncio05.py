# Check if a Task is Done
import asyncio

async def some_task():
    await asyncio.sleep(1)
    return "เสร็จสิ้น!"
async def main():
    task = asyncio.create_task(some_task())
    print("ก่อน await ", task.done())
    await task
    print("หลัง await ", task.done())

asyncio.run(main())
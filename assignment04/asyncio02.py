# Create 1 Task with High-Level API
import asyncio
async def do_something():
    print('เริ่มทำงาน...')
    await asyncio.sleep(2)
    print('เสร็จสิ้น!')
async def main():
    task = asyncio.create_task(do_something())
    await task
asyncio.run(main())
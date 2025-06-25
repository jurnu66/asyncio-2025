# get Exception
import asyncio
async def error_task():
    await asyncio.sleep(1)
    raise ValueError("เกิดข้อผิดพลาด!")
async def main():
    try:
        await error_task()
    except Exception as e:
        print("จับข้อผิดพลาด:", e)
asyncio.run(main())
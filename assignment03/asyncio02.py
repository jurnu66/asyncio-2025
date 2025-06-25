# example of running a coroutine
import asyncio
async def custom_coro():
    await asyncio.sleep(1)
async def main():
    await custom_coro()
# run the main coroutine
asyncio.run(main())
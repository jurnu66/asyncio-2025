# event loop
import asyncio
async def greet():
    print('Hello')
    await asyncio.sleep(1) 
    print('world')
asyncio.run(greet())

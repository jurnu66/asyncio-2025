import asyncio
import time 

async def say_after(drelay, message):
    if message == "Hello":
        print(f"{time.ctime()}: {message}is blocking...{drelay} seconds.")
        time.sleep(drelay)  # Blocking call
    else:
        print(f"{time.ctime()}: {message} is non-blocking...{drelay} seconds.")
        await asyncio.sleep(drelay)
        
async def main():
    task1= asyncio .create_task(say_after(1, "Hello"))
    task2 = asyncio.create_task(say_after(5, "World"))
    await task2
    await task1
    
asyncio.run(main())
print("All task done!!.")
    
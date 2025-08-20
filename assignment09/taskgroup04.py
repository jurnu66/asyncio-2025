import asyncio

#coroutine task1
async def task1():
    print("Hello from coroutine 1")
    await asyncio.sleep(1)
# coroutine task2   
async def task2():
    print("Hello from coroutine 2")
    await asyncio.sleep(1)
    
# coroutine task3
async def task3():
    print("Hello from coroutine2")
    await asyncio.sleep(1)  
    
async def main():
    try:
        async with asyncio.TaskGroup() as group:
            # create and run tasks
            t1 = group.create_task(task1())
            t2 = group.create_task(task2())
            t3 = group.create_task(task3())
            # wait for all tasks to complete
        await asyncio.sleep(0.5)
        t2.cancel()  
    except Exception as e:
        print(f"Exception caught: {e}")
    print(f"task1: done={t1.done()}, cancelled={t1.cancelled()}")
    print(f"task2: done={t2.done()}, cancelled={t2.cancelled()}")  
    print(f"task3: done={t3.done()}, cancelled={t3.cancelled()}")
    print(" done")

asyncio.run(main())

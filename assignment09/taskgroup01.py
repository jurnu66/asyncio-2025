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
    print("Hello from coroutine 3")
    await asyncio.sleep(1)  
    
async def main():
    async with asyncio.TaskGroup() as group:
        # create and run tasks
        group.create_task(task1())
        group.create_task(task2())
        group.create_task(task3())
        # wait for all tasks to complete
    print(" done")
asyncio.run(main())
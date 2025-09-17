#
# ให้หาข้อผิดพลาดและแก้ไขโค้ดให้ทำงานถูกต้อง
# Result:
# Task A started
# Task B started
# Task A finished
# Task B finished
# All tasks done

import asyncio

async def task(name):
    print(f"Task {name} started")
    await asyncio.sleep(2)
    print(f"Task {name} finished")

async def main():
    await asyncio.gather(task("A"), task("B"))
    print("All tasks done")

async def main():
    async with asyncio.TaskGroup() as group:
        # create and run tasks
        group.create_task(task(name="A"))
        group.create_task(task(name="B"))
       
    print(" done")
asyncio.run(main())


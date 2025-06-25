# example of getting the current task from the main coroutine
import asyncio

async def main():
	print(f'main coroutine started')
	task = asyncio.current_task()
	print(task)
# run the main coroutine
asyncio.run(main())


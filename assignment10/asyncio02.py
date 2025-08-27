# example of using an asyncio queue without blocking
from random import random
import asyncio


async def producer(queue):
    print('Producer: Running')
    # generate work
    for i in range(10):
       
        value = i
        # block to simulate work
        sleeptime = random()
        print(f'> Producer {value} sleep {sleeptime}')
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f'> Producer put {value}')
        await queue.put(value)

   
    await queue.put(None)
    print('Producer: Done')


async def consumer(queue):
    print('Consumer: Running')
    
    while True:
        
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
   
    print('Consumer: Done')


async def main():
   
    queue = asyncio.Queue()
    
    await asyncio.gather(producer(queue), consumer(queue))


asyncio.run(main())
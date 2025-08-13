import asyncio
import time 
import random


async def save_to_db(sensor_id, value):
    await asyncio.sleep(1)
    print(f"Sensor {time.ctime()}: Sensor {sensor_id} value {value} saved to DB.")
async def main():
    tasks = []
    for sensor_id in range(5):
        value = random.randint(50, 100)
        print(f"Sensor {time.ctime()}: Sensor {sensor_id} reading: {value}")
        task = asyncio.create_task(save_to_db(sensor_id, value))
        tasks.append(task)
    await asyncio.gather(*tasks)
asyncio.run(main())
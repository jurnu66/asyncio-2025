import asyncio
import time
import random   
async def save_to_db(sensor_id, value):
    await asyncio.sleep(1)

    if value > 80:
        raise ValueError(f"Sensor {sensor_id} value too high: {value}")
    print(f"Sensor {time.ctime()} value {value} saved to DB.")
async def handle_sensor(sensor_id):
    value = random.randint(50, 100)
    print(f"Sensor {time.ctime()}: Sensor {sensor_id} reading: {value}")
    asyncio.create_task(save_to_db(sensor_id, value))
async def main():
    for i in range(5):
        await handle_sensor(i)
        await asyncio.sleep(0.5)
asyncio.run(main())
import asyncio
import random


async def read_temperature():
    await asyncio.sleep(1)
    return "temperature:{random.randint(20, 30)}°C"
async def read_humidity():
    await asyncio.sleep(1)
    return "humidity:{random.randint(30, 50)}%" 
async def read_pressure():
    await asyncio.sleep(1)
    return "pressure:{random.randint(1000, 1020)}hPa"   
async def main():
    async with asyncio.TaskGroup() as group:
        temperature_task = group.create_task(read_temperature())
        humidity_task = group.create_task(read_humidity())
        pressure_task = group.create_task(read_pressure())
        
    print(temperature_task.result())
    print(humidity_task.result())
    print(pressure_task.result())
asyncio.run(main())
# This code creates three asynchronous tasks to read temperature, humidity, and pressure.
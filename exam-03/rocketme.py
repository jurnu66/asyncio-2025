import time
import asyncio
import httpx

student_id = "6610301011"

async def fire_rocket(name: str, t0: float):
    url = f"http://172.16.2.117:8088/fire/{student_id}"
    start_time = time.perf_counter() - t0  

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        time_to_target = response.json().get("time_to_target", 0)  
        await asyncio.sleep(time_to_target)  

    end_time = time.perf_counter() - t0  

    return {
        "name": name,
        "start_time": start_time,
        "time_to_target": time_to_target,
        "end_time": end_time
    }

async def main():
    t0 = time.perf_counter()  

    print("Rocket prepare to launch ...")  

    rocket_names = ["Alpha", "Bravo", "Charlie", "Delta"]
    tasks = [fire_rocket(name, t0) for name in rocket_names]

    results = await asyncio.gather(*tasks)

    for r in results:
        print(f"Rocket {r['name']}: start_time={r['start_time']:.2f}, time_to_target={r['time_to_target']:.2f}, end_time={r['end_time']:.2f}")

    t_total = time.perf_counter() - t0
    print(f"\nTotal time for all rockets: {t_total:.2f} sec")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())

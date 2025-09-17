import asyncio, time, httpx

student_id = "6610301011"   # ใส่รหัสนักศึกษา

async def fire_rocket(name: str, t0: float):
    url = f"http://127.0.0.1:8088/fire/{student_id}"
    start_time = time.perf_counter() - t0

    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        r.raise_for_status()
        data = r.json()
        time_to_target = data.get("time_to_target", 0.0)
        await asyncio.sleep(time_to_target)

    end_time = time.perf_counter() - t0
    return {
        "name": name,
        "start_time": start_time,
        "time_to_target": time_to_target,
        "end_time": end_time
    }

async def main():
    print("Rocket prepare to launch ...")
    t0 = time.perf_counter()

    # ยิง 3 ลูกพร้อมกัน
    tasks = [
        asyncio.create_task(fire_rocket(f"Rocket-{i+1}", t0))
        for i in range(3)
    ]
    results = await asyncio.gather(*tasks)

    # เรียงตามเวลาถึงจุดหมาย
    results.sort(key=lambda x: x["end_time"])

    for r in results:
        print(f"{r['name']} | start_time: {r['start_time']:.2f} sec | "
              f"time_to_target: {r['time_to_target']:.2f} sec | "
              f"end_time: {r['end_time']:.2f} sec")

    total_time = max(r["end_time"] for r in results)
    print(f"\nTotal time for all rockets: {total_time:.2f} sec")

if __name__ == "__main__":
    asyncio.run(main())
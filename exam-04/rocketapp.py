from fastapi import FastAPI, HTTPException
import asyncio
import random

app = FastAPI(title="Asynchronous Rocket Launcher")

# เก็บ task ของจรวด (optional)
rockets = []

async def launch_rocket(student_id: str):

    time_to_target = round(random.uniform(1, 2), 2)
    print(f"Rocket {student_id} launched! ETA: {time_to_target:.2f} seconds")
    await asyncio.sleep(time_to_target)
    print(f"Rocket {student_id} reached destination after {time_to_target:.2f} seconds")
    return time_to_target

@app.get("/fire/{student_id}")
async def fire_rocket(student_id: str):
   
    if len(student_id) != 10 or not student_id.isdigit():
        raise HTTPException(status_code=400, detail="Invalid student ID. Must be 10 digits.")

    # สุ่มเวลาระหว่าง 1 ถึง 2 วินาที
    time_to_target = round(random.uniform(1, 2), 2)

    # สร้าง background task
    task = asyncio.create_task(launch_rocket(student_id))
    rockets.append(task)  # เก็บ task ไว้ (optional)

    # รอ delay ก่อนตอบกลับ
    await asyncio.sleep(time_to_target)

    return {
        "message": f"Rocket {student_id} fired!",
        "time_to_target": time_to_target
    }

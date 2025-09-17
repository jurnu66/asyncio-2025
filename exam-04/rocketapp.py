# rocketapp.py
from fastapi import FastAPI, HTTPException
import asyncio, random

app = FastAPI()

@app.get("/fire/{student_id}")
async def fire(student_id: str):
    # ตรวจสอบ student_id ต้องมี 10 หลัก และเป็นตัวเลข
    if len(student_id) != 10 or not student_id.isdigit():
        raise HTTPException(status_code=400, detail="Invalid student_id")

    # สุ่มเวลาเดินทาง 1–2 วินาที
    time_to_target = round(random.uniform(1, 2), 2)

    # สร้าง background task จำลองการบิน
    asyncio.create_task(launch_rocket(student_id, time_to_target))

    return {
        "message": f"Rocket {student_id} fired!",
        "time_to_target": time_to_target
    }

async def launch_rocket(student_id: str, eta: float):
    print(f"Rocket {student_id} launched! ETA: {eta:.2f} sec")
    await asyncio.sleep(eta)
    print(f"Rocket {student_id} reached destination after {eta:.2f} sec")


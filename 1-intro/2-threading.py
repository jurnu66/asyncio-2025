import time
from datetime import datetime

def make_burger(student_id):
    start_time = time.time()  # ✅ เริ่มจับเวลา

    print(f"[{datetime.now().strftime('%H:%M:%S')}] เริ่มทำเบอร์เกอร์ให้นักเรียนคนที่ {student_id}")
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 1. ทอดเบอร์เกอร์...")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 2. ทอดไก่...")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 3. ใส่ผักและชีส...")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 4. ห่อเบอร์เกอร์...")
    time.sleep(5)

    end_time = time.time()  # ✅ จับเวลาหลังเสร็จ
    done_time_str = datetime.now().strftime('%H:%M:%S')  # ✅ เวลาปัจจุบันในรูปแบบสวยงาม
    duration = end_time - start_time  # ✅ เวลาที่ใช้ในการทำเบอร์เกอร์ของนักเรียนคนนี้

    print(f"[{done_time_str}] เสร็จแล้ว! เบอร์เกอร์ของนักเรียนคนที่ {student_id}!")
    print(f"--> นักเรียนคนที่ {student_id} ได้รับเบอร์เกอร์เวลา {done_time_str} ใช้เวลา {duration:.2f} วินาที\n")

def main():
    start = time.time()
    
    for i in range(1, 100):
        make_burger(i)
    
    end = time.time()
    total_duration = end - start
    print(f"[{datetime.now().strftime('%H:%M:%S')}] รวมเวลาทั้งหมด: {total_duration:.2f} วินาที")

if __name__ == "__main__":
    main()

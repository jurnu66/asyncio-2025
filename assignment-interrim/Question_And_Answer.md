# Question
1. ถ้าสร้าง asyncio.create_task(*tasks) ที่ไม่มี await ที่ main() เกิดอะไรบ้าง
   1. งานถูก “จัดคิว” แล้วเริ่มวิ่งแบบขนาน ทันทีที่ event loop หมุน—แต่ main() จะไม่รอพวกมันให้เสร็จเอง
   2. ถ้า main จบและ loop ปิด ก่อนงานเสร็จ: งานที่ยังค้างจะถูกยกเลิกถูกทำลาย  
   3. จะ ไม่ได้ผลลัพธ์ ข้อผิดพลาด
2. ความแตกต่างระหว่าง asyncio.gather(*tasks) กับ asyncio.wait(tasks) คืออะไร
   1. gather → โดยปกติ “รอทั้งหมด” ให้จบ (ยกเว้นเจอ exception แบบไม่ return_exceptions)
   2. wait → เลือกได้ ALL_COMPLETED / FIRST_COMPLETED / FIRST_EXCEPTION และมี timeout ให้ด้วย
   3. ..

   1. สร้าง create_task() และ coroutine ของ http ให้อะไรต่างกัน
   1. await do_http() ตรงๆ → ลำดับก่อน-หลัง (sequential): งานนี้เสร็จก่อน ค่อยงานถัดไป (ง่าย ควบคุมทรัพยากรง่าย)
   2. ..
   3. ..

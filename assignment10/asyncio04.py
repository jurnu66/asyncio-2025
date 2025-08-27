import asyncio
import time


# รายการสินค้าของลูกค้าแต่ละคน
customers = {
    "Alice": ["Apple", "Banana", "Milk"],
    "Bob": ["Bread", "Cheese"],
    "Charlie": ["Eggs", "Juice", "Butter"]
}

# เวลาในการคิดเงินต่อสินค้า (วินาที)
cashier_times = {
    "Cashier-1": 1,
    "Cashier-2": 2
}

# สร้าง queue กลาง
queue = asyncio.Queue()


async def customer(name, items):
    """Customer คือ producer"""
    print(f"[{time.ctime()}] [{name}] finished shopping: {items}")
    await queue.put((name, items))


async def cashier(name, process_time):
    """Cashier คือ consumer"""
    while True:
        customer_data = await queue.get()
        if customer_data is None:
            break
        customer_name, items = customer_data
        print(f"[{time.ctime()}] [{name}] processing {customer_name} with orders {items}")
        for item in items:
            await asyncio.sleep(process_time)
        print(f"[{time.ctime()}] [{name}] finished {customer_name}")
        queue.task_done()
    print(f"[{time.ctime()}] [{name}] closed")


async def main():
    # สร้าง task ของแคชเชียร์ก่อน
    cashier1 = asyncio.create_task(cashier("Cashier-1", cashier_times["Cashier-1"]))
    cashier2 = asyncio.create_task(cashier("Cashier-2", cashier_times["Cashier-2"]))

    # ส่งลูกค้าเข้า queue
    producers = []
    for name, items in customers.items():
        producers.append(asyncio.create_task(customer(name, items)))

    await asyncio.gather(*producers)

    # รอให้สินค้าทั้งหมดใน queue ถูกจัดการ
    await queue.join()

    # ปิด cashier อย่างปลอดภัย
    await queue.put(None)
    await queue.put(None)

    await asyncio.gather(cashier1, cashier2)
    print(f"[{time.ctime()}] [Main] Supermarket closed!")


# เริ่มโปรแกรม
asyncio.run(main())
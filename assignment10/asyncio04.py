import asyncio
import time

# รายการสินค้าของลูกค้าแต่ละคน (10 คน)
customers = {
    "Alice": ["Apple", "Banana", "Milk"],
    "Bob": ["Bread", "Cheese"],
    "Charlie": ["Eggs", "Juice", "Butter"],
    "David": ["Milk", "Butter"],
    "Eva": ["Juice", "Apple"],
    "Frank": ["Bread", "Eggs"],
    "Grace": ["Cheese", "Juice"],
    "Henry": ["Banana", "Apple", "Bread"],
    "Ivy": ["Milk", "Cheese"],
    "Jack": ["Eggs", "Juice", "Banana"]
}

# เวลาคิดเงินต่อสินค้า (วินาที)
cashier_times = {
    "Cashier-1": 1,
    "Cashier-2": 2
}

# คิวจำกัดความยาวสูงสุด 5
queue = asyncio.Queue(maxsize=5)


async def customer(name, items):
    print(f"[{time.ctime()}] [{name}] finished shopping: {items}")
    await queue.put((name, items))


async def cashier(name, process_time):
    try:
        while True:
            customer_data = await queue.get()
            try:
                customer_name, items = customer_data
                print(f"[{time.ctime()}] [{name}] processing {customer_name} with orders {items}")
                for item in items:
                    await asyncio.sleep(process_time)
                print(f"[{time.ctime()}] [{name}] finished {customer_name}")
            finally:
                queue.task_done()
    except asyncio.CancelledError:
        print(f"[{time.ctime()}] [{name}] closed")


async def main():
    # สร้างแคชเชียร์
    cashier1 = asyncio.create_task(cashier("Cashier-1", cashier_times["Cashier-1"]))
    cashier2 = asyncio.create_task(cashier("Cashier-2", cashier_times["Cashier-2"]))

    # สร้างลูกค้า 10 คน
    producers = []
    for name, items in customers.items():
        producers.append(asyncio.create_task(customer(name, items)))

    await asyncio.gather(*producers)
    await queue.join()

    # ปิดแคชเชียร์
    cashier1.cancel()
    cashier2.cancel()
    await asyncio.gather(cashier1, cashier2)

    print(f"[{time.ctime()}] [Main] Supermarket closed!")


# เริ่มโปรแกรม
asyncio.run(main())

import asyncio, time

async def download_file(file_name, size_mb, delay):
    start = time.time()
    await asyncio.sleep(delay)
    speed = size_mb / (time.time() - start)
    return file_name, size_mb, speed

async def main():
    files = [("file1.txt", 300, 3), ("file2.txt", 200, 2), ("file3.txt", 100, 1)]
    results = await asyncio.gather(*[download_file(f, s, d) for f, s, d in files])
    avg_speed = sum(speed for _, _, speed in results) / len(results)
    print(f"Average speed: {avg_speed:.2f} MB/s")

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(f"Completed in {time.time() - start:.2f} seconds.")

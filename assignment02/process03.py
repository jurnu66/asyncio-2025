import multiprocessing
from time import sleep, ctime, time

def xlibm_processor(index):
    print(f"{ctime()} Xlibm-{index}: Processing started")
    sleep(1.5)  # Simulate processing time
    print(f"{ctime()} Xlibm-{index}: Processing completed")

def como_processor(index):
    print(f"{ctime()} Como-{index}: Processing started")
    sleep(2.0)  # Simulate processing time
    print(f"{ctime()} Como-{index}: Processing completed")

def subn_processor(index):
    print(f"{ctime()} Subn-{index}: Processing started")
    sleep(1.0)  # Simulate processing time
    print(f"{ctime()} Subn-{index}: Processing completed")

if __name__ == "__main__":
    print(f"{ctime()} Main: Starting path processing system")
    start_time = time()
    
    processes = []
    
    # Create 2 xlibm processors
    for i in range(2):
        p = multiprocessing.Process(target=xlibm_processor, args=(i,))
        processes.append(p)
        p.start()
    
    # Create 2 como processors
    for i in range(2):
        p = multiprocessing.Process(target=como_processor, args=(i,))
        processes.append(p)
        p.start()
    
    # Create 2 subn processors
    for i in range(2):
        p = multiprocessing.Process(target=subn_processor, args=(i,))
        processes.append(p)
        p.start()
    
    # Wait for all processes to complete
    for p in processes:
        p.join()
    
    duration = time() - start_time
    print(f"{ctime()} Main: All processing completed in {duration:0.2f} seconds")
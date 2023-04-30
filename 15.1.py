import multiprocessing
import time
import random

def worker():
    wait_time = random.random()
    time.sleep(wait_time)
    print(f"Current time: {time.ctime()}")
    return

if __name__ == '__main__':
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

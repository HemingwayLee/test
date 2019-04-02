import time
import random
from concurrent.futures import ThreadPoolExecutor, wait, as_completed

def add(name):
    res = random.randint(1, 5)
    res = 2
    time.sleep(res)
    print("[!] {}: {}".format(name, res))
    return name

pool = ThreadPoolExecutor(5)
futures = []
for x in range(10):
    futures.append(pool.submit(add, "Thread-{}".format(x)))
    print("Added: Thread-{}".format(x))

for x in as_completed(futures):
    print("{} completed".format(x.result()))

print("Done")
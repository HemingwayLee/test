from threading import Thread
import time

def sam():
    print('started')
    time.sleep(10)
    print('waiting for 10sec')

t = Thread(target=sam)
t.start()

print("before join...")
t.join()
print("after join...")
import threading
import time

is_lock = True
if is_lock is True:
    threading.Lock()

def create_task(message):
    for _ in range(10):
        print(message)
        time.sleep(1)



thread_1 = threading.Thread(target=create_task, args=("send task 1",))
thread_2 = threading.Thread(target=create_task, args=("send task 2",))

thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
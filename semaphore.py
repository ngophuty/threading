import threading
import time

semaphore = threading.Semaphore(value=3)

def access_resource(message):
    semaphore.acquire()
    print('this is message', message)
    semaphore.release()


threads = []
for i in range(10):
    thread = threading.Thread(target=access_resource, args=(i,))
    threads.append(thread)


for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
import queue
import threading
import time

job_queue = queue.Queue()

def do_work(job):
    print("Starting job", job)
    time.sleep(1)


def worker():
    while True:
        try: 
            job = job_queue.get(timeout=1)
            do_work(job)
            job_queue.task_done()
        except Exception:
            break

for i in range(10):
    job_queue.put(i)

workers = []
for i in range(4):
    worker_thread = threading.Thread(target=worker)
    worker_thread.start()
    workers.append(worker_thread)

job_queue.join()

for worker_thread in workers:
    worker_thread.join()


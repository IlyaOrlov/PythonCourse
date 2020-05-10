import threading

local_data = threading.local()


def thread_id(*args):
    local_data.t = args
    print(threading.current_thread().name + " contains " + ''.join(local_data.t))


strings = ["Sample string 1", "Sample string 2", "Sample string 3"]

threads = []
for string in strings:
    thr = threading.Thread(target=thread_id, args=string)
    thr.start()
    threads.append(thr)

for thr in threads:
    thr.join()

import time

class Manager_time:

    def __enter__(self):
        self.start_time = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.perf_counter() - self.start_time
        print('Execution time {}'.format(self.end_time))


with Manager_time():
    def max_in_lst(lst):
        m = lst[0]
        for i in lst:
            if i > m:
                m = i
        return m




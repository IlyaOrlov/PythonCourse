#for Python 3.6
#lecture 5 task 3

from time import time, sleep

class Time_context:

    def __enter__(self):
        print("Starting function")
        self.start_moment = time()

    def __exit__(self, *args):
        print("Runtime: {:.3f} sec".format(time() - self.start_moment))


def example_fun():
    sleep(3)
    print("I've done something important")


if __name__ == '__main__':

    with Time_context():
        example_fun()

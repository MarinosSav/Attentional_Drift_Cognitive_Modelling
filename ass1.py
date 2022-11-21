import numpy
import time


def start():

    start_time = time.time()

    return round((time.time() - start_time) * 1000)


def perceptualstep():

    start_time = time.time()

    return round((time.time() - start_time) * 1000)


def cognitivestep():

    start_time = time.time()

    return round((time.time() - start_time) * 1000)


def motorstep():

    start_time = time.time()

    return round((time.time() - start_time) * 1000)


def example1():

    total_time = start()
    total_time += perceptualstep()
    total_time += cognitivestep()
    total_time += motorstep()

    return total_time

def main():
    pass


if __name__ == '__main__':
    main()

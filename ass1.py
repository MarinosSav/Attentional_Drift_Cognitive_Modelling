import numpy
import time


def start():

    start_time = time.time()

    return round((time.time() - start_time) * 1000)


def perceptualstep():

    t_percept = 100

    start_time = time.time()

    return round((time.time() - start_time) * 1000) + t_percept


def cognitivestep():

    t_cog = 70

    start_time = time.time()

    return round((time.time() - start_time) * 1000) + t_cog


def motorstep():

    t_motor = 70

    start_time = time.time()

    return round((time.time() - start_time) * 1000) + t_motor


def example1():

    total_time = start()
    total_time += perceptualstep()
    total_time += cognitivestep()
    total_time += motorstep()

    return total_time

def main():

    print(example1())


if __name__ == '__main__':
    main()

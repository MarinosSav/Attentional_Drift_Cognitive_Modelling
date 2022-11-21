import numpy
import time
import matplotlib.pyplot as plt

TYPES = {"fast", "middle", "slow"}

def start():

    start_time = time.time()

    return round((time.time() - start_time) * 1000)


def perceptualstep(type="middle"):

    if type == "fast":
        t_percept = 50
    elif type == "slow":
        t_percept = 200
    else:
        t_percept = 100

    start_time = time.time()

    return round((time.time() - start_time) * 1000) + t_percept


def cognitivestep(type="middle"):

    if type == "fast":
        t_cog = 25
    elif type == "slow":
        t_cog = 170
    else:
        t_cog = 70

    start_time = time.time()

    return round((time.time() - start_time) * 1000) + t_cog


def motorstep(type="middle"):

    if type == "fast":
        t_motor = 30
    elif type == "slow":
        t_motor = 100
    else:
        t_motor = 70

    start_time = time.time()

    return round((time.time() - start_time) * 1000) + t_motor


def example1():

    total_time = start()
    total_time += perceptualstep()
    total_time += cognitivestep()
    total_time += motorstep()

    return total_time

def example2(completeness="extremes"):

    time_list = []
    if completeness == "extremes":
        for type in TYPES:
            total_time = start()
            total_time += perceptualstep(type=type)
            total_time += cognitivestep(type=type)
            total_time += motorstep(type=type)
            time_list.append(total_time)
    elif completeness == "all":
        for type_i in TYPES:
            for type_j in TYPES:
                for type_z in TYPES:
                    total_time += perceptualstep(type=type_i)
                    total_time += cognitivestep(type=type_j)
                    total_time += motorstep(type=type_z)
                    time_list.append(total_time)
        plt.boxplot(time_list)


    return time_list


def main():

    print(example2())


if __name__ == '__main__':
    main()

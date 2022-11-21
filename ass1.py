import numpy as np
import time
import matplotlib.pyplot as plt

TYPES = ["fast", "middle", "slow"]

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
                    total_time = start()
                    total_time += perceptualstep(type=type_i)
                    total_time += cognitivestep(type=type_j)
                    total_time += motorstep(type=type_z)
                    time_list.append(total_time)
        plt.boxplot(time_list)
        plt.show()

    return time_list


def example3():

    time_list = []
    for type_i in TYPES:
        for type_j in TYPES:
            for type_z in TYPES:
                total_time = start()
                total_time += perceptualstep(type=type_i)
                total_time += perceptualstep(type=type_i)
                total_time += cognitivestep(type=type_j)
                total_time += cognitivestep(type=type_j)
                total_time += motorstep(type=type_z)
                if type_i == "fast" and type_j == "middle" and type_z == "slow":
                    print(total_time)
                time_list.append(total_time)

    return time_list


def example4():

    stimulus2_time_options = [40, 80, 110, 150, 210, 240]

    time_list = []
    for stimulus2_time in stimulus2_time_options:
        for type_i in TYPES:
            for type_j in TYPES:
                for type_z in TYPES:
                    total_time = start()
                    total_time += perceptualstep(type=type_i)
                    total_time += perceptualstep(type=type_i) + stimulus2_time
                    total_time += cognitivestep(type=type_j)
                    total_time += cognitivestep(type=type_j)
                    total_time += motorstep(type=type_z)
                    time_list.append(total_time)

    return time_list


def example5():

    error = 0.01
    error_dict = {"fast": 3, "middle": 2, "slow": 0.5}

    time_list = []
    error_list = []
    for type_i in TYPES:
        for type_j in TYPES:
            for type_z in TYPES:
                total_time = start()
                total_time += perceptualstep(type=type_i)
                total_time += perceptualstep(type=type_i)
                error += error * error_dict[type_i]
                total_time += cognitivestep(type=type_j)
                total_time += cognitivestep(type=type_j)
                error += error * error_dict[type_j]
                total_time += motorstep(type=type_z)
                error += error * error_dict[type_z]
                time_list.append(total_time)
                error_list.append(error)
                error = 0.01

    #print(error_list)
    plt.scatter(np.array(time_list), np.array(error_list))
    plt.xlabel("time (ms)")
    plt.ylabel("error (%)")
    plt.title("Time and Error for Human Processor Task for Different Input Types")
    plt.show()

    return



def main():

    print(example5())


if __name__ == '__main__':
    main()

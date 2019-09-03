from sys import argv
from matplotlib import pyplot as plt
import numpy as np
import math

if __name__ == "__main__":
    order = int(argv[1])
    x_list = [float(x) for x in input().split(",")]
    y_list = [float(y) for y in input().split(",")]

    b = []
    a = []

    for current_row in range(order):
        b_i = sum([y * x_list[idx]**current_row for idx,y in enumerate(y_list)])
        a_i = []
        for current_column in range(order):
            a_ij = sum([x **(current_row + current_column) for x in x_list])
            a_i.append(a_ij)

        b.append(b_i)
        a.append(a_i)

    a = np.matrix(a)
    b = np.asarray(b)

    w = np.linalg.solve(a,b)
    w_list = w.tolist() 

    print("Coefficients:")
    print(w_list)

    estimated_y_list = []
    for idx,y in enumerate(y_list):
        estimated_y = sum([x_list[idx]**(power + 1) * w for power,w in enumerate(w_list[1:])]) + w_list[0]
        estimated_y_list.append(estimated_y)
        print(x_list[idx], y, estimated_y)
    exact_y_list = [math.sin(-3/2 * math.pi * x) + 1/3 * math.sin(5 * math.pi * x) for x in x_list]
    plt.style.use("ggplot")

    fig, axes = plt.subplots()
    axes.plot(x_list, y_list, label = "Gaussian-noised", lw = 5)
    axes.plot(x_list, estimated_y_list, label = "Fitted", lw = 5)
    axes.plot(x_list, exact_y_list, label = "Original", lw = 5)

    axes.set_title("Least squares fitting")
    axes.legend()

    fig.savefig("3rd_degree.png")



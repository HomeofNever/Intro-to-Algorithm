from checkpoint1 import init_array
from checkpoint2 import strong_connected
import matplotlib.pyplot as plt
import numpy as np


def draw(x, y):
    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('x - axis: C')
    # naming the y axis
    plt.ylabel('y - axis: Percentage')

    # giving a title to my graph
    plt.title('Analysis of Strongly connected component')

    # function to show the plot
    plt.show()


def analysis(c_bottom, c_top, step_size, thold, num, n, equation=lambda c, n: c / n):
    c_data = []
    p_data = []
    for current_c in np.arange(c_bottom, c_top, step_size):
        p = current_c / n

        scc = 0
        for i in range(0, num):
            array = init_array(n, p)
            scc += strong_connected(array, thold)

        percentage = float(scc) / float(num)

        c_data.append(current_c)
        p_data.append(percentage)

        current_c += step_size

    return (c_data, p_data)


if __name__ == '__main__':
    thold = 30
    n = 40
    c_bottom = 0.2
    c_top = 3.0
    step_size = 0.2
    num = 500
    c_data, p_data = analysis(c_bottom, c_top, step_size, thold, num, n)

    draw(c_data, p_data)

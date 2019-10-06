# imports 
import matplotlib.pyplot as plt
import numpy as np

def prob_for_known_normal_dist(x, m, var):
    return 1 / np.sqrt(2 * np.pi * var) * np.e **(-1 * ((x - m)**2) / (2 * var))

def plot_normal_distribution(m, var):
    fig, axes = plt.subplots()
    plt.style.use("seaborn")
    x = np.linspace(-5, 5, 100)
    normal_sample = np.random.normal(m, var, 10)
    sample_y = np.zeros(10)
    axes.plot(x, prob_for_known_normal_dist(x, m, var), '-', label = "normal")
    axes.plot(normal_sample, sample_y, 'p', label = "sample")
    axes.set_title("normal distribution, folks")
    axes.legend()
    fig.savefig("0_5.png")

if __name__ == "__main__":
    plot_normal_distribution(0,5)


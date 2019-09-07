import sys
import numpy as np
import matplotlib.pyplot as plt

def my_normal_sample_generator(sample_size = 1000, mean = 0, std = 1):
    """
    Given sample size, mean and std returns an array of elements belonging to normal distribution
    """
    all_values = np.array([])
    for x in np.arange(mean - 4 * std, mean + 4 * std, 8 * std / 100):
        y = 1 / np.sqrt(2 * np.pi * std ** 2) * np.e ** -(((x - mean) ** 2)/ 2 * std ** 2)
        for i in range(int(10000 * y)):
            all_values = np.append(all_values,[x])

    # final sampling
    indexes_array = np.random.randint(0, len(all_values), sample_size)
    return all_values[indexes_array]

if __name__ == "__main__":
    mean, std = sys.argv[1:3]
    sample_size = int(input("Give me sample size! "))
    normal_sample = my_normal_sample_generator(sample_size, float(mean), float(std))
    
    m = np.mean(normal_sample)
    s = np.sum((normal_sample - m)**2) / len(normal_sample)
    print(f"m = {m}")
    print(f"s2 = {s}")

    fig, axes = plt.subplots()
    plt.style.use("ggplot")
    axes.hist(normal_sample, bins = 100)
    fig.savefig("lets_see.png")

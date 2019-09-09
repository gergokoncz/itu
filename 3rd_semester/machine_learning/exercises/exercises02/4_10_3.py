import sys
import numpy as np
import matplotlib.pyplot as plt
import math

def my_normal_sample_generator(sample_size = 1000, mean = 0, std = 1):
    """
    Given sample size, mean and std returns an array of elements belonging to normal distribution
    """
    all_values = np.array([], dtype = "float16")
    for x in np.arange(mean - 4 * std, mean + 4 * std, 8 * std / 1000):
        y = 1 / math.sqrt(2 * np.pi * std ** 2) * np.e ** (-1 * (((x - mean) ** 2) / (2 * (std ** 2))))
        current_values = np.full(shape = int(y * 10000), fill_value = x, dtype = "float16")
        all_values = np.append(all_values, current_values)

    fig, axes = plt.subplots()
    plt.style.use("ggplot")
    axes.hist(all_values, bins = 100)
    axes.set_ylabel("y")
    axes.set_title("current normal distribution")
    fig.savefig("lets_see.png")
    # final sampling
    indexes_array = np.random.randint(0, len(all_values), sample_size)
    return all_values[indexes_array]

def prob_for_known_parameters(mean, std):
    return 1 / math.sqrt(2 * np.pi * std ** 2) * np.e ** (-1 * (((x - mean) ** 2) / (2 * (std ** 2))))

def solution_3():
    mean = float(input("give me mean: "))
    std = float(input("give me std: "))
    sample_size = int(input("give me sample size: "))
    normal_sample = my_normal_sample_generator(sample_size, mean, std)
    
    m = np.mean(normal_sample)
    s2 = np.sum((normal_sample - m) ** 2) / len(normal_sample)
    print(f"m = {m}")
    print(f"s2 = {s2}")
    # needs bayes
    bayes = (sample_size / np.var(normal_sample)) / ((sample_size / np.var(normal_sample)) + (1 / std**2)) * m + (1 / std**2) / (sample_size / np.var(normal_sample) + 1 / std**2) * mean ## according to 4.18
    print(f"bayes = {bayes}")

def solution_6():
    mean1 = float(input("give me mean1: "))
    std1 = float(input("give me std1: "))
    sample_size1 = int(input("give me sample size1: "))
    normal_sample1 = my_normal_sample_generator(sample_size1, mean1, std1)

    m1 = np.mean(normal_sample1)
    s2_1 = np.sum((normal_sample1 - m1) ** 2) / len(normal_sample1)

    print(f"m1 = {m1}\ts2_1 = {s2_1}")

    mean2 = float(input("give me mean2: "))
    std2 = float(input("give me std2: "))
    sample_size2 = int(input("give me sample size2: "))
    normal_sample2 = my_normal_sample_generator(sample_size2, mean2, std2)

    m2 = np.mean(normal_sample2)
    s2_2 = np.sum((normal_sample2 - m2) ** 2) / len(normal_sample2)

    print(f"m2 = {m2}\ts2_2 = {s2_2}")
    
    fig, axes = plt.subplots()
    plt.style.use("ggplot")
    axes.hist(normal_sample1, bins = 100)
    axes.hist(normal_sample2, bins = 100)
    axes.set_ylabel("y")
    axes.set_title("current normal distribution")
    fig.savefig("two.png")

    coeffs_estimate = [-2 * s2_2 + 2 * s2_1, 4 * (m1 * s2_2 - m2 * s2_1), s2_1 * s2_2 * 4 * (- np.log(np.sqrt(s2_1)) + np.log(np.sqrt(s2_2))) - 2 * s2_2 * (m1 ** 2) + 2 * s2_1 * (m2 ** 2)]
    print(f"estimate discriminant points = {np.roots(coeffs_estimate)}")

    m1 = mean1
    m2 = mean2
    s2_1 = std1 ** 2
    s2_2 = std2 ** 2

    coeffs_theoretical = [-2 * s2_2 + 2 * s2_1, 4 * (m1 * s2_2 - m2 * s2_1), s2_1 * s2_2 * 4 * (- np.log(np.sqrt(s2_1)) + np.log(np.sqrt(s2_2))) - 2 * s2_2 * (m1 ** 2) + 2 * s2_1 * (m2 ** 2)]
    print(f"theoretical discriminant points = {np.roots(coeffs_theoretical)}")

if __name__ == "__main__":
    if sys.argv[1] == "3":
        solution_3()
    else:
        solution_6()

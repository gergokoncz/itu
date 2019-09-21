import numpy as np

def iris_reader():
    all_data = np.array([])
    with open("iris.txt", 'r') as this_file:
        for line in this_file.readlines():
            all_data = np.append(all_data, np.array(line.replace(',', '').strip().split(' '), dtype = "float16"))
    return np.reshape(all_data, (150,4))


if __name__ == "__main__":
    all_data = iris_reader()
    print(all_data.shape)
    print(np.amax(all_data, axis = 0))
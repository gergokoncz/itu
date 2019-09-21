import numpy as np

def iris_reader():
    all_data = np.array([])
    with open("iris.txt", 'r') as this_file:
        for line in this_file.readlines():
            all_data = np.append(all_data, np.array(line.replace(',', '').strip().split(' '), dtype = "float16"))
    return np.reshape(all_data, (150,4))

def clusterer(input_data, number_of_clusters):
    np.random.seed(125)
    max_values = np.amax(input_data, axis = 0).tolist()
    min_values = np.amin(input_data, axis = 0).tolist()
    m_s = [[np.random.uniform(low = min_value, high = max_values[idx]) for idx, min_value in enumerate(min_values)] for i in range(number_of_clusters)]
    print(m_s)

if __name__ == "__main__":
    all_data = iris_reader()
    number_of_clusters = int(input('n of clusters: '))
    clusterer(input_data = all_data, number_of_clusters=number_of_clusters)

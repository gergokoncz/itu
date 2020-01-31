import numpy as np

def iris_reader():
    all_data = np.array([])
    with open("iris.txt", 'r') as this_file:
        for line in this_file.readlines():
            all_data = np.append(all_data, np.array(line.replace(',', '').strip().split(' '), dtype = "float16"))
    return np.reshape(all_data, (150,4))

def clusterer(input_data, number_of_clusters):
    np.random.seed(125)

    # initial values for cluster centers
    max_values = np.amax(input_data, axis = 0).tolist()
    min_values = np.amin(input_data, axis = 0).tolist()
    m_s = [[np.random.uniform(low = min_value, high = max_values[idx]) for idx, min_value in enumerate(min_values)] for i in range(number_of_clusters)]
    cluster_center_printer(m_s)

    # run the whole optimization 
    n_of_cycles = int(input("give me number of cycles: "))
    for i in range(n_of_cycles):
        # expectaion round
        labels = []
        for row in input_data:
            label = 0
            min_distance = 1000
            for idx,m in enumerate(m_s):
                distance = sum([(m[i] - row[i]) ** 2 for i in range(len(row))])
                if distance < min_distance:
                    label = idx
                    min_distance = distance
            labels.append(label)

        # maximization round
        for i in range(len(m_s)):
            sums = [0 for m in m_s[i]]
            n_of_elements = 0
            for idx,label in enumerate(labels):
                if label == i:
                    n_of_elements += 1
                    for this_id,value in enumerate(sums):
                        sums[this_id] += input_data[idx, this_id]
            print(f"cluster {label} has {n_of_elements} elements")
            m_s[i] = [this_sum / n_of_elements for this_sum in sums]
        
        cluster_center_printer(m_s)
    
    # to check labels
    with open("my_labels.txt", "w") as this_file:
        for label in labels:
            this_file.write(f"{label}\n")

def cluster_center_printer(cluster_center):
    cluster_center = [[str(x) for x in row] for row in cluster_center]
    for idx,row in enumerate(cluster_center):
        print(f"cluster_id: {idx}")
        print("\t".join(row))

if __name__ == "__main__":
    all_data = iris_reader()
    number_of_clusters = int(input('n of clusters: '))
    clusterer(input_data = all_data[:, [0,2]], number_of_clusters=number_of_clusters)

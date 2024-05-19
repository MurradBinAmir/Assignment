import math
from collections import Counter

def euclidean_distance(point1, point2):
    distance = 0.0
    for i in range(len(point1) - 1):  # Exclude the label from the distance calculation
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)

def get_neighbors(training_data, test_point, k):
    distances = []
    for train_point in training_data:
        dist = euclidean_distance(test_point, train_point)
        distances.append((train_point, dist))
    distances.sort(key=lambda x: x[1])
    neighbors = [distances[i][0] for i in range(k)]
    return neighbors

def predict_classification(training_data, test_point, k):
    neighbors = get_neighbors(training_data, test_point, k)
    output_values = [row[-1] for row in neighbors]  # Extract the class labels
    prediction = Counter(output_values).most_common(1)[0][0]
    return prediction

# Example usage
if __name__ == "__main__":
    # Example dataset: [feature1, feature2, ..., featureN, label]
    training_data = [
        [2.7810836, 2.550537003, 0],
        [1.465489372, 2.362125076, 0],
        [3.396561688, 4.400293529, 0],
        [1.38807019, 1.850220317, 0],
        [3.06407232, 3.005305973, 0],
        [7.627531214, 2.759262235, 1],
        [5.332441248, 2.088626775, 1],
        [6.922596716, 1.77106367, 1],
        [8.675418651, -0.242068655, 1],
        [7.673756466, 3.508563011, 1]
    ]
    
    test_point = [3.5, 3.5]
    k = 3
    prediction = predict_classification(training_data, test_point, k)
    print(f'Predicted class for test point {test_point} is: {prediction}') 
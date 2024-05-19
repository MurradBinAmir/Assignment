import csv
import random
from typing import List, Any, Tuple, Dict
import numpy as np

# Helper function to load a CSV file
def load_csv(filename: str) -> List[List[str]]:
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        dataset = list(csv_reader)
    return dataset

# Calculate Gini index for a split dataset
def gini_index(groups: List[List[List[Any]]], classes: List[Any]) -> float:
    n_instances = sum([len(group) for group in groups])
    gini = 0.0
    for group in groups:
        size = len(group)
        if size == 0:
            continue
        score = 0.0
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        gini += (1.0 - score) * (size / n_instances)
    return gini

# Split a dataset based on an attribute and attribute value
def test_split(index: int, value: Any, dataset: List[List[Any]]) -> Tuple[List[List[Any]], List[List[Any]]]:
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right

# Select the best split point for a dataset
def get_split(dataset: List[List[Any]]) -> Dict[str, Any]:
    class_values = list(set(row[-1] for row in dataset))
    b_index, b_value, b_score, b_groups = 999, 999, 999, None
    for index in range(len(dataset[0])-1):
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups
    return {'index': b_index, 'value': b_value, 'groups': b_groups}

# Create a terminal node value
def to_terminal(group: List[List[Any]]) -> Any:
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)

# Recursive function to build the decision tree
def split(node: Dict[str, Any], max_depth: int, min_size: int, depth: int):
    left, right = node['groups']
    del(node['groups'])
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left)
        split(node['left'], max_depth, min_size, depth+1)
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right)
        split(node['right'], max_depth, min_size, depth+1)

# Build a decision tree
def build_tree(train: List[List[Any]], max_depth: int, min_size: int) -> Dict[str, Any]:
    root = get_split(train)
    split(root, max_depth, min_size, 1)
    return root

# Make a prediction with a decision tree
def predict_tree(node: Dict[str, Any], row: List[Any]) -> Any:
    if row[node['index']] < node['value']:
        if isinstance(node['left'], dict):
            return predict_tree(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict_tree(node['right'], row)
        else:
            return node['right']

# Bootstrap sampling
def bootstrap_sample(dataset: List[List[Any]]) -> List[List[Any]]:
    n_samples = len(dataset)
    return [random.choice(dataset) for _ in range(n_samples)]

# Select the best split point for a dataset with a random subset of features
def get_split_with_features(dataset: List[List[Any]], n_features: int) -> Dict[str, Any]:
    class_values = list(set(row[-1] for row in dataset))
    features = random.sample(range(len(dataset[0])-1), n_features)
    b_index, b_value, b_score, b_groups = 999, 999, 999, None
    for index in features:
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups
    return {'index': b_index, 'value': b_value, 'groups': b_groups}

# Build a decision tree with a random subset of features
def build_tree_with_features(train: List[List[Any]], max_depth: int, min_size: int, n_features: int) -> Dict[str, Any]:
    root = get_split_with_features(train, n_features)
    split(root, max_depth, min_size, 1)
    return root

# Build a random forest
def random_forest(train: List[List[Any]], n_trees: int, max_depth: int, min_size: int, n_features: int) -> List[Dict[str, Any]]:
    trees = []
    for _ in range(n_trees):
        sample = bootstrap_sample(train)
        tree = build_tree_with_features(sample, max_depth, min_size, n_features)
        trees.append(tree)
    return trees

# Make a prediction with a random forest
def predict(forest: List[Dict[str, Any]], row: List[Any]) -> Any:
    predictions = [predict_tree(tree, row) for tree in forest]
    return max(set(predictions), key=predictions.count)

# Test the decision tree algorithm
def main():
    # Example dataset
    dataset = [
        [2.771244718, 1.784783929, 0],
        [1.728571309, 1.169761413, 0],
        [3.678319846, 2.81281357, 0],
        [3.961043357, 2.61995032, 0],
        [2.999208922, 2.209014212, 0],
        [7.497545867, 3.162953546, 1],
        [9.00220326, 3.339047188, 1],
        [7.444542326, 0.476683375, 1],
        [10.12493903, 3.234550982, 1],
        [6.642287351, 3.319983761, 1]
    ]
    
    # Train Random Forest
    n_trees = 5
    max_depth = 3
    min_size = 1
    n_features = int(np.sqrt(len(dataset[0]) - 1))  # Number of features to consider at each split
    forest = random_forest(dataset, n_trees, max_depth, min_size, n_features)
    
    # Predict
    for row in dataset:
        prediction = predict(forest, row)
        print(f'Expected={row[-1]}, Predicted={prediction}')

if __name__ == '__main__':
    main()
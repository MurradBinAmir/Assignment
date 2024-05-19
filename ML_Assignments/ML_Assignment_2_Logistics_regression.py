import numpy as np

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Cost function
def compute_cost(X, y, theta):
    m = len(y)
    h = sigmoid(X.dot(theta))
    epsilon = 1e-5  # To avoid log(0)
    cost = -(1/m) * (y.T.dot(np.log(h + epsilon)) + (1 - y).T.dot(np.log(1 - h + epsilon)))
    return cost

# Gradient descent function
def gradient_descent(X, y, theta, learning_rate, num_iterations):
    m = len(y)
    for _ in range(num_iterations):
        h = sigmoid(X.dot(theta))
        gradient = (1/m) * X.T.dot(h - y)
        theta -= learning_rate * gradient
    return theta

# Logistic regression function
def logistic_regression(X, y, learning_rate=0.01, num_iterations=10000):
    # Add intercept term to X
    X = np.insert(X, 0, 1, axis=1)
    
    # Initialize parameters
    theta = np.zeros(X.shape[1])
    
    # Perform gradient descent
    theta = gradient_descent(X, y, theta, learning_rate, num_iterations)
    
    return theta

# Prediction function
def predict(X, theta, threshold=0.5):
    X = np.insert(X, 0, 1, axis=1)
    probabilities = sigmoid(X.dot(theta))
    return [1 if p >= threshold else 0 for p in probabilities]

# Example usage
if __name__ == "__main__":
    # Example data: 4 samples, 1 feature
    X = np.array([[0.5], [1.5], [1.0], [2.0]])
    y = np.array([0, 1, 0, 1])

    # Training logistic regression model
    theta = logistic_regression(X, y)

    # Making predictions
    predictions = predict(X, theta)

    print(f"Learned parameters: {theta}")
    print(f"Predictions on training data: {predictions}")
    print(f"Actual labels: {y}")

# Linear Regression from Scratch

# Function to calculate the mean of a list of numbers
def mean(values):
    return sum(values) / float(len(values))

# Function to calculate the variance of a list of numbers
def variance(values, mean_value):
    return sum([(x - mean_value) ** 2 for x in values])

# Function to calculate the covariance between two lists of numbers
def covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar

# Function to calculate the coefficients (b0 and b1) for linear regression
def coefficients(x, y):
    x_mean, y_mean = mean(x), mean(y)
    b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
    b0 = y_mean - b1 * x_mean
    return b0, b1

# Function to make predictions using the linear regression model
def simple_linear_regression(x, b0, b1):
    return [b0 + b1 * xi for xi in x]

# Main function to demonstrate linear regression
def main():
    # Example data
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]

    # Calculate coefficients
    b0, b1 = coefficients(x, y)
    print(f"Coefficients: b0 = {b0}, b1 = {b1}")

    # Make predictions
    predictions = simple_linear_regression(x, b0, b1)
    print(f"Predictions: {predictions}")

if __name__ == "__main__":
    main()

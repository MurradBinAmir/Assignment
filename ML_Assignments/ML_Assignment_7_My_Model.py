import numpy as np

# Random formulas
def formula1(x):
    return 2 * x + 3

def formula2(x):
    return 0.5 * x ** 2 - x + 4

def formula3(x):
    return np.sin(x) * 10 + 5

def formula4(x):
    return np.log(x + 1) * 20 - 10

def formula5(x):
    return (x ** 3) / 100 - (x ** 2) / 10 + x + 1

def generate_predictions(x):

    pred1 = formula1(x)
    pred2 = formula2(x)
    pred3 = formula3(x)
    pred4 = formula4(x)
    pred5 = formula5(x)

    return pred1 * pred2 * pred3 * pred4 * pred5

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for xi in x:
    prediction = generate_predictions(xi)
    print("Element:", xi, "Prediction:", prediction)
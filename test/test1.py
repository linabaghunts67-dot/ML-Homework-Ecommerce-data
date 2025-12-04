"""
Example usage of the custom 1D linear regression function.
Run this file to quickly test the regression on a tiny dataset.
"""

import numpy as np
from ml_homework_ecommerce_data import fit_1d_linear_regression

x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11]) 

b0, b1 = fit_1d_linear_regression(x, y)

print("Custom Regression Test")
print("Expected intercept: 1")
print("Expected slope: 2")
print("Calculated intercept:", b0)
print("Calculated slope:", b1)

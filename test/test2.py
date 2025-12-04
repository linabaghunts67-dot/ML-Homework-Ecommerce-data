"""
Example usage of the plot_fitted_line function.
This script will generate a scatter plot and save a PNG file.
"""

import numpy as np
from ml_homework_ecommerce_data import fit_1d_linear_regression, plot_fitted_line

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

b0, b1 = fit_1d_linear_regression(x, y)

print("Plot Example Test")
print("Intercept:", b0)
print("Slope:", b1)

plot_fitted_line(b0, b1, x, y, username="example_output")

print("Plot saved as example_output.png")

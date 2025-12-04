# ML-Homework-Ecommerce-data

📘 Linear Regression on E-Commerce Customer Data

A simple ML analysis using both custom and sklearn regression

This project explores a real-world style e-commerce dataset and builds a one-dimensional linear regression model to predict Yearly Amount Spent by customers based on their Length of Membership.

The goal of the assignment was to:

clean and prepare the dataset

select only numerical features

visualize relationships between features and the target

implement a custom linear regression function from scratch

compare it with sklearn’s LinearRegression

compute regression metrics (MAE, MSE, RMSE, R²)

plot the fitted line and save the output

Everything is done in a clear, step-by-step approach.

🔍 Project Steps
1️⃣ Data Cleaning

The dataset originally contained 8 columns, including non-numerical identifiers such as:

Email

Address

Avatar

These were removed because they are not useful for regression and contain too many unique values to encode.

The final dataset used for modeling includes:

Avg Session Length

Time on App

Time on Website

Length of Membership

Yearly Amount Spent (target)

2️⃣ Feature Selection

Scatterplots were created to examine linear relationships with the target.
The strongest linear relationship was found between:

➡️ Length of Membership
and
➡️ Yearly Amount Spent

So we kept only this one feature for the 1D linear regression task.

3️⃣ Custom Linear Regression

I implemented my own function:

fit_1d_linear_regression(x, y)


It calculates:

β₁ (slope)

β₀ (intercept)

using the analytical closed-form formulas based on means and covariances.

A second function,

plot_fitted_line(b0, b1, x, y, username)


creates a scatterplot + regression line and saves it as an image file.

4️⃣ Sklearn Regression Comparison

A standard LinearRegression model was fit using sklearn.
Both models produced almost identical coefficients — the differences were only floating-point rounding.

This confirms that the custom implementation is correct.

5️⃣ Model Evaluation

Using sklearn.metrics, the following were computed:

MAE — Mean Absolute Error

MSE — Mean Squared Error

RMSE — Root Mean Squared Error

R² Score

Both the custom model and sklearn model achieved the same results.

The R² score shows that Length of Membership alone explains most of the variance in yearly spending, making it a strong predictor for this dataset.

📈 Results Summary

Strong positive linear correlation between membership length and yearly spending

Custom regression matches sklearn’s implementation

Errors are low and R² is high for a single-feature model

Regression line fits the data well

This demonstrates that even a simple one-feature model can provide solid predictions when the relationship is truly linear.

🛠️ Technologies Used

Python

NumPy

Pandas

Matplotlib / Seaborn

scikit-learn

📎 Files in This Repository

Notebook / script with full analysis

Custom regression implementation

Plots generated during the project

README.md (this file)

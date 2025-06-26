# Task 3: House Price Prediction using Linear Regression

This task involves implementing linear regression using Python and scikit-learn to predict house prices based on features such as area, number of bedrooms, and bathrooms.

---

## Objective

- Understand and apply simple and multiple linear regression
- Train and test a model using scikit-learn
- Visualize the regression line
- Evaluate model performance using metrics like MAE, MSE, and R²

---

## Dataset

The dataset contains house prices with the following features:

- `area`: Size of the house in square feet
- `bedrooms`: Number of bedrooms
- `bathrooms`: Number of bathrooms
- `price`: Target variable (house price)

---

## Steps Performed

### 1. Data Loading and Exploration
- Loaded the dataset using Pandas
- Checked structure, column types, and missing values
- Performed basic descriptive statistics

### 2. Feature Selection
- For simple regression: used `area` as the only input
- For multiple regression: used `area`, `bedrooms`, and `bathrooms` as features

### 3. Model Building
- Used `LinearRegression` from scikit-learn
- Split data into training and testing sets using `train_test_split`
- Trained the model on training data

### 4. Evaluation
- Predicted prices on test data
- Calculated Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² score
- Interpreted model coefficients

### 5. Visualization (for simple regression)
- Plotted actual vs predicted prices using matplotlib
- Created a line plot showing the regression line over the data points

---

## Output

- Trained linear regression model
- Evaluation scores:
  - MAE
  - MSE
  - R² Score
- Plot showing predicted vs actual prices

---

## Files Included

- `task3.ipynb`: Jupyter notebook with full code and output
- `README.md`: This file

---

## How to Run

1. Clone the repository
2. Navigate to the `Task3/` folder
3. Open `task3.ipynb` in Jupyter Notebook or VS Code
4. Run the notebook cells step-by-step

---

## Notes

This task was completed as part of the Elevate Labs AI & ML Internship.  
The goal was to gain hands-on experience with regression algorithms and model evaluation using real-world data.

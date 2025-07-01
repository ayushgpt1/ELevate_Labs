# Task 5: Decision Tree and Random Forest Classification

This task involves building and evaluating two popular classification models: **Decision Tree** and **Random Forest**. The goal is to predict the target variable based on input features and understand how these models work, perform, and visualize their decision-making process.

---

## Objective

- Train and evaluate a Decision Tree classifier
- Train and evaluate a Random Forest classifier
- Visualize tree structure and feature importance
- Use confusion matrix and cross-validation for performance checking

---

## Dataset

The dataset used for this task is a health-related binary classification dataset (e.g., Heart Disease Dataset), containing medical features like:

- age
- cholesterol
- blood pressure
- ...etc.

**Target column:** `target`  
- `1` → Patient has heart disease  
- `0` → Patient does not have heart disease

---

## Steps Performed

### 1. Data Loading and Preparation
- Loaded the CSV data using pandas
- Checked for null values
- Split into features (`X`) and label (`y`)

### 2. Train-Test Split
- 80% data for training, 20% for testing
- Used `train_test_split` from scikit-learn

### 3. Decision Tree Model
- Trained using `DecisionTreeClassifier`
- Limited max depth to control overfitting
- Plotted tree structure using `plot_tree`
- Evaluated using confusion matrix and classification report

### 4. Random Forest Model
- Used `RandomForestClassifier` with 100 trees
- Measured accuracy and confusion matrix
- Plotted **feature importance** to see which inputs matter most
- Performed **5-fold cross-validation**

---

## Results

- Both models provided high accuracy on test data
- Random Forest outperformed the Decision Tree slightly due to better generalization
- Feature importance revealed the most influential predictors
- Visualization helped understand the internal logic of the tree model

---

## Visualizations

- 📊 Decision Tree structure
- 📉 Feature Importance bar chart
- 📌 Confusion Matrices
- ✅ Classification reports (Precision, Recall, F1-score)

---

## Files Included

| File Name                                | Description                            |
|-----------------------------------------|----------------------------------------|
| `task5_decision_tree_random_forest.ipynb` | Jupyter notebook with all code         |
| `heart_disease.csv`                     | Input dataset                          |
| `README.md`                             | This file                              |
| `tree_visualization.png` (optional)     | Saved image of the decision tree plot  |

---

## How to Run

1. Clone the repository
2. Navigate to the `Task5/` directory
3. Open the notebook using Jupyter or VS Code
4. Run all cells step-by-step to train and evaluate the models

---

## Notes

This task was completed as part of the Elevate Labs AI/ML Internship.  
It demonstrates the power of decision trees and ensemble methods like random forests in solving real-world classification problems.

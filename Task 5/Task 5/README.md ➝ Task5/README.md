# Task 5: Decision Tree and Random Forest Classification

This task explores the use of **Decision Tree** and **Random Forest** algorithms for binary classification problems. The goal is to train models, evaluate their performance, and interpret how they make decisions.

---

## Objective

- Train and test a Decision Tree model
- Build a Random Forest model for better generalization
- Visualize model structure and interpret feature importance
- Evaluate performance using metrics like accuracy and confusion matrix

---

## Dataset

The dataset includes health-related features used to predict a binary outcome (e.g., presence or absence of heart disease).

- **Input features:** age, cholesterol, blood pressure, etc.
- **Target column:** `target`  
  - `1` = condition present  
  - `0` = condition absent

---

## Implementation Steps

### 1. Load and Prepare Data
- Read dataset using pandas
- Split into `X` (features) and `y` (target)

### 2. Train-Test Split
- Split data into 80% training and 20% testing

### 3. Decision Tree Classifier
- Trained with limited depth to reduce overfitting
- Visualized using `plot_tree`
- Evaluated using accuracy and confusion matrix

### 4. Random Forest Classifier
- Built using multiple decision trees (100 estimators)
- More robust than a single decision tree
- Extracted feature importances
- Used 5-fold cross-validation to validate model performance

---

## Evaluation Metrics

- **Accuracy Score**
- **Confusion Matrix**
- **Classification Report** (Precision, Recall, F1-score)
- **Feature Importance Chart**

---

## Output Summary

- Decision tree structure visualized
- Random forest showed slightly better accuracy
- Important features identified and ranked
- Cross-validation confirmed model consistency

---

## Files

| File Name                                | Description                            |
|-----------------------------------------|----------------------------------------|
| `Task5.ipynb`                           | Main notebook with full implementation |
| `heart_disease.csv`                     | Dataset used                           |
| `README.md`                             | This documentation file                |

---

## How to Run

1. Open the notebook in Jupyter or VS Code
2. Run all cells to train and evaluate both models
3. View visualizations for tree structure and feature importance

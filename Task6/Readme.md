# Task 6: K-Nearest Neighbors (KNN) Classification

This task demonstrates the implementation and evaluation of the **K-Nearest Neighbors (KNN)** algorithm for binary classification using the Social Network Ads dataset.

---

## Objective

- Train a KNN classifier on real-world user data
- Normalize features to ensure fair distance calculation
- Evaluate model accuracy and performance
- Analyze the effect of different values of K
- Visualize decision boundaries for better understanding

---

## Dataset

**Social_Network_Ads.csv**

| Column           | Description                  |
|------------------|------------------------------|
| Age              | Age of the user              |
| EstimatedSalary  | Annual salary in USD         |
| Purchased        | Target (0 = No, 1 = Yes)     |

---

## Steps Performed

### 1. Load Dataset
- Imported CSV using pandas
- Selected `Age` and `EstimatedSalary` as features (`X`)
- Used `Purchased` as the target variable (`y`)

### 2. Normalize Features
- Applied `StandardScaler` to scale inputs
- Necessary because KNN is a distance-based algorithm

### 3. Train-Test Split
- 75% training, 25% testing using `train_test_split`

### 4. Train KNN Model
- Used `KNeighborsClassifier` from `sklearn`
- Initially trained with K = 5

### 5. Model Evaluation
- Measured **accuracy**, **classification report**, and **confusion matrix**
- Used heatmaps for better visual understanding

### 6. Tune K Parameter
- Tested values of K from 1 to 20
- Plotted accuracy vs K to find the optimal value

### 7. Visualize Decision Boundary
- Used matplotlib to plot KNN classification regions
- Helped understand how the algorithm divides the feature space

---

## Results

- KNN achieved high accuracy after proper scaling
- Best K value was determined using validation curve
- Decision boundary clearly separated the two classes in 2D

---

## Output Highlights

- Accuracy score and classification report
- Confusion matrix heatmap
- K vs Accuracy plot
- Decision boundary visualization

---

## Files

| File Name                     | Description                             |
|------------------------------|-----------------------------------------|
| `task6.ipynb`                | Full Jupyter Notebook implementation |
| `Social_Network_Ads.csv`     | Dataset used for binary classification  |
| `README.md`                  | This documentation file                 |

---

## How to Run

1. Open `task6_knn_classification.ipynb` in Jupyter or VS Code
2. Ensure the CSV is in the same folder
3. Run all cells sequentially to train and evaluate the model

---

## Summary

KNN is a simple yet powerful algorithm when used correctly with normalization and proper K tuning. This task provided hands-on experience with model selection, evaluation, and visualization.


# Task 4: Binary Classification using Logistic Regression

This task focuses on building a binary classification model using logistic regression. The dataset used is the Breast Cancer Wisconsin dataset, which helps identify whether a tumor is malignant or benign based on medical measurements.

---

## Objective

- Load and prepare a binary classification dataset
- Apply train-test split and standardization
- Train a logistic regression model
- Evaluate using confusion matrix, precision, recall, and ROC-AUC
- Visualize results and understand sigmoid function
- Tune classification threshold for performance control

---

## Dataset

**Source:** Breast Cancer Wisconsin (Diagnostic) Dataset  
**Target Variable:** `diagnosis`  
- `M` = Malignant (1)  
- `B` = Benign (0)

**Features:**  
Measurements of tumor size, texture, perimeter, area, smoothness, etc.

---

## Workflow

### 1. Load and Clean Data
- Removed unnecessary columns (`id`, `Unnamed: 32`)
- Mapped target values to binary: `M → 1`, `B → 0`

### 2. Feature Scaling
- Performed standardization using `StandardScaler`
- This ensures faster and more stable convergence

### 3. Model Training
- Used `LogisticRegression()` from `sklearn`
- Trained the model on 80% of the data

### 4. Evaluation
- Generated predictions and evaluated using:
  - **Confusion Matrix**
  - **Precision, Recall, F1-score**
  - **ROC-AUC Score** (0.997)
- Plotted **ROC Curve** to visualize model performance

### 5. Sigmoid & Threshold Tuning
- Logistic regression uses the **sigmoid function** to produce probabilities between 0 and 1
- Adjusted classification threshold using:
  ```python
  y_custom = (y_prob >= 0.3).astype(int)

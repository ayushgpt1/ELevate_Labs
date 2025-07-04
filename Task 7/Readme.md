# Task 8: K-Means Clustering

This task implements K-Means clustering on customer data to group individuals based on their spending patterns. The goal is to identify distinct customer segments that can help with targeted marketing or business insights.

---

## Objective

- Apply K-Means clustering to identify customer groups
- Normalize and preprocess data for better results
- Use the **Elbow Method** to find the optimal number of clusters
- Evaluate using **Silhouette Score**
- Visualize clusters using 2D plots

---

## Dataset

**Mall_Customers.csv**

| Column Name             | Description                            |
|-------------------------|----------------------------------------|
| CustomerID              | Unique ID for each customer            |
| Gender                  | Male or Female                         |
| Age                     | Age of the customer                    |
| Annual Income (k$)      | Annual income in thousands             |
| Spending Score (1-100)  | Score assigned by the mall based on spending behavior and income |

---

## Implementation Steps

### 1. Load and Preprocess the Data
- Dropped `CustomerID` column
- Optionally encoded `Gender` column
- Standardized features using `StandardScaler`

### 2. Apply K-Means Clustering
- Used scikit-learn's `KMeans` to fit the model
- Predicted cluster labels and added to the original DataFrame

### 3. Determine Optimal Clusters
- Used the **Elbow Method** to visualize inertia vs. number of clusters
- Selected `K = 5` based on the "elbow" point

### 4. Evaluate the Model
- Used **Silhouette Score** to assess the clustering quality

### 5. Visualize the Results
- 2D scatter plot of clusters using `Annual Income` and `Spending Score`
- Color-coded customer segments

---

## Results

- **Optimal Clusters:** 5  
- **Silhouette Score:** ~0.55 (may vary slightly)  
- Customers were grouped into distinct segments based on their spending behavior.

---

## Files

| File                          | Description                                 |
|-------------------------------|---------------------------------------------|
| `task8_kmeans_clustering.ipynb` | Jupyter Notebook implementation             |
| `Mall_Customers.csv`          | Dataset used for clustering                 |
| `README.md`                   | Project summary and documentation           |


---

## How to Run

1. Make sure the dataset is present in the working directory.
2. Open the notebook using Jupyter or VS Code.
3. Run all cells in order to preprocess, cluster, evaluate, and visualize the data.

---

## Summary

K-Means is an effective unsupervised learning technique for segmenting customers. By combining feature scaling, elbow method, and silhouette score, we can build and evaluate reliable customer segmentation models.

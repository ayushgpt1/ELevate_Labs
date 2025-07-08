# Task 2: Exploratory Data Analysis (EDA) - Iris Dataset

This task focuses on exploring the Iris dataset using statistical summaries and visualizations. The goal is to understand how different features relate to each other and how they differ between the three iris species.

## Objective

- Generate summary statistics
- Visualize feature distributions and relationships
- Detect patterns, correlations, or anomalies
- Draw basic conclusions from the data

## Dataset

The Iris dataset contains 150 records with the following features:

- `sepal_length`
- `sepal_width`
- `petal_length`
- `petal_width`
- `species` (target variable)

Each species (*setosa*, *versicolor*, *virginica*) has 50 samples.  
Source: [Seaborn Iris Dataset](https://github.com/mwaskom/seaborn-data/blob/master/iris.csv)

## Steps Performed

1. **Data Loading**
   - Loaded dataset using Pandas
   - Checked for null values and structure

2. **Descriptive Statistics**
   - Used `.describe()` to get mean, median, and std
   - Observed balanced class distribution

3. **Visualization**
   - Histograms for feature distributions
   - Boxplots for outlier detection
   - Heatmap for correlation between features
   - Pairplot to observe class separation visually

4. **Skewness Analysis**
   - Checked skewness to understand distribution symmetry

5. **Insights**
   - Petal dimensions are highly correlated
   - Setosa is clearly separated from other species
   - Minor outliers in sepal width
   - No missing values and well-structured dataset

## Files

- `task2.ipynb`: Notebook containing all steps and visualizations
- `README.md`: This file

## How to Run

1. Clone the repository
2. Navigate to `Task2/` directory
3. Open the notebook (`task2.ipynb`) in Jupyter or VS Code
4. Run cells sequentially to reproduce results

## Notes

This task was submitted as part of the AI & ML Internship under Elevate Labs.  
The Iris dataset was chosen for its simplicity and suitability for practicing core EDA concepts.


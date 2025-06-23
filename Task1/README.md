Task 1: Data Cleaning and Preprocessing

This task involves preparing the Titanic dataset for machine learning by performing data cleaning and preprocessing steps. The objective is to ensure the dataset is structured, consistent, and suitable for input into a machine learning model.

Objective

- Identify and handle missing values
- Encode categorical variables
- Scale numerical features
- Visualize and remove outliers

 Dataset

The dataset used is the Titanic dataset, which contains information about passengers, such as age, class, fare, and whether they survived. It is available on Kaggle.

Steps Performed

1. Data Exploration
- Loaded the dataset using Pandas
- Reviewed the structure, data types, and summary statistics
- Identified columns with missing values

 2. Handling Missing Values
- Filled missing values in the `Age` column using the median
- Replaced missing values in the `Embarked` column using the mode
- Dropped the `Cabin` column due to a high percentage of missing data

 3. Encoding Categorical Variables
- Converted the `Sex` column to numerical using label encoding
- Applied one-hot encoding to the `Embarked` column

 4. Feature Scaling
- Scaled `Age` and `Fare` using both standardization and normalization techniques
- Used `StandardScaler` and `MinMaxScaler` from scikit-learn

 5. Outlier Detection and Removal
- Visualized the `Age` and `Fare` columns using boxplots
- Identified and removed outliers using the Z-score method

Output

The final cleaned dataset is saved as `cleaned_titanic.csv`. It contains no missing values, all features are numeric, and the data is ready for use in model training.

Files Included

- `task1.ipynb`: Jupyter notebook with step-by-step implementation
- `titanic.csv`: Original dataset
- `cleaned_titanic.csv`: Dataset after preprocessing
- `README.md`: This file

How to Run

1. Clone the repository
2. Open the `task1.ipynb` notebook in Jupyter or VS Code
3. Run the cells in order to reproduce the results

Notes

This task was completed as part of a learning internship. All steps were implemented using Python and widely used data science libraries such as Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn.

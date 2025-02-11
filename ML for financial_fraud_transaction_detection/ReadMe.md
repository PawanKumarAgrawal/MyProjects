Financial Fraud Detection Analysis

This project involves analyzing a financial transactions dataset to identify patterns indicative of fraudulent activities.

Dataset:
The analysis utilizes the 'Fraud.csv' dataset, which contains records of various transaction types, amounts, and associated features.
Key Steps

    Data Exploration:
        Loaded and examined the dataset structure.
        Checked for missing values and class distribution.

    Data Visualization:
        Analyzed transaction types and their frequencies.
        Visualized the proportion of transaction amounts by type.

    Data Balancing:
        Addressed class imbalance by upsampling the minority class.

    Feature Engineering:
        Processed categorical variables using one-hot encoding.
        Simplified 'nameDest' feature for analysis.

    Correlation Analysis:
        Evaluated feature correlations with the target variable.

    Model Development:
        Implemented a Random Forest Classifier to predict fraudulent transactions.
        Assessed model performance using accuracy, precision, recall, and F1 score.

Results

The Random Forest model demonstrated high performance, indicating its effectiveness in detecting fraudulent transactions within the dataset.
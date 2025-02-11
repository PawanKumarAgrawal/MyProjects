Insurance Claim Prediction using Random Forest

📌 Project Overview

This project focuses on predicting insurance claims using a Random Forest Classifier. The dataset is preprocessed, balanced, and used to train a model to classify claims efficiently.

📊 Workflow

Data Loading & Exploration:

Load training data

Check data types and missing values

Analyze class distribution

Feature Engineering:

Convert categorical variables to numerical using one-hot encoding

Remove unnecessary columns

Handle class imbalance using upsampling

Model Training & Hyperparameter Tuning:

Split data into training and validation sets

Train Random Forest Classifier

Use GridSearchCV for hyperparameter tuning

Model Evaluation:

Evaluate model performance using confusion matrix and F1 score

Predict on test data and generate final results

🛠 Tech Stack

Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn

Model: Random Forest Classifier

📂 Output

The final predictions are saved as result.csv.

📌 Next Steps

Improve feature engineering

Explore additional models (XGBoost, LightGBM)

Optimize hyperparameters further for better performance


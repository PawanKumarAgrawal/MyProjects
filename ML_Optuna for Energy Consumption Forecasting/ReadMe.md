Energy Consumption Forecasting

This project demonstrates a complete pipeline for forecasting energy consumption using time series data. It covers data preprocessing, feature engineering, hyperparameter optimization with Optuna, model training, and visualization.
Project Overview

    Data Preparation:
        Loads energy data from a CSV file.
        Cleans the dataset by handling missing values and outliers.
        Converts the datetime column to a proper datetime format.

    Feature Engineering:
        Extracts date-related features (year, week, cyclic features such as month, day, and hour transformations).

    Modeling & Optimization:
        Splits the data into training and testing sets based on time.
        Tunes various regressors (e.g., RandomForest, GradientBoosting, LightGBM, CatBoost, XGBoost) using Optuna to minimize the Mean Absolute Percentage Error (MAPE).
        Selects and trains the best model.
        Uses SHAP for model interpretation.

    Forecasting & Visualization:
        Generates future predictions.
        Plots actual versus predicted energy consumption aggregated by month.

Installation

    Clone the repository:

git clone https://github.com/yourusername/energy-forecasting.git
cd energy-forecasting

Install the required packages:

    pip install -r requirements.txt

Usage

    Ensure that the dataset (GE_train_data.csv) is available in the appropriate directory.
    Open the Jupyter Notebook included in the repository.
    Run the cells sequentially to process data, optimize models, and generate forecasts and visualizations.

Tech Stack

    Python (Pandas, NumPy, Matplotlib)
    Scikit-learn, XGBoost, LightGBM, CatBoost
    Optuna (for hyperparameter tuning)
    SHAP (for model explainability)

License

This project is open source and available under the MIT License.
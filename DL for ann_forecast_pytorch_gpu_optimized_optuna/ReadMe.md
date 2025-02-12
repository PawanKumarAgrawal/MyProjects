ANN Forecasting with PyTorch, GPU Optimization & Optuna

This project implements an artificial neural network (ANN) for time series forecasting of energy consumption. The model leverages PyTorch with GPU support and uses Optuna for hyperparameter optimization. Originally developed in Google Colab, the notebook processes a dataset (GE_train_data.csv) to predict future energy values and visualizes actual vs. predicted energy consumption.
Features

    Data Preprocessing:
        Handles missing values and interpolates energy data.
        Performs outlier detection and correction using IQR and Z-Score.
        Extracts date-related features for enhanced forecasting.

    Neural Network Model:
        Custom PyTorch model with adjustable hidden layers, dropout, and batch normalization.
        Trained on historical energy data with GPU support when available.

    Hyperparameter Optimization:
        Uses Optuna to optimize model hyperparameters (number of layers, neurons per layer, dropout rate, learning rate, etc.) based on Mean Absolute Percentage Error (MAPE).

    Visualization:
        Generates a comparative plot of actual vs. predicted monthly energy consumption with relevant statistics.

Setup

    Install Dependencies:

    Ensure you have Python 3.x installed. Then, install the required packages:

    pip install -r requirements.txt

    Run the Notebook:

    Open the ann_forecast_pytorch_gpu_optimized_optuna.ipynb notebook in Google Colab or your local environment to execute the code.

Usage

    Data Input:
    The script reads from GE_train_data.csv (ensure the file is accessible in your environment).

    Model Training:
    The notebook performs preprocessing, splits the dataset, and trains the model while tuning hyperparameters with Optuna.

    Evaluation & Prediction:
    It evaluates the model using MAPE and plots actual versus predicted energy consumption aggregated by month.

Requirements

    Python 3.x
    PyTorch
    Optuna
    pandas, numpy
    scikit-learn
    matplotlib
    Additional libraries as specified in requirements.txt

License

This project is licensed under the MIT License.

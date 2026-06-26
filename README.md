# IoT-Based Predictive Maintenance Using LightGBM

## Project Overview

This project aims to predict machine failures using machine learning by combining sensor data with IoT maintenance information. The objective is to identify potential failures before they occur, enabling proactive maintenance and reducing downtime.

---

## Objectives

* Predict machine failures using machine learning.
* Improve predictive performance by integrating IoT maintenance features.
* Handle class imbalance using SMOTE.
* Build an accurate and explainable LightGBM model.

---

## Datasets

### AI4I 2020 Predictive Maintenance Dataset

Contains machine sensor readings and failure information.

### IoT Maintenance Dataset

Contains maintenance-related features such as:

* Machine Age
* Operating Hours
* Days Since Last Maintenance
* Maintenance Count
* Energy Consumption
* Vibration Level
* Humidity
* Ambient Dust Level
* Maintenance Cost

---

## Project Workflow

* Data Collection
* Data Understanding
* Exploratory Data Analysis (EDA)
* Dataset Integration
* Data Preprocessing
* Class Balancing using SMOTE
* LightGBM Model Training
* Model Evaluation
* Feature Importance Analysis
* Hyperparameter Tuning *(In Progress)*
* SHAP Explainability *(Planned)*

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* LightGBM
* Imbalanced-learn (SMOTE)

---

## Current Results

| Metric    | Value |
| --------- | ----: |
| Accuracy  | 98.5% |
| Precision |  0.89 |
| Recall    |  0.97 |
| F1-score  |  0.93 |

---

## Important Features

The LightGBM model identifies the following features as the most influential:

* Vibration Level
* Tool Wear
* Torque
* Rotational Speed
* Operating Hours

---

## Future Enhancements

* Hyperparameter Tuning
* SHAP Explainability
* Feature Engineering
* Flask Deployment
* Final Testing and Documentation

---

## Author

**Raees**

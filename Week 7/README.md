# Week 7 Assignment – Streamlit Deployment of Titanic Survival Prediction

---

## Overview
This assignment focuses on deploying a machine learning model using Streamlit. The task was to build an interactive web app that predicts whether a Titanic passenger would survive based on their input features. 

---

## Objectives
- Build classification models to predict survival using the Titanic dataset.
- Perform one-hot encoding, scaling, and preprocessing using a pipeline.
- Optimize models using `GridSearchCV`.
- Save the best models and preprocessing pipeline using `joblib`.
- Deploy an interactive app with Streamlit to take user input and display predictions and visual insights.

---

## Features of the Web App
- **Model Selection:** Choose between Random Forest and Gradient Boosting models.
- **User Input Form:** Input fields for Age, Sex, Fare, Pclass, Embarked location, and family members onboard.
- **Prediction Output:** Shows whether the passenger is likely to survive along with a probability chart.
- **Interpretation & Summary:** View input breakdown and summary statistics of the dataset.

---

## Files
- `assignment_week7.ipynb`: Jupyter Notebook containing the entire workflow — data loading, preprocessing, model training, tuning, and export.
- `app.py`: Streamlit script for deploying the trained models as a web app.
- `random_forest_model.pkl` and `gradient_boost_model.pkl`: Tuned model files.
- `preprocessor.pkl`: Serialized preprocessing pipeline used during prediction.
- `titanic/train.csv`: Cleaned Titanic dataset used in the app.

---

## How to Run the App
1. Install required packages:
    ```bash
    pip install streamlit pandas scikit-learn altair
    ```

2. Run the app:
    ```bash
    streamlit run app.py
    ```

3. Interact with the UI in your browser.

---

## Conclusion
This assignment demonstrated the complete cycle of building, optimizing, and deploying a machine learning model in a real-world application. It emphasizes not only modeling skills but also practical deployment using modern Python tools.


---
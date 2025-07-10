import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# ------------------ Page Config ------------------ #
st.set_page_config(page_title="Student Exam Score Predictor", layout="wide")
st.title("📚 Student Final Grade Prediction App")

st.markdown("""
<style>
.sidebar .sidebar-content {
    background-color: #f0f2f6;
}
.stButton > button {
    background-color: #4CAF50;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ------------------ Load Models ------------------ #
model_dict = {
    "Linear Regression": joblib.load("linear_regression_model.pkl"),
    "Ridge Regression": joblib.load("ridge_regression_model.pkl"),
    "Random Forest": joblib.load("random_forest_model.pkl"),
    "Gradient Boosting": joblib.load("gradient_boosting_model.pkl"),
    "XGBoost": joblib.load("xgboost_model.pkl")
}

preprocessor = joblib.load("preprocessor.pkl")

# ------------------ Sidebar Inputs ------------------ #
st.sidebar.header("🧾 Enter Student Information")

pclass = st.sidebar.selectbox("School", ["GP", "MS"])
sex = st.sidebar.radio("Sex", ["F", "M"])
age = st.sidebar.slider("Age", 15, 22, 17)
address = st.sidebar.radio("Address", ["U", "R"])
famsize = st.sidebar.radio("Family Size", ["LE3", "GT3"])
Pstatus = st.sidebar.radio("Parent Status", ["T", "A"])
Medu = st.sidebar.selectbox("Mother's Education", [0, 1, 2, 3, 4])
Fedu = st.sidebar.selectbox("Father's Education", [0, 1, 2, 3, 4])
Mjob = st.sidebar.selectbox("Mother's Job", ["teacher", "health", "services", "at_home", "other"])
Fjob = st.sidebar.selectbox("Father's Job", ["teacher", "health", "services", "at_home", "other"])
reason = st.sidebar.selectbox("School Choice Reason", ["home", "reputation", "course", "other"])
guardian = st.sidebar.selectbox("Guardian", ["mother", "father", "other"])
traveltime = st.sidebar.slider("Travel Time (1-4)", 1, 4, 1)
studytime = st.sidebar.slider("Weekly Study Time (1-4)", 1, 4, 2)
failures = st.sidebar.slider("Past Class Failures", 0, 4, 0)
schoolsup = st.sidebar.radio("Extra School Support", ["yes", "no"])
famsup = st.sidebar.radio("Family Educational Support", ["yes", "no"])
paid = st.sidebar.radio("Extra Paid Classes", ["yes", "no"])
activities = st.sidebar.radio("Extracurricular Activities", ["yes", "no"])
nursery = st.sidebar.radio("Attended Nursery", ["yes", "no"])
higher = st.sidebar.radio("Wants Higher Education", ["yes", "no"])
internet = st.sidebar.radio("Internet Access", ["yes", "no"])
romantic = st.sidebar.radio("In a Romantic Relationship", ["yes", "no"])
famrel = st.sidebar.slider("Family Relationship Quality", 1, 5, 4)
freetime = st.sidebar.slider("Free Time After School", 1, 5, 3)
goout = st.sidebar.slider("Going Out with Friends", 1, 5, 3)
Dalc = st.sidebar.slider("Workday Alcohol Consumption", 1, 5, 1)
Walc = st.sidebar.slider("Weekend Alcohol Consumption", 1, 5, 2)
health = st.sidebar.slider("Current Health Status", 1, 5, 5)
absences = st.sidebar.slider("School Absences", 0, 30, 4)
G1 = st.sidebar.slider("First Period Grade (G1)", 0, 20, 12)
G2 = st.sidebar.slider("Second Period Grade (G2)", 0, 20, 13)

# ------------------ Construct Input ------------------ #
user_input = pd.DataFrame([{
    'school': pclass, 'sex': sex, 'age': age, 'address': address, 'famsize': famsize,
    'Pstatus': Pstatus, 'Medu': Medu, 'Fedu': Fedu, 'Mjob': Mjob, 'Fjob': Fjob,
    'reason': reason, 'guardian': guardian, 'traveltime': traveltime, 'studytime': studytime,
    'failures': failures, 'schoolsup': schoolsup, 'famsup': famsup, 'paid': paid,
    'activities': activities, 'nursery': nursery, 'higher': higher, 'internet': internet,
    'romantic': romantic, 'famrel': famrel, 'freetime': freetime, 'goout': goout,
    'Dalc': Dalc, 'Walc': Walc, 'health': health, 'absences': absences, 'G1': G1, 'G2': G2
}])

# ------------------ Model Selection ------------------ #
st.sidebar.subheader("🔍 Choose a Model")
selected_model_name = st.sidebar.selectbox("Select a trained model", list(model_dict.keys()))
selected_model = model_dict[selected_model_name]

# ------------------ Prediction ------------------ #
if st.sidebar.button("Predict Final Grade"):
    try:
        X_transformed = preprocessor.transform(user_input)
        prediction = selected_model.predict(X_transformed)[0]
        st.success(f"🎓 Predicted Final Grade (G3): **{round(prediction, 2)} / 20**")
        st.markdown("### 👤 Input Summary")
        user_input_display = user_input.T.rename(columns={0: "Value"})
        user_input_display["Value"] = user_input_display["Value"].astype(str)
        st.dataframe(user_input_display.style.set_properties(**{"text-align": "left"}))

    except Exception as e:
        st.error(f"Prediction failed: {e}")

# ------------------ Performance Visualization ------------------ #
st.markdown("### 📈 Model Performance Comparison")

cols = st.columns(3)

with cols[0]:
    st.image("plots/r2_comparison.png", caption="R² Score Comparison")

with cols[1]:
    st.image("plots/actual_predicted_final_grades.png", caption="Actual vs Predicted Final Grades (Gradient Boosting)")

with cols[2]:
    st.image("plots/final_grades_distribution.png", caption="Distribution of Final Grades (G3)")

# ------------------ About Section ------------------ #
with st.expander("📘 About This App"):
    st.markdown("""
    This app uses multiple machine learning regression models to predict a student's final grade based on 
    various features like study time, absences, prior grades, and more. The app supports models like:

    - Linear Regression
    - Ridge Regression
    - Random Forest Regressor
    - Gradient Boosting Regressor
    - XGBoost Regressor

    You can choose a model, input data, and get an instant prediction. Visualizations help compare model performance.
    """)

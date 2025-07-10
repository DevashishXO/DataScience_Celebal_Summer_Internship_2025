# Celebal Technologies CSI'25 (Data Science) Internship

**Author**: [Devashish Nagpal]

## Files
- `assignment_week_1.py`: Contains the code for the first week's assignment.
- `assignment_week_2.py`: Contains the code for the second week's assignment.
- `assignment_week_3.py`: Contains the code for the third week's assignment.
- `assignment_week_4.py`: Contains the code for the fourth week's assignment.
- `assignment_week_5.ipynb`: Jupyter Notebook for Week 5 - Regression Preprocessing, Feature Engineering, and Evaluation.
- `assignment_week_6.ipynb`: Jupyter Notebook for Week 6 - Model Evaluation and Hyperparameter Tuning.

## Assignments

### Week 1 Assignment
- **Task**: Create lower triangular, upper triangular and pyramid containing the "*" character.

### Week 2 Assignment
- **Task**: Implement a singly linked list in Python using OOP, with methods to add, print, and delete nodes, including exception handling.

### Week 3 Assignment
- **Task**: Perform exploratory data analysis and visualization on any dataset using different python plotting libraries to uncover trends, patterns, and insights.

### Week 4 Assignment
- **Task**: Conduct an in-depth Exploratory Data Analysis on a complex dataset. Focus on understanding data distributions, identifying missing values, detecting outliers, and uncovering relationships between variables. Utilize visualizations like histograms, box plots, and heatmaps to support your findings.

### Week 5 Assignment
- **Task**: Perform detailed data preprocessing, feature engineering, and model evaluation on a real-world housing dataset in preparation for advanced regression tasks. 

### Week 6 Assignment
- **Task**: Train multiple classification models on the Heart Disease dataset. Evaluate their performance using Accuracy, Precision, Recall, and F1-Score. Perform hyperparameter tuning using GridSearchCV and RandomizedSearchCV. Visualize and compare results to identify the best-performing model.

### Week 7 Assignment
- **Task**: Deploy a trained machine learning model using **Streamlit**. Develop a web application that allows users to input features, receive predictions, and understand the model output through interactive visualizations. This will help bridge the gap between model building and practical accessibility.



## Project: Student Exam Score Prediction
### Overview
This project aims to predict students' **final exam scores (G3)** based on a rich set of features including academic history, personal background, and lifestyle attributes. The dataset used includes Portuguese secondary school students and was obtained from the UCI Machine Learning Repository.

### Dataset Overview
**Source:** [UCI Machine Learning Repository – Student Performance Data Set](https://archive.ics.uci.edu/ml/datasets/Student+Performance)
We use the `student-mat.csv` file which contains data related to students enrolled in the **Math course**.
### Features (selected from 33 columns)
- **Demographic:** `age`, `sex`, `address`, `famsize`, `Pstatus`
- **Parental Info:** `Medu`, `Fedu`, `Mjob`, `Fjob`
- **Academic:** `G1`, `G2`, `studytime`, `failures`, `schoolsup`, `paid`
- **Lifestyle:** `absences`, `health`, `goout`, `romantic`, `internet`, `Dalc`, `Walc`
- **Target Variable:** 
  - `G3` — Final grade (0–20)

### Objective
To build a **regression model** that accurately predicts a student's final exam score (`G3`) based on available information from the dataset.

---


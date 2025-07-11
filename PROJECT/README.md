# Student Exam Score Prediction (Regression Project)

This project aims to predict students' **final exam scores (G3)** based on a rich set of features including academic history, personal background, and lifestyle attributes. The dataset used includes Portuguese secondary school students and was obtained from the UCI Machine Learning Repository.

---

![Homepage](screenshots/home_page.png)
![Input Form](screenshots/input_form_filled.png)
![Output Prediction](screenshots/prediction_result.png)

## Dataset Overview

**Source:** [UCI Machine Learning Repository – Student Performance Data Set](https://archive.ics.uci.edu/ml/datasets/Student+Performance)

We use the `student-mat.csv` file which contains data related to students enrolled in the **Math course**.

### Features (selected from 33 columns)

- **Demographic:** `age`, `sex`, `address`, `famsize`, `Pstatus`
- **Parental Info:** `Medu`, `Fedu`, `Mjob`, `Fjob`
- **Academic:** `G1`, `G2`, `studytime`, `failures`, `schoolsup`, `paid`
- **Lifestyle:** `absences`, `health`, `goout`, `romantic`, `internet`, `Dalc`, `Walc`

**Target Variable:**  
- `G3` — Final grade (0–20)

---

## Objective

To build a **regression model** that accurately predicts a student's final exam score (`G3`) based on available information from the dataset.

---

## Workflow

1. **Data Loading & Inspection**
   - Explored shape, types, and missing values
2. **Exploratory Data Analysis (EDA)**
   - Visualized distribution of grades and key relationships
3. **Preprocessing**
   - Handled categorical variables using One-Hot Encoding
   - Scaled numeric features
4. **Model Building**
   - Trained three models:
     - Linear Regression
     - Random Forest Regressor
     - Gradient Boosting Regressor
5. **Evaluation**
   - Compared using:
     - Mean Absolute Error (MAE)
     - Mean Squared Error (MSE)
     - R² Score

---

## Results

| Model                | MAE   | MSE   | R² Score |
|---------------------|-------|-------|----------|
| Linear Regression    | 1.65  | 5.66  | 0.7241   |
| Random Forest        | 1.18  | 3.83  | 0.8130   |
| Gradient Boosting    | 1.16  | 4.02  | 0.8040   |

**Random Forest Regressor** provided the best balance between interpretability and performance.

---

## Sample Input-Output Example

```json
Input:
{
  "G1": 13,
  "G2": 14,
  "studytime": 2,
  "failures": 0,
  "absences": 4,
  "sex": "F",
  "school": "GP",
  "paid": "yes",
  "romantic": "no"
}

Predicted Final Grade (G3): 15.2

```

## How to Run the App Locally?

Follow the steps below to run the Streamlit app on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/student-exam-score-prediction.git
cd student-exam-score-prediction
```
Replace `your-username` with your actual GitHub username.

### 2. Install Dependencies
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install required packages
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App
```bash
streamlit run app.py
```

## Author

Linkedin: [Devashish Nagpal](https://www.linkedin.com/in/devashishnagpal/)
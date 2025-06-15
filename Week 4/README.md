# Week 4 – Exploratory Data Analysis on Medical Cost Dataset

This repository contains my submission for Week 4 of the Celebal CSI Data Science Summer Internship 2025. In this assignment, I conducted a detailed Exploratory Data Analysis (EDA) on the popular "Medical Cost Personal Dataset" which includes patient-level data related to age, gender, BMI, children, smoking habits, region, and medical expenses.

---

## Dataset Overview

- **Source**: Kaggle – [Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- **Records**: 1,338 rows
- **Columns**: 7 features including age, sex, BMI, number of children, smoking status, region, and medical charges.

The objective of this dataset is to explore the **key factors influencing individual medical insurance charges** and gain insights into lifestyle-based cost variations.

---

## Tech Stack Used

- **Python 3.10+**
- **Jupyter Notebook / VS Code**
- **Libraries**:
  - `pandas` – Data handling
  - `matplotlib` & `seaborn` – Data visualization
  - `numpy` – Numerical operations

---

## EDA Objectives

1. Understand individual features (univariate analysis)
2. Study relationships between variables (bivariate & multivariate analysis)
3. Detect outliers and interpret medical cost variability
4. Engineer meaningful features (e.g. BMI category, age group)
5. Support insights using clear visualizations

---

## Visualizations Included

- **Distribution plots**: Age, BMI, Charges
- **Boxplots**: Charges vs Smoker, Sex, Region, Children
- **Correlation heatmap**: Relationships between numeric variables
- **Scatterplot**: Age vs Charges colored by smoker, sized by BMI
- **Bar plots**: Charges by Age Group and BMI Category

---

## Key Insights & Learnings

### Analytical Learnings:
- Smoking status has the **strongest impact** on medical costs.
- **Obese individuals** and those with **higher age** generally face greater charges.
- Certain regions (like Southeast) showed slightly higher average costs.
- Categorical breakdowns (age groups, BMI category) improved interpretability.

### Technical Learnings:
- Gained hands-on practice with **EDA flow** — from data inspection and cleaning to feature engineering and visualization.
- Understood the significance of **visual storytelling** to uncover data-driven narratives.
- Reinforced the value of **feature transformation** in improving insight depth (e.g., turning numerical BMI into categorical groups).
- Practiced handling plots, identifying correlation, and interpreting multi-feature interactions.

---

## Reflection

This assignment helped me approach data not just as numbers, but as a reflection of human behavior and systems — in this case, healthcare costs. I saw how even a small dataset, when analyzed correctly, can reveal **meaningful patterns**, expose **economic implications of lifestyle choices**, and offer insights that align with **real-world intuition**. I also sharpened my technical EDA workflow while focusing on drawing conclusions that go beyond the visuals.

---

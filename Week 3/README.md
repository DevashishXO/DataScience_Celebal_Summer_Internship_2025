# Airplane Crash Visualization Project

## Overview

This project involves exploratory data analysis (EDA) and visualization of a historical dataset containing details about airplane crashes from 1908 to the present. The aim was to uncover trends, patterns, and insights from over a century of aviation incidents.

The dataset was obtained from Kaggle and includes crash details such as date, operator, location, number of fatalities, aircraft type, and more. By analyzing this data, we aim to understand how aviation safety has evolved, which operators were most involved in incidents, and which crashes were the deadliest.

---

## Dataset Information

- **Source:** [Airplane Crashes Since 1908 – Kaggle](https://www.kaggle.com/datasets/saurograndi/airplane-crashes-since-1908)
- **Shape:** 5246 rows × 14 columns (after cleaning)
- **Features include:**  
  - Date and time of crash  
  - Operator (airline/military/etc.)  
  - Location  
  - Type of aircraft  
  - Number of people aboard, fatalities, survivors  
  - Summary of the incident  

---

## Objectives

- Perform cleaning and preprocessing on the dataset  
- Handle missing values and engineer new time-based features  
- Visualize crash trends across different dimensions  
- Derive meaningful insights from the data using visual storytelling

---

## Visualizations Used

### 1. Yearly Crash Trends
A line plot showing the number of crashes per year. Revealed a clear peak in the 1970s and a decline after the 1990s, reflecting increased aviation safety.

### 2. Top 10 Deadliest Airplane Crashes
Bar chart displaying the worst crash events in terms of fatalities. Helped highlight rare but catastrophic incidents.

### 3. Heatmap – Crashes by Month and Year
Used a Seaborn heatmap to explore the distribution of crashes by both month and year, revealing yearly patterns but no strong monthly seasonality.

### 4. Operator-wise Crash Count
Bar plot showcasing the top operators (airlines/military forces) with the highest crash counts. Helped understand which entities had the most incidents logged.

### 5. Word Cloud of Crash Locations
A textual visualization of locations where crashes occurred most frequently. Highlighted cities and countries with dense air traffic or historical aviation activity.

---

## Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- WordCloud
- Jupyter Notebook

---

## Key Insights

- Aviation crashes peaked during the 1970s and early 1980s but have declined drastically since.
- Military and early commercial aviation operators appear more frequently in crash records.
- Some crashes involved exceptionally high fatality counts, though they remain outliers.
- Crashes are more dependent on the year (e.g., era-specific safety standards) than the month.
- The dataset provides a rare look into aviation’s historical development from a safety perspective.

---

## Author

Devashish Nagpal  
Data Science Intern, Celebal Technologies Pvt. Ltd. 
Summer Internship 2025  

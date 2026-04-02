# 🌫️ AQI Monitor — AI-Powered Air Quality Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![Machine Learning](https://img.shields.io/badge/ML-Ensemble%20Learning-green?logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

>  An AI-powered Air Quality Index (AQI) prediction system built using advanced machine learning models and deployed through an interactive **Streamlit** web application for real-time environmental analysis.

##  Dataset Used
The model is trained on historical environmental data from India (2015-2024):
**Dataset:** [Air Quality Data in India (Kaggle)](https://www.kaggle.com/datasets/ankushpanday1/air-quality-data-in-india-2015-2024)

---

##  About the Project

**AQI Monitor** is an end-to-end machine learning project designed to predict the Air Quality Index (AQI) using key environmental pollutant data such as **PM2.5, PM10, NO2, SO2, CO, and O₃**.

The project evaluates multiple machine learning models—specifically focusing on **Random Forest Regression** and advanced ensemble techniques—to achieve high prediction accuracy. The final model is deployed in a user-friendly dashboard where users can explore data visually and predict AQI in real-time.

---

##  Features

-  **Multiple ML Models:** Trained and evaluated various regression algorithms.
-  **Interactive Dashboard:** Built with **Streamlit** for a modern, responsive UI.
-  **Real-time Prediction:** Two-column input system for instant AQI results.
-  **Visual Analytics:** Includes histograms, scatter plots, and correlation heatmaps.
-  **Live Logging System:** A dedicated page to monitor model loading and system activity.
-  **Professional Architecture:** Designed with clear DFD and ER diagrams.

---

##  ML Models Used

| # | Model | Type |
|---|-------|------|
| 1 | Linear Regression | Linear |
| 2 | Polynomial Regression | Linear |
| 3 | Decision Tree | Tree-based |
| 4 | **Random Forest** | **Ensemble (Primary)** |
| 5 | Gradient Boosting | Ensemble |
| 6 | **XGBoost** | Boosting |
| 7 | **LightGBM** | Boosting |
| 8 | **Stacking Regressor** | Ensemble |
| 9 | **Voting Regressor** | Final Ensemble Model |

---

## 📊 Model Performance

- **Best Model:** Voting Regressor
- **R² Score:** 0.934
- **RMSE:** 26.78
- **MAE:** 15.97

---

##  Demo

 **Live App:** [AQI Monitor Dashboard](https://aqi-monitor-alenjohn.streamlit.app/)

---

##  Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Core programming |
| **Streamlit** | Web application framework |
| **Scikit-learn** | ML training & Random Forest |
| **XGBoost / LightGBM** | Advanced Boosting Models |
| **Pandas / NumPy** | Data handling & cleaning |
| **Matplotlib / Plotly** | Data visualization |
| **Pickle / Joblib** | Model serialization |

---

##  Project Workflow

| Step | Action | Output |
|------|--------|--------|
| 1 | Data preprocessing & cleaning | Clean Kaggle dataset |
| 2 | System Architecture Design | ER & Data Flow Diagrams |
| 3 | Model Training & Tuning | Optimized Random Forest |
| 4 | UI Development | Streamlit Dashboard |
| 5 | System Integration | Live Logging & Prediction |

---

##  Author

**Alen John**
* College Project — Machine Learning Track
* Focus: System Management & Architecture

---

<p align="center">Made with and Python | Star this repo if you found it useful!</p>

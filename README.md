# Air Quality Index (AQI) Predictor
# Developed by: Alen John

1. PROJECT OVERVIEW

Monitoring air quality is crucial for public health. This project focuses on 
building a robust Machine Learning regression model that interprets complex 
pollutant data (PM2.5, PM10, NO2, SO2, CO, O3) to provide a standardized 
AQI value.

The core of this project is a Voting Regressor ensemble that aggregates the 
strengths of multiple models (including Random Forest and XGBoost) to ensure 
prediction stability and high accuracy.


2. MODEL PERFORMANCE

The final ensemble model was evaluated using standard regression metrics:

* R-Squared (R2) Score: 0.934  (Explains 93.4% of data variance)
* Mean Absolute Error (MAE): 15.97
* Root Mean Squared Error (RMSE): 26.78

These metrics confirm that the "Voting" approach successfully minimizes 
prediction errors compared to individual standalone models.


3. KEY FEATURES

* Interactive UI: Built with Streamlit, allowing users to input pollutant 
  levels via sliders or text boxes for real-time results.
* Ensemble Learning: Uses a Voting Regressor to balance bias and variance.
* Automated Logging: A built-in system records every prediction with a 
  timestamp, log level (INFO/SUCCESS/ERROR), and model details.
* Data Visualization: Integrated gauges and charts within the dashboard 
  to visualize the predicted AQI level.


4. TECH STACK

* Language: Python 3.8+
* Machine Learning: Scikit-Learn, XGBoost, LightGBM
* Web Framework: Streamlit
* Data Handling: Pandas, NumPy
* Logging: Python Logging Module


5. PROJECT STRUCTURE

├── app.py              # Main Streamlit application script
├── model.py            # ML Pipeline & Voting Regressor logic
├── requirements.txt    # Python dependencies
├── logs/               # Directory for generated system logs
└── data/               # Source Kaggle dataset


6. HOW TO RUN

1. Install dependencies:
   pip install -r requirements.txt

2. Launch the dashboard:
   streamlit run app.py


Note: This project was developed as a college presentation to demonstrate 
the practical application of Ensemble Learning and End-to-End ML deployment.

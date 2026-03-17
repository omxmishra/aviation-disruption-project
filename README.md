# ✈️ Aviation Disruption Intelligence System

## Project Overview
A machine learning project that analyzes global aviation disruptions during geopolitical conflict scenarios. The system predicts whether a flight is likely to be cancelled or rerouted and provides interactive analytics through a deployed Streamlit dashboard.

## Key Features
- End-to-end machine learning pipeline  
- Multi-table dataset integration and preprocessing  
- Exploratory data analysis with insights  
- Model comparison across multiple algorithms  
- Prediction system for flight disruption outcomes  
- Interactive Streamlit dashboard  
- Analytics on airlines, airports, and disruption severity  

## Dataset Description
The dataset includes:

- Flight reroutes with delay, distance, and fuel cost  
- Flight cancellations with reasons and passenger impact  
- Airspace closures across multiple regions  
- Airport disruptions with severity and duration  
- Conflict events influencing aviation operations  

## Project Structure

aviation-disruption-project/

│
├── data/

│   ├── raw/
│   └── processed/
│

├── notebooks/

│   └── aviation_analysis.ipynb
│

├── src/

│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── predict.py
│

├── models/

│   ├── aviation_disruption_model.pkl
│   └── model_columns.json
│

├── app/

│   └── streamlit_app.py
│

├── assets/
│

├── requirements.txt

├── README.md

└── .gitignore


## Machine Learning Approach
- Problem Type: Binary Classification  
- Target Variable: disruption_category (Cancelled or Rerouted)  

Models evaluated:
- Logistic Regression  
- Decision Tree  
- Random Forest  
- Gradient Boosting  
- XGBoost  

Final model:
- Gradient Boosting Classifier  

## Model Performance
The model achieved approximately 53 percent accuracy on the test dataset. Due to the nature of the data and limited predictive features, the focus of the project is on building a robust pipeline and system rather than optimizing accuracy.

## Streamlit Application
The project includes an interactive Streamlit dashboard with:

- Prediction interface for disruption outcome  
- Dropdown-based input selection  
- Analytics dashboard with airline and airport insights  
- Severity distribution visualization  
- Dataset preview  

## How to Run the Project

Clone the repository:
git clone <your-repo-link>
cd aviation-disruption-project

Install dependencies:
pip install -r requirements.txt

Run the application:
streamlit run app/streamlit_app.py


## Technologies Used
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- XGBoost  
- Matplotlib  
- Streamlit  

## Future Improvements
- Improve feature engineering with additional external data  
- Enhance model performance with larger datasets  
- Add real-time data integration  
- Improve UI with advanced visualizations  
- Deploy the application on cloud platforms  

## Conclusion
This project demonstrates an end-to-end machine learning workflow for analyzing and predicting aviation disruptions. It highlights the integration of data engineering, modeling, and deployment into a structured and interactive system.

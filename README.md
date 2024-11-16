# Salary Prediction App

## Deployed Link
You can try the live demo of the app by clicking [here](https://salary-prediction-model-using-ml.streamlit.app/).

## Overview
This is a web application built using **Streamlit** and a **Linear Regression Model** to predict the salary of an individual based on their years of experience. 
Users can either input their years of experience for a single prediction or upload a CSV file to get predictions for multiple entries.

## Features
- **Single Prediction**: Enter your years of experience and get an immediate salary prediction.
- **Batch Prediction**: Upload a CSV file with the `YearsExperience` column, and the app will predict salaries for each entry.
- **Visualization**: Visualize salary trends and compare actual vs predicted salaries in interactive graphs.

## Technologies Used
- **Streamlit** for building the web interface
- **Python** for data manipulation and model prediction
- **Scikit-learn** for the Linear Regression model
- **Plotly** for interactive graphs

## Installation
To run the app locally:

1. Clone this repository:
   ```bash
   git clone https://github.com/rohit-2002/Salary-Prediction-App.git
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
3. Run the Streamlit app:
   ```bash
   streamlit run app.py

# Stock Price Prediction System

Welcome to the Stock Price Prediction System. This system is designed to predict stock prices using a linear regression model and exposes the model via a Flask API. The guide below will walk you through the steps to set up and deploy the prediction system.

## Table of Contents

1. [Data Collection](#data-collection)
2. [Data Preparation](#data-preparation)
3. [Model Training](#model-training)
4. [Flask API Setup](#flask-api-setup)
5. [Deployment](#deployment)
6. [Testing](#testing)
7. [Maintenance](#maintenance)

---

## 1. Data Collection <a name="data-collection"></a>

- **Objective**: Collect data for the stock you want to predict. This includes the stock's historical prices and relevant market factors.
- **Tools/Platforms**: Yahoo Finance, Quandl, Alpha Vantage, etc.
- **Steps**:
  1. Choose a reliable data source.
  2. Gather historical stock prices.
  3. Collect relevant market factors (e.g., trading volume, market indices).

---

## 2. Data Preparation <a name="data-preparation"></a>

- **Objective**: Ensure that the data is clean, free of anomalies, and prepared for modeling.
- **Tools**: Pandas, NumPy
- **Steps**:
  1. Remove any missing or erroneous data points.
  2. Normalize or scale data if necessary.
  3. Split data into training and test sets.

---

## 3. Model Training <a name="model-training"></a>

- **Objective**: Train a linear regression model using the prepared data.
- **Tools**: scikit-learn
- **Steps**:
  1. Initialize a linear regression model.
  2. Train the model using the training dataset.
  3. Evaluate model performance using metrics like mean squared error or R-squared.

---

## 4. Flask API Setup <a name="flask-api-setup"></a>

- **Objective**: Set up a Flask API that will expose the trained model for prediction requests.
- **Tools**: Flask
- **Steps**:
  1. Initialize a Flask app.
  2. Create API endpoints to receive user inputs (stock symbol, date range) and return predictions.
  3. Integrate the trained model into the Flask app.

---

## 5. Deployment <a name="deployment"></a>

- **Objective**: Make the Flask API available for users by deploying it.
- **Tools**: PythonAnywhere
- **Steps**:
  1. Register on PythonAnywhere.
  2. Create a new web app.
  3. Upload all necessary code and dependencies.
  4. Configure the web app to launch the Flask API.

---

## 6. Testing <a name="testing"></a>

- **Objective**: Ensure that the deployed Flask API is functioning correctly.
- **Tools**: Postman, cURL
- **Steps**:
  1. Send prediction requests to the Flask API endpoints.
  2. Verify the responses against expected outcomes.

---

## 7. Maintenance <a name="maintenance"></a>

- **Objective**: Ensure the prediction model remains accurate over time.
- **Steps**:
  1. Monitor model performance metrics regularly.
  2. Retrain the model with fresh data if performance drops.
  3. Update the model or features if necessary.

---

## Feedback & Contribution

We welcome feedback and contributions to improve this system. Please raise an issue or submit a pull request if you have suggestions or improvements.

---

## Streamlit Web App <a name="streamlit-web-app"></a>

We have successfully developed a web app using Streamlit that provides a user-friendly interface for our Stock Price Prediction System. The web app allows users to easily input their stock data and get predictions in real-time without any technical know-how.

Furthermore, we've hosted our Streamlit app on Hugging Face, allowing for seamless access and scalable user interactions. You can access the Streamlit app [here](https://huggingface.co/spaces/NEXAS/stock).

---



**Author**: NARESH KUMAR LAHAJAL  
**License**: MIT 

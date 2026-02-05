# Fraud-Detection-with-machine-learning-end2end-project
## 📌 Project Overview

This project demonstrates an end-to-end fraud detection system built using machine learning, covering the full lifecycle from data preprocessing and feature engineering to model training, evaluation, and deployment via an interactive web application.

The goal is to identify potentially fraudulent financial transactions in real time while maintaining high accuracy and interpretability — a common challenge in banking and financial services.

This repository is designed to reflect real-world industry practices rather than a toy example.

## 🎯 Business Problem

Financial fraud causes significant revenue loss and operational risk for banks and payment platforms.
The challenge is to:

Detect fraudulent transactions accurately

Minimize false positives (blocking legitimate customers)

Make predictions fast enough for real-time decision making

This system addresses these challenges by leveraging supervised machine learning and feature engineering inspired by real banking transactions.

🧠 Solution Architecture

## The project follows a structured ML workflow:

# Data Understanding & Cleaning

Handled missing values and inconsistencies

Ensured correct data types and distributions

# Feature Engineering

Transaction type encoding

Balance change calculations for origin and destination accounts

Removal of data leakage features

# Model Development

Logistic Regression (baseline, interpretable model)

Model evaluation using classification metrics

Focus on fraud class detection performance

# Model Persistence

Trained model saved using joblib

Ensures reproducibility and deployment readiness

# Deployment

Streamlit web application for real-time predictions

User-friendly interface for transaction input

Fraud probability output for decision support

## 📁 Dataset

- Public dataset (e.g., [Kaggle: Fraud Detection Dataset][https://www.kaggle.com/datasets/atulmittal199174/credit-risk-analysis-for-extending-bank-loans/data](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download))  
- Features include: `type`, `amount`, `nameOrig`, `oldbalanceOrg`, `newbalanceOrig`,`nameDest`,`oldbalanceDest`,`newbalanceDest`,`isFraud`,`isFlaggedFraud`
- Target variable: `isFraud` 


## 🛠️ Tech Stack

Programming Language: Python

Data Analysis: Pandas, NumPy

Machine Learning: Scikit-learn

Model Serialization: Joblib

Web App Framework: Streamlit

Version Control: Git & GitHub


## Application Output

The model returns:

1 for fraudulent transactions

0 for non-fraudulent transactions

The application can also display the probability of fraud, which is useful for risk-based decision making.

## 🖥️ Streamlit Application

The deployed app allows users to:

Select transaction type

Enter transaction and balance details

Receive an instant fraud prediction

View confidence/probability of fraud

This simulates how fraud analysts or automated systems would interact with the model in production.

## Running the Project
Clone the repository
git clone https://github.com/motheomoshageng/fraud-detection-project.git
cd fraud-detection-project

# Install dependencies
pip install -r requirements.txt

Start the application
streamlit run app.py

Project Structure
├── notebooks/        # Data exploration and model training
├── fraud_detection.py            # Streamlit application
├── model_lr.joblib   # Trained model
├── requirements.txt
└── README.md


## What This Project Shows

Through this project, I demonstrate:

An understanding of the full machine learning workflow

Practical feature engineering for transaction data

Building and deploying an interpretable ML model

Turning a model into a usable application

## Future Improvements

Try tree-based or ensemble models

Improve handling of class imbalance

Add logging and monitoring

## Deploy the application to a cloud platform

🔍 Key Takeaways for Employers

This project demonstrates my ability to:

Translate a business problem into a machine learning solution

Perform feature engineering aligned with domain knowledge

Build interpretable ML models suitable for regulated industries

Deploy models into usable applications

Follow clean, reproducible ML workflows

## 💼 About Me

I'm a data science enthusiast passionate about solving real-world problems using machine learning. This project showcases my ability to manage the full ML pipeline — from raw data to deployable solution.

📩 I'm open to entry-level roles in data science. 
Feel free to connect with me on  www.linkedin/motheo-moshageng/!






# README
# AI-Powered Phishing Detection Script
# 
# Overview:
# This script implements a Naive Bayes classifier to detect phishing emails.
# It processes a text file dataset ('phishing-2022.txt') and converts it into
# a format suitable for training, then provides a function to classify new emails.
# 
# Author: Faith Dennis Osse
# Date: July 30, 2025
# 
# Requirements:
# - Python 3.x
# - Libraries: pandas, numpy, scikit-learn
# - Dataset: 'phishing-2022.txt' at 'C:\Users\faith\Downloads\phishing-2022.txt'
#   (assumed to contain email text, one per line, with labels to be inferred or
#    manually added; a temporary CSV will be created)
# 
# Usage:
# 1. Ensure 'phishing-2022.txt' is at 'C:\Users\faith\Downloads\phishing-2022.txt'.
# 2. Run the script: `python3 phishing_detector.py`
# 3. Use the `classify_email(email_text)` function to test new emails.
# 
# Example:
# sample_email = "Click here to claim your prize!"
# result = classify_email(sample_email)
# print(f"Classification: {result}")
# 
# Notes:
# - The script assumes 'phishing-2022.txt' contains raw email text. It creates
#   a temporary 'phishing_corpus.csv' with 'email' and 'label' columns (label 1
#   for phishing, 0 for legitimate; adjust preprocessing if labels are present).
# - Adjust the file path if stored differently or move the file to the script
#   directory for simplicity.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Preprocess text file to CSV (simplified assumption: all emails are phishing)
with open(r'C:\Users\faith\Downloads\phishing-2022.txt', 'r', encoding='utf-8') as file:
    emails = file.readlines()
emails = [email.strip() for email in emails if email.strip()]
data = pd.DataFrame({'email': emails, 'label': 1})  # Label 1 for phishing
data.to_csv('phishing_corpus.csv', index=False)

# Load the processed dataset
data = pd.read_csv('phishing_corpus.csv')
X = data['email']
y = data['label']

# Convert email text to feature vectors
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(X)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print(classification_report(y_test, y_pred))

# Function to classify a new email
def classify_email(email_text):
    email_vector = vectorizer.transform([email_text])
    prediction = model.predict(email_vector)
    return "Phishing" if prediction[0] == 1 else "Legitimate"

# Example usage
sample_email = "Click here to claim your prize!"
print(f"Sample email classification: {classify_email(sample_email)}")

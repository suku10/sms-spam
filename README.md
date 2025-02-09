SMS Spam Detection System

Overview

The SMS Spam Detection System is a machine learning-based project designed to classify SMS messages as either spam or non-spam (ham). The project leverages text preprocessing techniques and machine learning algorithms to build an efficient spam classifier that minimizes false positives while maintaining high accuracy.

Features

Preprocessing of SMS messages through cleaning, tokenization, and vectorization (TF-IDF).

Implementation of multiple machine learning models, including logistic regression, decision trees, and neural networks.

Evaluation of models based on performance metrics such as accuracy, precision, recall, and F1-score.

Deployment-ready spam filtering solution for real-time classification of SMS messages.

Dataset

The project uses a dataset of SMS messages categorized into spam and non-spam (ham). The dataset is preprocessed to remove noise, normalize text, and extract meaningful features for model training.

Installation

To run the project, follow these steps:

Clone the repository:

git clone https://github.com/suku10/sms-spam.git
cd sms-spam

Install the required dependencies:

pip install -r requirements.txt

Run the preprocessing and model training script:

python train_model.py

Use the trained model to classify SMS messages:

python predict.py --message "Your free lottery ticket awaits! Claim now!"

Methodology

Data Preprocessing: Cleaning and normalizing text, removing stopwords, and converting text into numerical vectors using TF-IDF.

Feature Extraction: Tokenization and transformation of text data into feature vectors.

Model Training: Training multiple classification models and selecting the best-performing model.

Evaluation: Assessing models based on accuracy, precision, recall, and F1-score.

Deployment: Implementing the selected model for real-time SMS classification.

Results

The best-performing model achieves high accuracy and significantly reduces false positives compared to traditional spam filters. The system provides an effective and scalable solution for SMS spam detection.

Contact

For any queries or collaborations, feel free to reach out via GitHub issues.

#!/usr/bin/env python
# coding: utf-8

# # Binary Classification with a Bank Churn Dataset

# In[1]:


import pandas as pd

#Load the CSV file
file = pd.read_csv('sample_submission.csv')
train_file = pd.read_csv('train.csv')
test_file = pd.read_csv('test.csv')

#Display the first few rows of the dataframe
print(file.head())
print(train_file.head())
print(test_file.head())


# # Build a predictive model:
# 1. Data Preprocessing: Handle missing values, encode categorical variables, and normalize/standardize numerical features.
# 2. Model Selection: Choose a suitable machine learning model.
# 3. Training the Model: Use the training data to train the model.
# 4. Model Evaluation: Evaluate the model's performance on the training data using precision, recall, and AUC-ROC score.
# 5. Predictions: Use the trained model to predict 'Exited' for the test dataset.

# In[4]:


from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

# Separating features and target variable in training data
X_train = train_file.drop('Exited', axis=1)
y_train = train_file['Exited']

# Preprocessing Steps:
# 1. Impute missing values for numerical columns
# 2. Standardize numerical columns
# 3. One-hot encode categorical columns

# Identifying numerical and categorical columns
numerical_cols = X_train.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = X_train.select_dtypes(include=['object']).columns

# Creating transformers for numerical and categorical data
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combining transformers into a preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Preprocessing the training data
X_train_preprocessed = preprocessor.fit_transform(X_train)

# Splitting the processed training data for model evaluation
X_train_split, X_val_split, y_train_split, y_val_split = train_test_split(X_train_preprocessed, y_train, test_size=0.2, random_state=42)

X_train_preprocessed.shape, X_train_split.shape, X_val_split.shape


# # 1. Preprocessing Steps:
# - Missing values in numerical columns were imputed with the mean.
# - Numerical columns were standardized.
# - Categorical columns were one-hot encoded.
# # 2. Dataset Transformation:
# - The training data has been transformed into a format suitable for machine learning models.
# - The number of features has increased to 2812 due to one-hot encoding of categorical variables.
# # 3. Splitting for Model Evaluation:
# - The preprocessed training data has been split into two parts:
# - A training set (80%) for training the model.
# - A validation set (20%) for evaluating the model.

# I will select a machine learning model, train it using the training set, and evaluate its performance on the validation set using precision, recall, and AUC-ROC score.
# Given the nature of the data (a binary classification problem), Random Forest Classifier is a suitable choice for this demonstration.
# 
# I will use a smaller sample of the training data for quicker model training and evaluation due to the large size of the dataset and the high number of features after preprocessing.

# In[7]:


from sklearn.utils import resample
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, roc_auc_score

# Reducing the size of the training set by sampling
sampled_X_train_split, sampled_y_train_split = resample(X_train_split, y_train_split, n_samples=10000, random_state=42)

# Training the Random Forest Classifier on the sampled data
rf_model_sampled = RandomForestClassifier(random_state=42)
rf_model_sampled.fit(sampled_X_train_split, sampled_y_train_split)

# Predicting on the validation set
sampled_y_pred_val = rf_model_sampled.predict(X_val_split)

# Evaluating the model on the validation set
sampled_precision_val = precision_score(y_val_split, sampled_y_pred_val)
sampled_recall_val = recall_score(y_val_split, sampled_y_pred_val)
sampled_roc_auc_val = roc_auc_score(y_val_split, sampled_y_pred_val)

sampled_precision_val, sampled_recall_val, sampled_roc_auc_val


# Precision : 78.53%
# Recall : 38.02%
# ROC-AUC : 67.62%
# 
# For more accurate and robust predictions, consider using the full dataset.

# In[10]:


# Preprocessing the test data
X_test_preprocessed = preprocessor.transform(test_file)

# Making predictions on the test dataset
test_predictions = rf_model_sampled.predict_proba(X_test_preprocessed)[:, 1]

# Creating a DataFrame for the predictions
prediction_df = pd.DataFrame({
    'id' : test_file['id'],
    'Exited': test_predictions
})

prediction_df.head()


# The predictions are in the format of a probability between 0 and 1, where higher values indicate a higher likelihood of the 'Exited' event.

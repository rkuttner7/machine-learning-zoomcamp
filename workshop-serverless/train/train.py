#!/usr/bin/env python
# coding: utf-8

# The code is based on the modules 3 and 4. We use the same dataset: [telco customer churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

# System imports
import pickle

# libraries
import pandas as pd
import numpy as np
import sklearn

# named imports
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression


print(f'pandas=={pd.__version__}')
print(f'numpy=={np.__version__}')
print(f'sklearn=={sklearn.__version__}')

# Parameters
output_file = "model.bin"

def load_data():
    data_url = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-03-churn-prediction/WA_Fn-UseC_-Telco-Customer-Churn.csv'

    df = pd.read_csv(data_url)

    df.columns = df.columns.str.lower().str.replace(' ', '_')

    categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

    for c in categorical_columns:
        df[c] = df[c].str.lower().str.replace(' ', '_')

    df.totalcharges = pd.to_numeric(df.totalcharges, errors='coerce')
    df.totalcharges = df.totalcharges.fillna(0)

    df.churn = (df.churn == 'yes').astype(int)
    return df




def train_model(df):
    numerical = ['tenure', 'monthlycharges', 'totalcharges']

    categorical = [
        'gender',
        'seniorcitizen',
        'partner',
        'dependents',
        'phoneservice',
        'multiplelines',
        'internetservice',
        'onlinesecurity',
        'onlinebackup',
        'deviceprotection',
        'techsupport',
        'streamingtv',
        'streamingmovies',
        'contract',
        'paperlessbilling',
        'paymentmethod',
    ]

    #dv = DictVectorizer()

    train_dict = df[categorical + numerical].to_dict(orient='records')
    y_train = df.churn
    #X_train = dv.fit_transform(train_dict)

    #model = LogisticRegression(solver='liblinear')
    #model.fit(X_train, y_train)

    pipeline = make_pipeline(
        DictVectorizer(),
        LogisticRegression(solver='liblinear')
    )

    pipeline.fit(train_dict, y_train)

    #X = dv.transform(datapoint)
    #model.predict_proba(X)[0, 1]


    return pipeline
    

def save_model(filename, model):
    ### Save the model
    # Character Meaning:
    # 'w'       open for writing, truncating the file first
    # 'b'       file is binary, return contents as bytes objects without any decoding
    with open(filename, 'wb') as f_out:
        pickle.dump(model, f_out)

    print(f'model saved to {filename}')



df = load_data()
pipeline = train_model(df)
save_model(output_file, pipeline)

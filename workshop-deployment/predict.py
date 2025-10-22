
#!/usr/bin/env python
# coding: utf-8

 
# The code is based on the modules 3 and 4. We use the same dataset: [telco customer churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

import pickle


input_file = "model.bin"

datapoint = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 129.85
}

### Load model
# Character Meaning:
# 'r'       open for reading the file
with open(input_file, 'rb') as f_in: 
    pipeline = pickle.load(f_in)

#X = dv.transform(customer)
#y_pred = model.predict_proba(X)[0, 1]
y_pred = pipeline.predict_proba([datapoint])[0, 1]
churn = y_pred >= 0.5 

print("prob churn = ", y_pred)
print("churn = ", churn)





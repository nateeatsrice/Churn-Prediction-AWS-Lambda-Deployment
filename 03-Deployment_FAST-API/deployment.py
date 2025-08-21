#!/usr/bin/env python
# coding: utf-8

import pickle
import requests

with open('../log_reg.bin','rb') as f_in:
    (dv,model) = pickle.load(f_in)

datapoint = {
    'gender': 'male',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'yes',
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
    'monthlycharges': 30.85,
    'totalcharges': 29.85
}

X = dv.transform(datapoint)
model.predict_proba(X)[0, 1]

pipeline.fit(train_dict, y_train)


pipeline.predict_proba(datapoint)[0, 1]


url = 'http://localhost:9696/predict'

customer = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'yes',
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
    'totalcharges': 29.85
}

response = requests.post(url, json=customer)

predictions = response.json()

if predictions['churn']:
    print('accept loan application')
else:
    print('reject loan application')

for n in numerical:
    print(df[n].describe())
    print()

for c in categorical:
    print(df[c].value_counts())
    print()


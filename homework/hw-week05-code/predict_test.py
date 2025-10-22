#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'

datapoint = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}


response = requests.post(url, json=datapoint).json()
print(response)

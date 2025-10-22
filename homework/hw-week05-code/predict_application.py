
#!/usr/bin/env python
# coding: utf-8

# Web service application

# Homework 5

import pickle

from fastapi import FastAPI
import uvicorn

from typing import Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
# request

class Datapoint(BaseModel):
    # raise an error for additional fields
    model_config = ConfigDict(extra="forbid")

    lead_source: Literal["organic_search"]
    number_of_courses_viewed: int = Field(..., ge=0)
    annual_income: int = Field(..., ge=0) 

# response
class PredictResponse(BaseModel):
    convert_probability: float
    conversion: bool

app = FastAPI(title="convert-prediction")

input_file = "data/hw5-pipeline.bin"

datapoint = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

### Load model
# Character Meaning:
# 'r'       open for reading the file
with open(input_file, 'rb') as f_in: 
    pipeline = pickle.load(f_in)


def predict_single(datapoint):
    result = pipeline.predict_proba(datapoint)[0, 1]
    return float(result)

@app.post("/predict") 
def predict(datapoint: Datapoint) -> PredictResponse:
    prob = predict_single(datapoint.model_dump())

    return PredictResponse(
        convert_probability=prob,
        conversion=bool(prob >= 0.5)
    )




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)



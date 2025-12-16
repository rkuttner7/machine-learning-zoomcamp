#!/usr/bin/env python
# coding: utf-8

# Web service application

import pickle

from fastapi import FastAPI
import uvicorn

from typing import Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict

import numpy as np
import onnxruntime as ort
from keras_image_helper import create_preprocessor

onnx_model_path = 'clothing-model.onnx'

classes = [
    "dress",
    "hat",
    "longsleeve",
    "outwear",
    "pants",
    "shirt",
    "shoes",
    "shorts",
    "skirt",
    "t-shirt",
]

def preprocess_pytorch(X):
    # X: shape (1, 299, 299, 3), dtype=float32, values in [0, 255]
    X = X / 255.0

    mean = np.array([0.485, 0.456, 0.406]).reshape(1, 3, 1, 1)
    std = np.array([0.229, 0.224, 0.225]).reshape(1, 3, 1, 1)

    # Convert NHWC → NCHW
    # from (batch, height, width, channels) to (batch, channels, height, width)
    X = X.transpose(0, 3, 1, 2)

    # Normalize
    X = (X - mean) / std

    return X.astype(np.float32)


preprocessor = create_preprocessor(preprocess_pytorch, target_size=(224, 224))


session = ort.InferenceSession(
    onnx_model_path, providers=["CPUExecutionProvider"]
)
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

def predict_single(url):
    X = preprocessor.from_url(url)
    result = session.run([output_name], {input_name: X})
    float_predictions = result[0][0].tolist()

    predictions_dict = dict(zip(classes, float_predictions))
    
    top_class = max(predictions_dict, key=predictions_dict.get)
    top_probability = predictions_dict[top_class]

    return predictions_dict, top_class, top_probability


def lambda_handler(event, context):
    url = event["url"]
    result = predict_single(url)
    return result

# request

class Request(BaseModel):
    url: str = Field(..., example = "http://bit.ly/mlbookcamp-pants")


class PredictResponse(BaseModel):
    predictions: dict[str, float]
    top_class: str
    top_probability: float

app = FastAPI(title="clothing-model")

@app.post("/predict", response_model=PredictResponse) 
def predict(request: Request) -> PredictResponse:
    predictions, top_class, top_prob = predict_single(request.url)

    return PredictResponse(
        predictions=predictions,
        top_class=top_class,
        top_probability=top_prob
    )

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

import numpy as np
import onnxruntime as ort
from keras_image_helper import create_preprocessor

onnx_model_path = "clothing-model-new.onnx"

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


preprocessor = create_preprocessor('xception', target_size=(299, 299))


session = ort.InferenceSession(
    onnx_model_path, providers=["CPUExecutionProvider"]
)
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

def predict(url):
    X = preprocessor.from_url(url)
    result = session.run([output_name], {input_name: X})
    float_predictions = result[0][0].tolist()
    return dict(zip(classes, float_predictions))


def lambda_handler(event, context):
    url = event["url"]
    result = predict(url)
    return result
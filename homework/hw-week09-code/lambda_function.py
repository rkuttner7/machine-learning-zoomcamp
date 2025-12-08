import numpy as np
import onnxruntime as ort
from keras_image_helper import create_preprocessor

onnx_model_path = 'hair_classifier_empty.onnx'

def preprocess_pytorch(X):
    X = X / 255.0

    mean = np.array([0.485, 0.456, 0.406]).reshape(1, 3, 1, 1)
    std = np.array([0.229, 0.224, 0.225]).reshape(1, 3, 1, 1)

    # Convert NHWC → NCHW
    # from (batch, height, width, channels) to (batch, channels, height, width)
    X = X.transpose(0, 3, 1, 2)

    # Normalize
    X = (X - mean) / std

    return X.astype(np.float32)

preprocessor = create_preprocessor(
    preprocess_pytorch, 
    target_size=(200, 200))


session = ort.InferenceSession(
    onnx_model_path, providers=["CPUExecutionProvider"]
)
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

def predict(url):
    X = preprocessor.from_url(url)
    result = session.run([output_name], {input_name: X})
    float_predictions = result[0][0].tolist()
    return float_predictions


def lambda_handler(event, context):
    url = event["url"]
    result = predict(url)
    return result
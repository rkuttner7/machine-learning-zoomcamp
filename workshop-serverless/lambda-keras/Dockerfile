FROM public.ecr.aws/lambda/python:3.13

# skipped using uv during workshop to save coding time
RUN pip install onnxruntime keras-image-helper

COPY clothing-model-new.onnx clothing-model-new.onnx
COPY lambda_function.py ./

CMD ["lambda_function.lambda_handler"]
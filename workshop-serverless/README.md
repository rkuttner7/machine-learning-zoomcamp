# Deploy Machine Learning Models with AWS Lambda (Serverless) and ONNX    

[instructor's notes](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/09-serverless/workshop)  
  
* Build and test Lambda functions for ML models
* Use Docker and AWS Elastic Container Registry (ECR) to package dependencies
* Optimize Docker images for faster deployment
* Handle warm and cold starts efficiently
* Deploy both traditional ML models and deep learning models (PyTorch, Keras)
* Compare Lambda vs SageMaker for cost and complexity
* Prepare your pipeline for production-grade model deployment
  
  

## Plan

The plan for the workshop:
* Creating a simple AWS Lambda function
* Deploying Scikit-Learn models with Docker
* Using ONNX for Keras and TF models
* ONNX for PyTorch models

## Prerequisites

* [AWS Account](https://aws.amazon.com/console/)
* [AWS Cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)


## Scikit-Learn Models  
  
train a simple scikit-learn model that we will later deploy  

Copy training script from previous deplopyment (uv-fastapi) workshop.  
```bash
cd train
uv sync
uv run python train.py
```
Generates `model.bin` we will use to deploy.  
  
## AWS Lambda  

Start with simplest AWS Lambda application.  
  
Create a file `lambda_function.py`, in new directory `lambda-sklearn\`:  
```python
def predict_single(customer):
    # we will put our model here
    return 0.56

def lambda_handler(event, context):    
    print("Parameters:", event)
    customer = event['customer']
    prob = predict_single(customer)
    return {
        "churn_probability": prob,
        "churn": bool(prob >= 0.5)
    }
```

### "**deploy**":  
  
* Go to AWS -> Lambda
* Click "Create Function"
* Author from scratch
    * Name: "churn-prediction"
    * Runtime: Python 3.13
    * Default execution role: create a new one (selected by default)
    * Additional configuration - keep as is
* Put the lambda function code there

    
### Test deployment - on AWS platform  
  
Now **test** it. Deploy it, click `test`, then create a new event with the following data:
```json
{
  "customer": {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 1,
    "monthlycharges": 29.85,
    "totalcharges": 29.85
  }
}
```
  
Should see the following:  
```bash
{
  "churn_probability": 0.56,
  "churn": true
}
```
  
### Test deployment - local CLI:  
```bash
aws lambda invoke \
  --function-name churn-prediction \
  --cli-binary-format raw-in-base64-out \
  --payload file://lambda-1-simple/customer.json \
  output.json
```
  
### Test deployment - boto3:  

[Configure AWS account authentication credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration)  
  
see `lambda_function.py\invoke.py`:  
```python
import boto3
import json

lambda_client = boto3.client('lambda')

customer = [json example data here]

response = lambda_client.invoke(
    FunctionName='churn-prediction',
    InvocationType='RequestResponse',
    Payload=json.dumps(customer)
)

result = json.loads(response['Payload'].read())
print(json.dumps(result, indent=2))
```
  
### Test deployment - expose as a web service  

see [unit 9.7 about API Gateway | ML Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/09-serverless/07-api-gateway.md)  

* API Gateway > click `create API` > scroll down to **REST API** and click `Build`  
* Under **Create REST API** enter:
    * **API Name** enter: "clothes-classification" 
    * **Security Policy** select: "SecurityPolicy_[details]"
    *click `Create API`

>  When you use an enhanced security policy, you must also set the endpoint access mode for additional governance.

* click `Create resource`:  
  * **Resource name**: "predict"
  * click `Create resource`
  
>  REST convention is to name resources as nouns, but we break this to follow naming used in earlier sessions.  
  
* click `Create method`:  
    * **Method type** select: Post
    * **Lambda function** enter: 
        * old lecture suggests: "clothes-classification"
        * AWS prompts docker image: "arn:aws:lambda:us-east-2:268428820208:function:churn-prediction"
    * click `create`  
    
> Methods our how endpoints are envoked.  
  

* scroll down and over to select **Test**
  * **Request body** enter either:   
      * old lecture points to image of pants: {'url': 'http://bit.ly/mlbookcamp-pants'}
      * current use customer data as json: (see above)  
  * click `Test`  
  
* click `Deploy API`   

* copy the URL

> !!WARNING!!
> After deployment the URL is open to the internet for access by anyone. 
> Only keep available during testing and close after to avoid abuse.  
  

In the test script `lambda-sklearn\test.py` replace the `url` with deployed endpoint URL.  
    
## AWS Lambda with Docker: Running Locally  

```Dockerfile
FROM public.ecr.aws/lambda/python:3.13
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

COPY pyproject.toml uv.lock ./
RUN uv pip install --system -r <(uv export --format requirements-txt)

COPY lambda_function.py model.bin ./

CMD ["lambda_function.lambda_handler"]
```
  
Build docker image:  
```bash
docker build -t churn-prediction-lambda .
```
  
Run:  
```bash
docker run -it --rm -p 8080:8080 churn-prediction-lambda
```
  
Test (see test.py):  
```python
url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

result = requests.post(url, json=customer).json()
print(result)
```

  
## AWS Lambda: Deployment  
  
Create a registry either through web interface or AWS CLI:   
```bash
aws ecr create-repository \
  --repository-name "churn-prediction-lambda" \
  --region "us-east-2"
```
  
see `lambda-sklearn\publish.sh`.

```sh
#!/bin/bash

AWS_REGION=us-east-2

ECR_URI=268428820208.dkr.ecr.${AWS_REGION}.amazonaws.com

REPO_URL=${ECR_URI}/churn-prediction-lambda

REMOTE_IMAGE_TAG="${REPO_URL}:v1"

LOCAL_IMAGE=churn-prediction-lambda


# run it only once
# aws ecr create-repository \
#   --repository-name ${IMAGE_NAME} \
#   --region ${AWS_REGION}

aws ecr get-login-password \
  --region ${AWS_REGION} \
| docker login \
  --username AWS \
  --password-stdin ${ECR_URI}

docker build -t ${LOCAL_IMAGE} .

# Tag local image with remote image tag
docker tag ${LOCAL_IMAGE} ${REMOTE_IMAGE_TAG}
docker push ${REMOTE_IMAGE_TAG}

echo "Done"
```

**Create Lambda function based on image**:
* click `create function` > select `Container image`  
* **Function Name** enter: churn-prediction-docker  
* **Select container image**:  
  * **ECR image repository** select: churn-prediction-lambda  
  * **Images**: v1
  

## AWS Lambda: TensorFlow Models  
  
Converting the Tensorflow Model from Keras has difficulties that instructor needed to hack, must be done in Docker to avoid version conflicts between TensorFlow and ONNX. Details are skipped here.  
  
Download a ONNX version of the classification model:
```bash
wget https://github.com/DataTalksClub/machine-learning-zoomcamp/releases/download/dl-models/clothing-model-new.onnx
```
  
The ONNX model is loaded using the following:  
```python
import onnxruntime as ort

onnx_model_path = "clothing-model-new.onnx"
session = ort.InferenceSession(onnx_model_path, providers=["CPUExecutionProvider"])

inputs = session.get_inputs()
outputs = session.get_outputs()

input_name = inputs[0].name
output_name = outputs[0].name
```
  
See `lambda-keras/lambda-function.py` for full implementation.  
  
Build the prediction model (Dockerfile similar to sklearn example):  
```bash
docker build -t clothing-lambda-keras .
docker run -it --rm -p 8080:8080 clothing-lambda-keras
```
  
Test the model using the image of pants at URL "http://bit.ly/mlbookcamp-pants". See `lambda-keras/test.py`.     

To deploy need to configure lambda-function with:  
  * **RAM**: >= 500MB
  * **timeout**: 30 - 60 seconds
  
## AWS Lambda: PyTorch Models  
  
Make a new directory `lambda-pytorch/` for this example.

More detailed notes on PyTorch model `notes/project-week08-02-pytorch-deep_learning.ipynb`.   
  
Download trained model:  
```bash
wget https://github.com/DataTalksClub/machine-learning-zoomcamp/releases/download/dl-models/clothing_classifier_mobilenet_v2_latest.onnx
```

(Optional) parameterize model selection in `lambda_function.py`:  
```python
import os

# environment variable defining model, defaults to 'clothing_classifier_mobilenet_v2_latest.onnx'
os.getenv('MODEL_PATH', 'clothing_classifier_mobilenet_v2_latest.onnx')
```
  
Updates:
  * Pre-process the model:  
      * PyTorch uses a different format (not BCHW, but BHWC, where B is batch, C is channel, W is width and H is height)
  * Target image is '224' to meet model 'mobilenet' expectation
  
Build and run the container:  
```bash
docker build -t clothing-pytorch .
docker run -it --rm -p 8080:8080 clothing-pytorch
```

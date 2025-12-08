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

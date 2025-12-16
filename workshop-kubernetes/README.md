# Kubernetes Tutorial: Deploy Machine Learning Models with Docker and FastAPI
  

[instructor's notes](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/10-kubernetes/workshop) 
 
## Prerequisites:  

* Docker
* FastAPI
* Kubernetes
* kind
* uv
  
## Environment Setup

### Install kubectl:

[Install and Set Up kubectl on Linux](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)  

```bash
cd 

mkdir bin && cd bin

curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
```

- Install globally (if user has root access):
```bash
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```
  
- Else in `.bashrc` add to path to install locally (if user does not have root access):
```bash
nano ~/.bashrc

# scroll to bottom of .bashrc and append to $PATHadd:
export PATH="${PATH}:${HOME}/bin"
```
  
Test version and path to binary:  
```bash
kubectl version --client
which kubectl
```
  
### Install kind:  
  
[Install kind](https://kind.sigs.k8s.io/docs/user/quick-start) kind is a tool for running local Kubernetes clusters using Docker container **nodes**.  
  
- Install globally (if user has root access):
```bash
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.30.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

- Install locally (if user does not have root access):
```bash
[ $(uname -m) = x86_64 ] && curl -Lo ${HOME}/bin/kind https://kind.sigs.k8s.io/dl/v0.30.0/kind-linux-amd64
chmod +x ${HOME}/bin/kind
```
  
Verify installation:
```bash
kind version
which kind
```

### Model Preparation

Use a pre-trained PyTorch model that classifies clothing items. 
  
Download the ONNX model:  
```bash
wget https://github.com/DataTalksClub/machine-learning-zoomcamp/releases/download/dl-models/clothing_classifier_mobilenet_v2_latest.onnx -O clothing-model.onnx
```

### Building the FastAPI Service
  
Create a FastAPI application that serves the ONNX model for inference.  
  
The service structure is similar to what we built in the FastAPI workshop, but adapted for ONNX models.
  
Initialize the project:  
  
```bash
# cd service
uv init
rm main.py
```

Add dependencies:  
```bash 
uv add fastapi uvicorn onnxruntime keras-image-helper
```

Create the FastAPI application (See `app.py`) based on:
* Web service application: `workshop-deployment/churn_application.py`
* `workshop-serverless/lambda-pytorch/lambda_function.py`
  
Include health check expected by Kubernetes:
```python
@app.get("/health")
def health():
    return {"status": "healthy"}
```
  
Spin up application and run a health check:
```bash
uv run uvicorn app:app --host 0.0.0.0 --port 8080 --reload

curl localhost:8080/health
```
  
Test the output through the documentation url `http://localhost:8080/docs`.

Expand the application to make more informative response:
```python
def predict_single(url: str):
    ...
    predictions_dict = dict(zip(classes, float_predictions))
    top_class = max(predictions_dict, key=predictions_dict.get)
    top_probability = predictions_dict[top_class]
    
    return predictions_dict, top_class, top_probability   

class PredictResponse(BaseModel):
    predictions: dict[str, float]
    top_class: str
    top_probability: float 

@app.post("/predict", response_model=PredictResponse) 
def predict(request: Request) -> PredictResponse:
    predictions, top_class, top_prob = predict_single(request.url)

    return PredictResponse(
        predictions=predictions,
        top_class=top_class,
        top_probability=top_prob
    )
```
  
## Docker Containerization  

Build container similar to those used in previous workshops.  

```bash  
docker build -t clothing-classifier:v1 .  
```
  
Test the container locally:  
```bash
docker run -it --rm -p 8080:8080 clothing-classifier:v1
```

## Kind Cluster
  
Create a local Kubernetes cluster:
```bash
kind create cluster --name mlzoomcamp
```

* Creates a single-node Kubernetes cluster
* Configures kubectl to use this cluster
  
Verify the cluster is running:
```bash
kubectl cluster-info
kubectl get nodes
```
  
Load Image to Kind:
```bash
kind load docker-image clothing-classifier:v1 --name mlzoomcamp
```

* Kind clusters run in Docker, so they can't access images from your local Docker daemon by default. We need to load the image into Kind.


## Kubernetes: Deployment  
  
Kubernetes Resources:
* **Pod**: The smallest deployable unit in Kubernetes (one or more containers)
* **Deployment**: Manages a set of identical Pods, handles updates and scaling
* **Service**: Exposes Pods to network traffic
* **HPA** (Horizontal Pod Autoscaler): Automatically scales Pods based on metrics
  
Create `k8s/deployment.yaml`: 

* **replicas**: 2 - Run 2 copies of our service
* **imagePullPolicy**: Never - Use local image (don't pull from registry)
* **resources**: Memory and CPU limits/requests
* **livenessProbe**: Restart container if unhealthy
* **readinessProbe**: Only send traffic when ready

Deploy it:  
```bash
kubectl apply -f k8s/deployment.yaml
```
  
Check the deployment:  
```bash
kubectl get deployments
kubectl get pods
kubectl describe deployment clothing-classifier
```
  
## Kubernetes: Service Manifest
  
**services**: act as entry points to route requests to the correct pods  

Create `k8s/service.yaml`:  
  
* **type**: NodePort - Expose on a static port on each node
* **nodePort**: 30080 - Accessible on port 30080 from host
* **selector** - Routes traffic to Pods with matching labels
   
Deploy it:    
```bash
kubectl apply -f k8s/service.yaml
```
  
Check the service:
```bash
kubectl get services
kubectl describe service clothing-classifier
```
  
## Test Deployed Service  
  
With NodePort, the service is accessible on `localhost:30080`:  
```bash
curl http://localhost:30080/health
```
  
Our kind cluster is not configured for NodePort, so it won't work.  
  
Use kubectl port-forward from the service to the host machine for local testing:    
```bash
kubectl port-forward service/clothing-classifier 30080:8080
```
  
> **NOTE**:
> Can also port forward from nodes to host machine to debug issues. To see how pod responds.    
    

When we deploy to EKS, it won't be a problem - there Elastic Load Balancer will solve this problem.  
  
## Horizontal Pod Autoscaling  
  
Kubernetes can automatically scale your application based on CPU or memory usage.
  
Install metrics-server in kubectl:  
```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```
  
* Desribes how much CPU is used on each of nodes.

When run locally with Kind, patch metrics-server to work without TLS:    
```bash
kubectl patch -n kube-system deployment metrics-server --type=json -p '[{"op":"add","path":"/spec/template/spec/containers/0/args/-","value":"--kubelet-insecure-tls"}]'
```

Create `k8s/hpa.yaml`:  
* Scale between 2 and 10 replicas
* Target 50% CPU utilization
* Automatically adds/removes Pods based on load
  
Deploy HPA:  
```bash
kubectl apply -f k8s/hpa.yaml
```
  
Check HPA status:  
```bash
kubectl get hpa
kubectl describe hpa clothing-classifier-hpa
```
  
### Test Autoscaling   
  
Create load to trigger autoscaling, simple load test (see `load_test.py`):    

Include development only dependency for local testing:  
```bash
uv add --dev requests
```
  
Run the test:  
```bash
uv run python load_test.py
```  
  
While running the load test, watch the HPA in another terminal:  
```bash
kubectl get hpa -w
```
  
See the number of replicas increase as CPU usage rises:  
```bash
kubectl get pods -w
```
  
## Managing the Deployment  
  
### **Updating the Application**
  
If you make changes to your code:  
1. Rebuild the image with a new tag:  
```bash
docker build -t clothing-classifier:v2 .
```
2. Load to Kind:  
```bash
kind load docker-image clothing-classifier:v2 --name mlzoomcamp
```
3. Update deployment YAML file and apply:  
```bash
kubectl apply -f k8s/deployment.yaml
```
  
Watch the rollout:  
```bash
kubectl rollout status deployment/clothing-classifier
```

### **Viewing Logs**:  
  
All Pods:
```bash
kubectl logs -l app=clothing-classifier --tail=20
```
  
Specific Pod:
```bash
kubectl logs <pod-name>
```
  
Follow logs:
```bash
kubectl logs -f -l app=clothing-classifier
```
  
### **Debugging**:  
  
Describe resources:  
```bash
kubectl describe deployment clothing-classifier
kubectl describe pod <pod-name>
kubectl describe service clothing-classifier
```
  
Get events:
```bash
kubectl get events --sort-by='.lastTimestamp'
```
  
Execute commands in a Pod:  
```bash
kubectl exec -it <pod-name> -- /bin/bash
```
    
[Deploy and Access the Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)
  
### **Cleanup**:   
  
Delete the deployment and service:
```bash
kubectl delete -f k8s/deployment.yaml
kubectl delete -f k8s/service.yaml
kubectl delete -f k8s/hpa.yaml
```

Or, delete everything at once:  
```bash
kubectl delete all -l app=clothing-classifier
kubectl delete hpa clothing-classifier-hpa
```
  
Delete the Kind cluster:
```bash
kind delete cluster --name mlzoomcamp
```
  
Delete the docker image:
```bash
docker images
docker rmi <IMAGE ID>
```
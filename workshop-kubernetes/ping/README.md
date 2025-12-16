# Kubernetes simple service
  
Deploy a simple web application to a kubernetes cluster.  
    
## Initialize the project:  
  
```bash
# cd service
uv init
rm main.py
```

Add dependencies:  
```bash 
uv add fastapi uvicorn
```
  
## Create a simple ping application in FastAPI 
  
(see `ping.py` and `Dockerfile`)  
  
Build the image:
```bash
docker build -t ping:v001 .
```
> **Note**:  
> Need to specify the **tag** along with the app name for the local kubernetes setup Kind to run without problems.  
  
Run the image:
```bash
docker run -it --rm -p 9696:9696 ping:v001
```
  
Test the application:
```bash
curl localhost:9696/ping 
```

## Create a cluster with Kind. 
  
Specify the node image:
```bash
kind create cluster --image kindest/node:v1.23.0
```

## Setup kubernetes cluster and test it 
  
### Create a **cluster**:  
```bash
# (default cluster name is "kind")  
kind create cluster 
```
  
Information on kubectl cluster kind:
```bash
 kubectl cluster-info --context kind-kind
 ```
   
Check running services:
 ```bash
kubectl get service
 ```
  
### Create a **deployment** (see `deployment.yaml`)
```bash
kubectl apply -f deployment.yaml
```
  
### Load the docker image into our cluster: 
```bash
kind load docker-image ping:v001
```
  
Check running pod(s):  
```bash
kubectl get pod
```
  
Test the pod: 
* specify the ports: 
```bash
kubectl port-forward <pod-name> 9696:9696 
```
* request response:
```bash
curl localhost:9696/ping
```
  
### Create **service** for deployment (see `service.yaml`)  
```bash
kubectl apply -f service.yaml
```
  
List of external and internal services: 
```bash
kubectl get service
```
  
Test the service: 
* port forwarding and specify ports: 
```bash
# use 8080 instead of 80 to avoid permission issues
kubectl port-forward service/ping 8080:80
```
* request response:
```bash
curl localhost:8080/ping
```

## Cleanup  

Delete the deployment and service:
```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
```
  
Or, delete everything:  
```bash
kubectl delete all -l app=ping
```
  
Delete the Kind cluster:
```bash
kind delete cluster --name kind
```
  
Delete the docker image:
```bash
docker images
docker rmi <IMAGE ID>
```
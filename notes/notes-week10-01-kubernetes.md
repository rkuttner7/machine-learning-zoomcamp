# 10.05 Kubernetes  


### **Notes**:  
  
**Kubernetes** (K8s): is an open-source system for automating the deployment, scaling, and management of containerized applications. Ensures that your application stays responsive, efficient, and ready to scale at any moment.  
  
Kubernetes Cluster is made up of:  
    * **nodes**: servers or computers running the processes
    * **pods**: containers that run specific images, reside within nodes
  
**deployemnt**: grouping of pods  
    * All pods in a deployment share the same Docker image and configuration  
  
**services**: act as entry points to route requests to the correct pods  
    * **External Services** (Load Balancer): Accessible from outside the cluster. Example: gateway service
    * **Internal Services** (Cluster IP): Accessible only within the cluster. Example: model service.
  
**INGRESS**: entry point at the front of the cluster. This directs user traffic to the appropriate external services.  



  
### **Further reading**:  
* [Amazon Elastic Container Services](https://aws.amazon.com/ecs/) container orchestration alternative to Kubernetes  
* [Google Cloud Run](https://cloud.google.com/run) container orchestration alternative to Kubernetes    
* [kubernetes extension|Visual Studio Code](https://code.visualstudio.com/docs/azure/kubernetes) handy extension to create K8s templates.
* [Load Balancer | Kind](https://kind.sigs.k8s.io/docs/user/loadbalancer/) service type that automatically provisions an external load balancer to distribute incoming traffic across multiple pods, ensuring high availability and performance for applications. It provides a stable IP address for accessing the application from outside the cluster.   
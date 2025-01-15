# FastAPI with Redis using Kubernetes

This repository contains an example of deploying a FastAPI application with Redis as a temporary database, orchestrated using Kubernetes.

## Folder Structure
```
fastapi-redis-kubernetes/
├── k8s/                 # Kubernetes YAML files
│   ├── fastapi-deployment.yaml
│   ├── redis-deployment.yaml
│   ├── fastapi-service.yaml
│   ├── redis-service.yaml
│   └── ingress.yaml
├── app/
│   ├── main.py          # FastAPI app code
│   ├── requirements.txt
├── Dockerfile
├── .env
└── README.md            # Instructions for setup
```

## Prerequisites
- Kubernetes cluster
- `kubectl` command-line tool
- Docker
- Docker Hub account (for pushing the image)

### Using Minikube
If you are using Minikube as your Kubernetes cluster:
1. Start Minikube:
   ```bash
   minikube start
   ```

   ```bash
   docker context use default
   ```

2. Set `kubectl` to use the Minikube context:
   ```bash
   kubectl config use-context minikube
   ```

3. Enable Ingress in Minikube:
   ```bash
   minikube addons enable ingress
   ```

4. Get the Minikube IP for local testing:
   ```bash
   minikube ip
   ```
   Use this IP to map `fastapi.local` in your `/etc/hosts` file:
   ```plaintext
   <minikube-ip> fastapi.local
   ```

## Steps to Deploy

1. **Build Docker Image**:
   ```bash
   source .env # load the .env file
   docker build -t fastapi-redis:latest .
   docker login
   docker push $DOCKER_USERNAME/fastapi-redis:latest
   ```

2. **Apply Kubernetes Manifests**:
   ```bash
   kubectl apply -f k8s/
   ```

3. **Verify Deployments and Services**:
   ```bash
   kubectl get pods
   kubectl get services
   ```

4. **Access FastAPI Application**:
   - Use `kubectl port-forward` to access FastAPI if Ingress is not configured:
     ```bash
     kubectl port-forward service/fastapi-service 8000:8000
     ```
   - Open `http://localhost:8000/docs` to access the Swagger UI.

5. **Using Ingress**:
   If Ingress is configured, ensure the domain `fastapi.local` points to your cluster.

## Features
- Increment key functionality in Redis
- FastAPI Swagger UI for interaction

## Troubleshooting
### Unable to Connect to the Cluster
If you encounter the error `Unable to connect to the server: dial tcp [::1]:8080`, ensure the following:
- Minikube is running:
  ```bash
  minikube start
  ```
- The correct context is set for `kubectl`:
  ```bash
  kubectl config use-context minikube
  ```
- The cluster is reachable and the API server is accessible:
  ```bash
  kubectl cluster-info
  ```

### Check Services and Pods
Ensure all services and pods are running correctly:
```bash
kubectl get pods
kubectl get services
```

If you still encounter issues, ensure your Kubernetes configuration file (`~/.kube/config`) is correct and matches your cluster.



# linux attempt
kubectl create deployment hello-fastapi-kube --image=registry.hub.docker.com/chanyanhon/fastapi-redis
kubectl create deployment hello-fastapi-kube --image=chanyanhon/fastapi-redis
kubectl expose deployment hello-fastapi-kube --type=LoadBalancer --port=8000
kubectl get service hello-fastapi-kube
minikube service hello-fastapi-kube --url 

kubectl delete services --all
kubectl delete deployments --all
minikube stop

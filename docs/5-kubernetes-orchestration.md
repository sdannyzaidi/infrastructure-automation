# 5. Kubernetes - Container Orchestration

## 🎯 Learning Objectives
- Understand Kubernetes architecture and concepts
- Deploy applications using pods, services, and deployments
- Manage configuration with ConfigMaps and Secrets
- Implement ingress controllers and networking
- Set up monitoring and logging

## 📚 Key Concepts
- **Pods**: Smallest deployable units
- **Services**: Network abstraction for pods
- **Deployments**: Manage replica sets and rolling updates
- **ConfigMaps/Secrets**: Configuration management
- **Ingress**: HTTP/HTTPS routing
- **Namespaces**: Resource isolation

## 🏗️ Project Structure
```
kubernetes/
├── 01-basics/              # Basic pod and service definitions
├── 02-deployments/         # Deployment configurations
├── 03-services/            # Service definitions
├── 04-ingress/             # Ingress controllers
├── 05-monitoring/          # Monitoring stack
└── manifests/              # Complete application manifests
```

## 🚀 Getting Started

### Prerequisites
```bash
# Install kubectl
brew install kubectl  # macOS
# or download from https://kubernetes.io/docs/tasks/tools/

# Install minikube for local development
brew install minikube  # macOS

# Start local cluster
minikube start

# Verify cluster
kubectl cluster-info
kubectl get nodes

# Enable ingress addon
minikube addons enable ingress
```

### Step 1: Basic Pods and Services
```bash
cd kubernetes/01-basics

# Create basic pod manifest
touch pod.yaml

# Create service manifest
touch service.yaml

# Your pod should include:
# - Container specification
# - Resource limits
# - Health checks
# - Labels for service selection
```

### Step 2: Deployments
```bash
cd ../02-deployments

# Create deployment manifest
touch deployment.yaml

# Your deployment should include:
# - Replica count
# - Rolling update strategy
# - Pod template
# - Resource requests/limits
# - Readiness/liveness probes
```

### Step 3: Services and Networking
```bash
cd ../03-services

# Create different service types:
touch clusterip-service.yaml    # Internal communication
touch nodeport-service.yaml     # External access via node port
touch loadbalancer-service.yaml # Cloud load balancer

# Each service should demonstrate:
# - Port mapping
# - Selector configuration
# - Service discovery
```

### Step 4: Ingress Configuration
```bash
cd ../04-ingress

# Create ingress manifest
touch ingress.yaml

# Configure ingress for:
# - HTTP routing
# - Host-based routing
# - Path-based routing
# - TLS termination (optional)
```

### Step 5: Complete Application
```bash
cd ../manifests

# Create complete application stack:
touch web-app-deployment.yaml
touch web-app-service.yaml
touch web-app-configmap.yaml
touch web-app-secret.yaml
touch web-app-ingress.yaml
```

## 📝 Core Exercises

### Exercise 1: Deploy Your First Pod
```bash
cd kubernetes/01-basics

# Apply pod manifest
kubectl apply -f pod.yaml

# Check pod status
kubectl get pods
kubectl describe pod <pod-name>

# Access pod logs
kubectl logs <pod-name>

# Execute commands in pod
kubectl exec -it <pod-name> -- /bin/bash
```

### Exercise 2: Scale with Deployments
```bash
cd ../02-deployments

# Deploy application
kubectl apply -f deployment.yaml

# Scale deployment
kubectl scale deployment web-app --replicas=3

# Check rollout status
kubectl rollout status deployment/web-app

# Update deployment (rolling update)
kubectl set image deployment/web-app container=new-image:tag

# Rollback deployment
kubectl rollout undo deployment/web-app
```

### Exercise 3: Service Discovery
```bash
cd ../03-services

# Create services
kubectl apply -f clusterip-service.yaml
kubectl apply -f nodeport-service.yaml

# Test service connectivity
kubectl get services
kubectl get endpoints

# Access service from within cluster
kubectl run test-pod --image=busybox --rm -it -- /bin/sh
# Inside pod: wget -qO- http://web-app-service:80
```

### Exercise 4: Ingress Setup
```bash
cd ../04-ingress

# Apply ingress
kubectl apply -f ingress.yaml

# Check ingress status
kubectl get ingress
kubectl describe ingress web-app-ingress

# Test external access
curl -H "Host: myapp.local" http://$(minikube ip)
```

### Exercise 5: Configuration Management
```bash
cd ../manifests

# Create ConfigMap and Secret
kubectl apply -f web-app-configmap.yaml
kubectl apply -f web-app-secret.yaml

# Deploy application with configuration
kubectl apply -f web-app-deployment.yaml

# Verify configuration is mounted
kubectl exec -it <pod-name> -- env | grep CONFIG
```

## 🔧 Essential Commands

### Cluster Management
```bash
# Cluster information
kubectl cluster-info
kubectl get nodes
kubectl describe node <node-name>

# Namespace management
kubectl get namespaces
kubectl create namespace development
kubectl config set-context --current --namespace=development
```

### Resource Management
```bash
# Apply manifests
kubectl apply -f manifest.yaml
kubectl apply -f directory/

# Get resources
kubectl get pods
kubectl get services
kubectl get deployments
kubectl get all

# Describe resources
kubectl describe pod <pod-name>
kubectl describe service <service-name>

# Delete resources
kubectl delete -f manifest.yaml
kubectl delete pod <pod-name>
```

### Debugging and Troubleshooting
```bash
# View logs
kubectl logs <pod-name>
kubectl logs -f <pod-name>  # Follow logs
kubectl logs <pod-name> -c <container-name>  # Multi-container pod

# Execute commands
kubectl exec -it <pod-name> -- /bin/bash
kubectl exec <pod-name> -- ps aux

# Port forwarding
kubectl port-forward pod/<pod-name> 8080:80
kubectl port-forward service/<service-name> 8080:80

# Resource usage
kubectl top nodes
kubectl top pods
```

### Configuration and Secrets
```bash
# ConfigMaps
kubectl create configmap app-config --from-file=config.properties
kubectl get configmaps
kubectl describe configmap app-config

# Secrets
kubectl create secret generic app-secret --from-literal=password=secret123
kubectl get secrets
kubectl describe secret app-secret
```

## 🏗️ Best Practices

### Resource Definitions
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
  labels:
    app: web-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: web-app
        image: nginx:1.21
        ports:
        - containerPort: 80
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "128Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 80
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 5
```

### Security Considerations
```yaml
# Security context
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  fsGroup: 2000
  capabilities:
    drop:
    - ALL

# Network policies
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: web-app-netpol
spec:
  podSelector:
    matchLabels:
      app: web-app
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 80
```

## 🐛 Troubleshooting

### Common Issues
```bash
# Pod stuck in Pending
kubectl describe pod <pod-name>
# Check: Resource constraints, node capacity, scheduling issues

# Pod CrashLoopBackOff
kubectl logs <pod-name> --previous
# Check: Application errors, health check failures, resource limits

# Service not accessible
kubectl get endpoints <service-name>
# Check: Service selector, pod labels, port configuration

# Ingress not working
kubectl describe ingress <ingress-name>
# Check: Ingress controller, DNS configuration, backend services
```

### Debugging Techniques
```bash
# Check events
kubectl get events --sort-by=.metadata.creationTimestamp

# Resource usage
kubectl top pods --sort-by=cpu
kubectl top pods --sort-by=memory

# Network connectivity
kubectl run debug --image=busybox --rm -it -- /bin/sh
# Test DNS: nslookup kubernetes.default
# Test connectivity: wget -qO- http://service-name:port

# Check resource quotas
kubectl describe resourcequota
kubectl describe limitrange
```

## 🎯 Learning Outcomes

### Kubernetes Architecture
- **Control plane components**: API server, etcd, scheduler, controller manager
- **Node components**: kubelet, kube-proxy, container runtime
- **Networking**: Pod networking, service discovery, ingress
- **Storage**: Persistent volumes, storage classes

### Application Deployment
- **Workload management**: Pods, deployments, replica sets
- **Service mesh**: Communication between services
- **Configuration**: ConfigMaps, secrets, environment variables
- **Scaling**: Horizontal pod autoscaling, cluster autoscaling

### Operations and Monitoring
- **Health checks**: Liveness and readiness probes
- **Logging**: Centralized log collection
- **Monitoring**: Metrics collection and alerting
- **Troubleshooting**: Debugging techniques and tools

## 📚 Interview Preparation

### Architecture Questions
- "Explain the Kubernetes architecture and main components"
- "What's the difference between a pod and a container?"
- "How does service discovery work in Kubernetes?"
- "Explain the role of etcd in Kubernetes"

### Deployment Scenarios
- "How would you deploy a stateless web application?"
- "What's the difference between Deployment and StatefulSet?"
- "How do you handle rolling updates and rollbacks?"
- "Explain blue-green vs canary deployments"

### Troubleshooting
- "A pod is stuck in Pending state. How do you troubleshoot?"
- "How do you debug networking issues between pods?"
- "What would you check if a service is not accessible?"
- "How do you monitor resource usage in Kubernetes?"

### Security and Best Practices
- "How do you secure a Kubernetes cluster?"
- "What are network policies and when would you use them?"
- "How do you manage secrets in Kubernetes?"
- "Explain RBAC in Kubernetes"

## 🔗 Integration with Other Tools

### With Docker
```bash
# Build and push images
docker build -t myapp:v1.0 .
docker push registry/myapp:v1.0

# Use in Kubernetes
kubectl set image deployment/myapp container=registry/myapp:v1.0
```

### With Terraform
```hcl
# Provision EKS cluster
resource "aws_eks_cluster" "main" {
  name     = "my-cluster"
  role_arn = aws_iam_role.cluster.arn
  # ... configuration
}
```

### With CI/CD
```yaml
# Deploy to Kubernetes
- name: Deploy to Kubernetes
  run: |
    kubectl apply -f k8s/
    kubectl rollout status deployment/web-app
```

## 🚀 Next Steps
After mastering Kubernetes:
1. **CI/CD Pipelines** with Kubernetes deployments (Tutorial 6)
2. **Monitoring** with Prometheus and Grafana on Kubernetes (Tutorial 7)
3. **Advanced Topics**: Service mesh (Istio), GitOps (ArgoCD)
4. **Production**: EKS/GKE cluster management

## 📖 Additional Resources
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Kubernetes Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/)

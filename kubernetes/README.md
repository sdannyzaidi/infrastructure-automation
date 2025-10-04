# Kubernetes - Container Orchestration

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
```

### Basic Commands
```bash
# Apply manifests
kubectl apply -f <file.yaml>

# Get resources
kubectl get pods
kubectl get services
kubectl get deployments

# Describe resources
kubectl describe pod <pod-name>

# View logs
kubectl logs <pod-name>

# Execute commands in pods
kubectl exec -it <pod-name> -- /bin/bash

# Port forwarding
kubectl port-forward <pod-name> 8080:80

# Delete resources
kubectl delete -f <file.yaml>
```

## 📝 Learning Path

### 1. Basic Concepts (Week 1)
- Create your first pod
- Understand services and networking
- Learn about labels and selectors

### 2. Deployments and Scaling (Week 2)
- Deploy applications with Deployments
- Implement rolling updates
- Configure horizontal pod autoscaling

### 3. Configuration Management (Week 3)
- Use ConfigMaps for configuration
- Manage secrets securely
- Mount volumes and persistent storage

### 4. Networking and Ingress (Week 4)
- Set up ingress controllers
- Configure SSL/TLS termination
- Implement network policies

### 5. Monitoring and Logging (Week 5)
- Deploy Prometheus and Grafana
- Set up log aggregation
- Configure alerting

## 🔧 Useful Tools
- **kubectl**: Command-line tool
- **helm**: Package manager
- **k9s**: Terminal UI for Kubernetes
- **lens**: Desktop GUI for Kubernetes

## 📖 Best Practices
1. Use namespaces for organization
2. Set resource limits and requests
3. Implement health checks
4. Use secrets for sensitive data
5. Apply security contexts
6. Tag images with specific versions

## ✅ Completion Checklist
- [ ] Deploy pods and services
- [ ] Create deployments with rolling updates
- [ ] Configure ingress routing
- [ ] Set up monitoring stack
- [ ] Implement persistent storage
- [ ] Apply security best practices

Start with `01-basics/` to begin your Kubernetes journey!

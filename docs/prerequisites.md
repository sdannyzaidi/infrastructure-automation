# Prerequisites and Setup Guide

## Required Tools Installation

### 1. Version Control
```bash
# Git (if not already installed)
# macOS: git --version (should be pre-installed)
# Linux: sudo apt-get install git
# Windows: Download from https://git-scm.com/
```

### 2. Infrastructure as Code
```bash
# Terraform
# macOS
brew install terraform

# Linux
wget https://releases.hashicorp.com/terraform/1.6.0/terraform_1.6.0_linux_amd64.zip
unzip terraform_1.6.0_linux_amd64.zip
sudo mv terraform /usr/local/bin/

# Windows: Download from https://www.terraform.io/downloads
```

### 3. Configuration Management
```bash
# Ansible
# macOS
brew install ansible

# Linux
sudo apt-get update
sudo apt-get install ansible

# Windows: Use WSL2 or Docker
```

### 4. Containerization
```bash
# Docker Desktop
# Download from https://www.docker.com/products/docker-desktop/
# Follow installation instructions for your OS
```

### 5. Kubernetes
```bash
# kubectl
# macOS
brew install kubectl

# Linux
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# minikube (for local cluster)
# macOS
brew install minikube

# Linux
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

### 6. Cloud CLI Tools
```bash
# AWS CLI (optional - for cloud resources)
# macOS
brew install awscli

# Linux
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Google Cloud CLI (optional)
# Follow instructions at https://cloud.google.com/sdk/docs/install
```

### 7. Monitoring Tools
```bash
# Helm (for Kubernetes package management)
# macOS
brew install helm

# Linux
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

## Verification Commands
Run these commands to verify installations:

```bash
# Check versions
git --version
terraform --version
ansible --version
docker --version
kubectl version --client
minikube version
helm version
```

## Cloud Account Setup (Optional)
For cloud resources, you'll need:

### AWS Free Tier
1. Create AWS account at https://aws.amazon.com/
2. Set up IAM user with programmatic access
3. Configure AWS CLI: `aws configure`

### Google Cloud Platform
1. Create GCP account at https://cloud.google.com/
2. Create new project
3. Enable required APIs
4. Set up service account and download credentials

## Development Environment
- **Code Editor**: VS Code with extensions:
  - Terraform
  - Ansible
  - Docker
  - Kubernetes
  - YAML
- **Terminal**: Any modern terminal (iTerm2, Windows Terminal, etc.)

## Next Steps
Once all tools are installed:
1. Verify installations with the commands above
2. Start with the Terraform basics in `/terraform/README.md`
3. Follow the learning path in the main README

## Troubleshooting
- **Permission issues**: Use `sudo` for Linux/macOS installations
- **Path issues**: Ensure tools are in your PATH
- **Docker issues**: Make sure Docker Desktop is running
- **Kubernetes issues**: Start with `minikube start`

For specific issues, check the official documentation for each tool.

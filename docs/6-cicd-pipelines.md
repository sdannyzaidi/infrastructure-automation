# 6. CI/CD Pipelines with GitHub Actions

## 🎯 Learning Objectives
- Understand CI/CD principles and best practices
- Build automated pipelines with GitHub Actions
- Implement testing, security scanning, and deployment
- Configure multi-environment deployments
- Set up monitoring and notifications

## 📚 Key Concepts
- **Continuous Integration**: Automated testing and validation
- **Continuous Deployment**: Automated deployment to environments
- **Pipeline as Code**: Version-controlled pipeline definitions
- **Environment Promotion**: Staging → Production workflow
- **Security Integration**: SAST, DAST, dependency scanning
- **Rollback Strategies**: Automated failure recovery

## 🏗️ Pipeline Architecture
```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Code      │    │     CI      │    │  Staging    │    │ Production  │
│   Commit    │───▶│  Pipeline   │───▶│ Deployment  │───▶│ Deployment  │
│             │    │             │    │             │    │ (Manual)    │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                           │
                   ┌───────▼───────┐
                   │   Security    │
                   │   Scanning    │
                   └───────────────┘
```

## 🚀 Getting Started

### Prerequisites
```bash
# Ensure you have:
# - GitHub repository
# - Docker Hub or GitHub Container Registry account
# - Cloud provider account (AWS/GCP) for deployments
# - Slack workspace (optional, for notifications)

# Repository structure should include:
# - Application code (apps/web-app/)
# - Dockerfile (docker/Dockerfile)
# - Kubernetes manifests (kubernetes/manifests/)
```

### Step 1: Create Workflow Directory
```bash
# Create GitHub Actions workflow directory
mkdir -p .github/workflows

# You'll create these workflow files:
# - ci.yml (main CI pipeline)
# - cd-staging.yml (staging deployment)
# - cd-production.yml (production deployment)
# - security.yml (security scanning)
```

### Step 2: Build CI Pipeline
```bash
# Create .github/workflows/ci.yml
touch .github/workflows/ci.yml

# Your CI pipeline should include:
# 1. Code checkout
# 2. Language/runtime setup
# 3. Dependency installation
# 4. Code linting and formatting
# 5. Unit tests execution
# 6. Code coverage reporting
# 7. Docker image building
# 8. Security scanning
```

### Step 3: Create Deployment Pipelines
```bash
# Create staging deployment
touch .github/workflows/cd-staging.yml

# Create production deployment
touch .github/workflows/cd-production.yml

# Each deployment should include:
# 1. Environment-specific configuration
# 2. Infrastructure validation
# 3. Application deployment
# 4. Health checks
# 5. Rollback on failure
```

### Step 4: Security Integration
```bash
# Create security scanning workflow
touch .github/workflows/security.yml

# Include security checks:
# 1. Static Application Security Testing (SAST)
# 2. Dependency vulnerability scanning
# 3. Container image scanning
# 4. Infrastructure security validation
```

## 📝 Core Exercises

### Exercise 1: Basic CI Pipeline
```yaml
# .github/workflows/ci.yml structure:
name: CI Pipeline
on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      # Add your CI steps here
```

### Exercise 2: Docker Integration
```yaml
# Add Docker build and push to CI:
build:
  needs: test
  runs-on: ubuntu-latest
  steps:
    - name: Build Docker image
      # Implement Docker build
    - name: Push to registry
      # Implement image push
```

### Exercise 3: Multi-Environment Deployment
```yaml
# Staging deployment (automatic):
deploy-staging:
  if: github.ref == 'refs/heads/develop'
  needs: [test, build]
  environment: staging
  # Add deployment steps

# Production deployment (manual approval):
deploy-production:
  if: github.ref == 'refs/heads/main'
  needs: [test, build]
  environment: production
  # Add deployment steps with approval
```

### Exercise 4: Security Scanning
```yaml
# Security workflow:
security:
  runs-on: ubuntu-latest
  steps:
    - name: Run SAST scan
      # Implement static analysis
    - name: Dependency scan
      # Implement dependency checking
    - name: Container scan
      # Implement image scanning
```

### Exercise 5: Notifications and Monitoring
```yaml
# Add notification steps:
notify:
  if: failure()
  runs-on: ubuntu-latest
  steps:
    - name: Slack notification
      # Implement Slack notification
    - name: Email notification
      # Implement email notification
```

## 🔧 Essential Workflow Components

### Triggers and Events
```yaml
# Various trigger types:
on:
  push:
    branches: [ main, develop ]
    paths: [ 'apps/**', 'docker/**' ]
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM
  workflow_dispatch:     # Manual trigger
```

### Environment Management
```yaml
# Environment configuration:
environment:
  name: production
  url: https://myapp.com
  
# Environment variables:
env:
  NODE_ENV: production
  DATABASE_URL: ${{ secrets.DATABASE_URL }}
```

### Conditional Execution
```yaml
# Conditional job execution:
if: github.ref == 'refs/heads/main'
if: contains(github.event.head_commit.message, '[deploy]')
if: success() && github.event_name == 'push'
```

### Matrix Builds
```yaml
# Test multiple versions:
strategy:
  matrix:
    python-version: [3.9, 3.10, 3.11]
    os: [ubuntu-latest, windows-latest, macos-latest]
```

## 🔐 Security and Secrets Management

### Repository Secrets
```bash
# Configure these secrets in GitHub repository settings:
# - DOCKER_USERNAME
# - DOCKER_PASSWORD
# - AWS_ACCESS_KEY_ID
# - AWS_SECRET_ACCESS_KEY
# - KUBECONFIG
# - SLACK_WEBHOOK_URL
```

### Secret Usage in Workflows
```yaml
# Using secrets securely:
- name: Login to Docker Hub
  uses: docker/login-action@v2
  with:
    username: ${{ secrets.DOCKER_USERNAME }}
    password: ${{ secrets.DOCKER_PASSWORD }}

# Environment-specific secrets:
- name: Deploy to production
  env:
    DATABASE_URL: ${{ secrets.PROD_DATABASE_URL }}
    API_KEY: ${{ secrets.PROD_API_KEY }}
```

## 🏗️ Best Practices

### Pipeline Design
```yaml
# Use job dependencies:
jobs:
  test:
    runs-on: ubuntu-latest
  
  build:
    needs: test
    runs-on: ubuntu-latest
  
  deploy:
    needs: [test, build]
    runs-on: ubuntu-latest
```

### Caching and Optimization
```yaml
# Cache dependencies:
- name: Cache dependencies
  uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}

# Use build cache:
- name: Build with cache
  uses: docker/build-push-action@v4
  with:
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

### Error Handling
```yaml
# Continue on error:
continue-on-error: true

# Timeout protection:
timeout-minutes: 30

# Retry on failure:
- name: Deploy with retry
  uses: nick-invision/retry@v2
  with:
    timeout_minutes: 10
    max_attempts: 3
    command: kubectl apply -f k8s/
```

## 🐛 Troubleshooting

### Common Issues
```bash
# Workflow not triggering
# Check: Branch protection rules, file paths, syntax errors

# Permission denied
# Check: Repository secrets, token permissions, GITHUB_TOKEN scope

# Build failures
# Check: Dependencies, environment variables, resource limits

# Deployment failures
# Check: Target environment, credentials, network connectivity
```

### Debugging Techniques
```yaml
# Enable debug logging:
- name: Debug information
  run: |
    echo "GitHub context:"
    echo "${{ toJson(github) }}"
    echo "Environment variables:"
    env

# Step-by-step debugging:
- name: Debug step
  run: |
    set -x  # Enable verbose output
    kubectl get pods
    kubectl describe deployment myapp
```

## 🎯 Learning Outcomes

### CI/CD Principles
- **Automation**: Eliminate manual deployment processes
- **Consistency**: Standardized deployment procedures
- **Reliability**: Automated testing and validation
- **Speed**: Faster time to market
- **Quality**: Continuous feedback and improvement

### GitHub Actions Expertise
- **Workflow design**: Complex pipeline orchestration
- **Action usage**: Leveraging community actions
- **Custom actions**: Building reusable components
- **Security**: Secrets and permissions management
- **Optimization**: Caching and performance tuning

### DevOps Integration
- **Infrastructure as Code**: Terraform integration
- **Container orchestration**: Kubernetes deployments
- **Monitoring**: Automated monitoring setup
- **Security**: Integrated security scanning

## 📚 Interview Preparation

### CI/CD Concepts
- "Explain the difference between CI and CD"
- "What are the benefits of pipeline as code?"
- "How do you handle secrets in CI/CD pipelines?"
- "What's your approach to testing in CI/CD?"

### Pipeline Design
- "How would you design a multi-environment deployment pipeline?"
- "Explain blue-green vs canary deployment strategies"
- "How do you handle rollbacks in automated deployments?"
- "What metrics do you monitor in CI/CD pipelines?"

### Troubleshooting
- "A deployment pipeline is failing intermittently. How do you debug?"
- "How do you handle flaky tests in CI pipelines?"
- "What would you do if a production deployment fails?"

### Security
- "How do you secure CI/CD pipelines?"
- "What security scans do you include in pipelines?"
- "How do you manage credentials across environments?"

## 🔗 Integration Examples

### With Kubernetes
```yaml
- name: Deploy to Kubernetes
  run: |
    kubectl apply -f k8s/
    kubectl rollout status deployment/web-app
    kubectl get services
```

### With Terraform
```yaml
- name: Terraform Plan
  run: |
    terraform init
    terraform plan -out=tfplan
    
- name: Terraform Apply
  if: github.ref == 'refs/heads/main'
  run: terraform apply tfplan
```

### With Monitoring
```yaml
- name: Update monitoring
  run: |
    # Update Grafana dashboards
    # Configure alerts
    # Send deployment notification
```

## 🚀 Advanced Topics

### GitOps Integration
```yaml
# Update GitOps repository:
- name: Update GitOps repo
  run: |
    git clone https://github.com/org/gitops-repo
    cd gitops-repo
    yq e '.image.tag = "${{ github.sha }}"' -i apps/web-app/values.yaml
    git commit -am "Update web-app to ${{ github.sha }}"
    git push
```

### Multi-Cloud Deployments
```yaml
# Deploy to multiple clouds:
deploy-aws:
  runs-on: ubuntu-latest
  steps:
    - name: Deploy to EKS
      # AWS deployment steps

deploy-gcp:
  runs-on: ubuntu-latest
  steps:
    - name: Deploy to GKE
      # GCP deployment steps
```

## 🔗 Next Steps
After mastering CI/CD:
1. **Monitoring and Observability** setup (Tutorial 7)
2. **Advanced GitOps** with ArgoCD
3. **Multi-cloud deployments**
4. **Advanced security** with policy as code

## 📖 Additional Resources
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Awesome Actions](https://github.com/sdras/awesome-actions) - Community actions
- [CI/CD Best Practices](https://docs.github.com/en/actions/learn-github-actions/security-hardening-for-github-actions)
- [GitOps Principles](https://www.gitops.tech/)

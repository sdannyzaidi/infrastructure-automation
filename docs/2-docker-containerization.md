# 2. Docker Tutorial - Containerization and Orchestration

## 🎯 What You'll Learn
This tutorial will teach you containerization and orchestration fundamentals through hands-on practice. You'll learn to:

- **Build multi-stage Docker images** with security best practices
- **Orchestrate multiple services** with Docker Compose
- **Implement service networking** and dependencies
- **Integrate monitoring** with Prometheus and Grafana
- **Configure reverse proxies** with Nginx
- **Apply container security** best practices

## 🏗️ Architecture You'll Build
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│     Nginx       │    │    Web App      │    │     Redis       │
│  (Port 80)      │───▶│  (Port 4000)    │───▶│  (Port 6379)    │
│ Reverse Proxy   │    │   Flask App     │    │    Cache        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
         ┌─────────────────┐     │    ┌─────────────────┐
         │   Prometheus    │     │    │    Grafana      │
         │  (Port 9090)    │◀─── ┘───▶│  (Port 3000)    │
         │ Metrics Store   │          │  Dashboards     │
         └─────────────────┘          └─────────────────┘
```

## 🚀 Step-by-Step Tutorial

### Prerequisites
```bash
# Verify Docker is installed and running
docker --version
docker-compose --version

# Make sure you're in the docker directory
cd /path/to/infrastructure-automation/docker
```

### Step 1: Create the Dockerfile
```bash
# Create a multi-stage Dockerfile for the Flask app
touch Dockerfile

# Your Dockerfile should include:
# - Multi-stage build (builder + production)
# - Security best practices (non-root user)
# - Minimal base image (python:3.11-slim)
# - Health checks
# - Proper file permissions
```

### Step 2: Build the Application Container
```bash
# Build the Docker image from the parent directory
cd ..
docker build -f docker/Dockerfile -t infrastructure-learning-app .

# Verify the image was created
docker images | grep infrastructure-learning-app
```

### Step 3: Test Single Container
```bash
# Run just the web application
docker run -p 4000:4000 --name test-app infrastructure-learning-app

# In another terminal, test the application
curl http://localhost:4000/health

# Stop and remove the test container
docker stop test-app
docker rm test-app
```

### Step 4: Create Docker Compose Configuration
```bash
# Navigate back to docker directory
cd docker

# Create docker-compose.yml with these services:
# - web-app (your Flask application)
# - nginx (reverse proxy)
# - redis (caching)
# - prometheus (metrics collection)
# - grafana (visualization)
```

### Step 5: Create Nginx Configuration
```bash
# Create nginx.conf for reverse proxy
touch nginx.conf

# Configure Nginx to:
# - Proxy requests to Flask app
# - Serve static files
# - Add security headers
# - Enable gzip compression
```

### Step 6: Create Prometheus Configuration
```bash
# Create prometheus.yml for metrics collection
touch prometheus.yml

# Configure Prometheus to scrape:
# - Web application metrics (/metrics)
# - Node exporter metrics
# - Container metrics
```

### Step 7: Launch the Full Stack
```bash
# Start all services in background
docker-compose up -d

# Watch the logs as services start
docker-compose logs -f

# Check that all services are running
docker-compose ps
```

### Step 8: Explore Your Services
Open these URLs in your browser:
- **Web Application**: http://localhost:80 (via Nginx)
- **Direct App Access**: http://localhost:4000
- **Grafana Dashboard**: http://localhost:3000 (admin/admin123)
- **Prometheus Metrics**: http://localhost:9090
- **Redis**: Use `redis-cli -p 6379` to connect

### Step 9: Monitor and Debug
```bash
# View logs for specific services
docker-compose logs web-app
docker-compose logs nginx
docker-compose logs prometheus

# Execute commands inside containers
docker-compose exec web-app /bin/bash
docker-compose exec redis redis-cli

# Restart a service
docker-compose restart web-app
```

### Step 10: Cleanup
```bash
# Stop all services
docker-compose down

# Stop and remove volumes (removes all data!)
docker-compose down -v

# Clean up unused Docker resources
docker system prune -f
```

## 📁 File Structure
```
docker/
├── README.md              # This file
├── Dockerfile             # Multi-stage app container (you create)
├── docker-compose.yml     # Service orchestration (you create)
├── nginx.conf            # Nginx configuration (you create)
└── prometheus.yml        # Prometheus config (you create)
```

## 🔧 Key Docker Concepts You'll Learn

### 1. Multi-Stage Builds
Your Dockerfile should demonstrate:
- **Builder stage**: How dependencies are compiled
- **Production stage**: How minimal runtime images are created
- **Benefits**: Why this approach creates smaller, more secure images

### 2. Security Best Practices
Implement these security features:
- **Non-root user**: Why containers shouldn't run as root
- **Minimal base image**: Using `python:3.11-slim` instead of full OS
- **Health checks**: How Docker monitors container health
- **File permissions**: Proper ownership and access controls

### 3. Service Orchestration
Your docker-compose.yml should show:
- **Networks**: How services communicate via `app-network`
- **Dependencies**: How `depends_on` controls startup order
- **Volumes**: How data persists between container restarts
- **Environment variables**: How configuration is managed

## 📊 Monitoring You'll Implement

### Prometheus Integration
- Scrape metrics from Flask app `/metrics` endpoint
- Collect system metrics with node-exporter
- Monitor container metrics with cAdvisor
- Store time-series data for analysis

### Grafana Dashboards
- Visualize application performance
- Monitor system resources
- Create custom dashboards
- Set up alerting rules

### Nginx Reverse Proxy
- Load balance requests
- Terminate SSL (in production)
- Add security headers
- Serve static content

## 🐛 Troubleshooting

### Common Issues
```bash
# Port conflicts
# Solution: Change ports in docker-compose.yml
ports:
  - "8080:80"  # Use 8080 instead of 80

# Permission denied
# Solution: Check Docker daemon is running
sudo systemctl start docker

# Build failures
# Solution: Check Dockerfile syntax
docker build --no-cache -f docker/Dockerfile .

# Service won't start
# Solution: Check logs
docker-compose logs service-name
```

### Debugging Commands
```bash
# Check container status
docker-compose ps

# View all logs
docker-compose logs

# Enter container for debugging
docker-compose exec web-app /bin/bash

# Check network connectivity
docker-compose exec web-app ping redis

# Monitor resource usage
docker stats
```

## 🎯 Learning Outcomes

### Docker Skills
- **Image building**: Multi-stage Dockerfiles
- **Container orchestration**: Docker Compose
- **Networking**: Service discovery and communication
- **Volume management**: Data persistence
- **Security**: Best practices for production

### DevOps Skills
- **Service architecture**: Microservices design
- **Reverse proxies**: Load balancing and routing
- **Monitoring integration**: Metrics and observability
- **Configuration management**: Environment-based configs

### Production Readiness
- **Health checks**: Container health monitoring
- **Logging**: Centralized log collection
- **Scaling**: Horizontal service scaling
- **Security**: Container security hardening

## 🚀 Advanced Exercises

### Experiment with the Setup
```bash
# Try scaling services
docker-compose up -d --scale web-app=3

# Monitor resource usage
docker stats

# Test service resilience
docker-compose stop web-app
# Watch how the system behaves, then restart
docker-compose start web-app
```

### Extend the Configuration
1. **Add environment-specific configs** (dev/staging/prod)
2. **Implement secrets management** with Docker secrets
3. **Create custom Grafana dashboards** for your metrics
4. **Add log aggregation** with ELK stack integration

## 📚 Interview Preparation
After completing this tutorial, you'll be able to discuss:

**Container Concepts:**
- "What are the benefits of multi-stage Docker builds?"
- "How do you secure Docker containers?"
- "Explain Docker networking and service discovery"

**Orchestration:**
- "How does Docker Compose handle service dependencies?"
- "What's the difference between Docker Compose and Kubernetes?"
- "How do you scale services with Docker Compose?"

**Monitoring:**
- "How do you monitor containerized applications?"
- "What metrics are important for container health?"
- "How do you implement centralized logging?"

## 🔗 Next Steps
After mastering Docker:
1. **Infrastructure as Code** with Terraform (Tutorial 3)
2. **Configuration Management** with Ansible (Tutorial 4)
3. **Container Orchestration** with Kubernetes (Tutorial 5)
4. **CI/CD Pipelines** with GitHub Actions (Tutorial 6)

# Docker Tutorial - Containerization and Orchestration

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

### Step 1: Build the Application Container
```bash
# Build the Docker image from the parent directory
cd ..
docker build -f docker/Dockerfile -t infrastructure-learning-app .

# Verify the image was created
docker images | grep infrastructure-learning-app
```

### Step 2: Test Single Container
```bash
# Run just the web application
docker run -p 4000:4000 --name test-app infrastructure-learning-app

# In another terminal, test the application
curl http://localhost:4000/health

# Stop and remove the test container
docker stop test-app
docker rm test-app
```

### Step 3: Launch the Full Stack
```bash
# Navigate back to docker directory
cd docker

# Start all services in background
docker-compose up -d

# Watch the logs as services start
docker-compose logs -f

# Check that all services are running
docker-compose ps
```

### Step 4: Explore Your Services
Open these URLs in your browser:
- **Web Application**: http://localhost:80 (via Nginx)
- **Direct App Access**: http://localhost:4000
- **Grafana Dashboard**: http://localhost:3000 (admin/admin123)
- **Prometheus Metrics**: http://localhost:9090
- **Redis**: Use `redis-cli -p 6379` to connect

### Step 5: Monitor and Debug
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

### Step 6: Cleanup
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
├── Dockerfile             # Multi-stage app container
├── docker-compose.yml     # Service orchestration
├── nginx.conf            # Nginx configuration (to be created)
└── prometheus.yml        # Prometheus config (to be created)
```

## 🔧 Key Docker Concepts You'll Learn

### 1. Multi-Stage Builds
Examine the `Dockerfile` to understand:
- **Builder stage**: How dependencies are compiled
- **Production stage**: How minimal runtime images are created
- **Benefits**: Why this approach creates smaller, more secure images

### 2. Security Best Practices
Look for these security features in the Dockerfile:
- **Non-root user**: Why containers shouldn't run as root
- **Minimal base image**: Using `python:3.11-slim` instead of full OS
- **Health checks**: How Docker monitors container health
- **File permissions**: Proper ownership and access controls

### 3. Service Orchestration
Study the `docker-compose.yml` to learn:
- **Networks**: How services communicate via `app-network`
- **Dependencies**: How `depends_on` controls startup order
- **Volumes**: How data persists between container restarts
- **Environment variables**: How configuration is managed

## 📊 Monitoring You'll Implement

### Prometheus Metrics Collection
Your app will expose metrics at `/metrics` endpoint:
- HTTP request counts and response times
- System resource usage (CPU, memory)
- Custom business metrics

### Grafana Visualization
You'll access dashboards at http://localhost:3000:
- Default credentials: `admin` / `admin123`
- Pre-configured data sources
- Custom dashboard creation

## 🐛 Troubleshooting

### Common Issues
```bash
# Check if services are running
docker-compose ps

# View service logs
docker-compose logs web-app
docker-compose logs nginx

# Restart a specific service
docker-compose restart web-app

# Check port conflicts
netstat -tulpn | grep :4000
```

### Port Conflicts
If you get port conflicts:
1. Change ports in `docker-compose.yml`
2. Update health check URLs accordingly
3. Restart with `docker-compose up -d`

### Container Won't Start
```bash
# Check container logs
docker-compose logs <service-name>

# Inspect container
docker inspect <container-name>

# Execute into running container
docker-compose exec web-app /bin/bash
```

## 🎯 Learning Outcomes
After completing this tutorial, you will understand:

### Technical Skills You'll Gain
- **Containerization**: How to build efficient, secure Docker images
- **Orchestration**: How to manage multi-service applications
- **Networking**: How containers communicate with each other
- **Monitoring**: How to collect metrics and create visualizations
- **Security**: How to apply container security best practices

### SRE/DevOps Concepts You'll Master
- **Infrastructure as Code**: Writing declarative service definitions
- **Service Discovery**: Understanding how services find each other
- **Health Checks**: Implementing automated service monitoring
- **Observability**: Setting up metrics, logs, and tracing
- **Scalability**: Learning horizontal scaling patterns

## 🚀 What to Try Next

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

1. **"How do you containerize applications?"**
   - Explain multi-stage builds and their benefits
   - Discuss security considerations like non-root users
   - Describe health check implementation

2. **"How do you orchestrate multiple services?"**
   - Demonstrate Docker Compose usage
   - Explain service dependencies and networking
   - Show volume management for data persistence

3. **"How do you monitor containerized applications?"**
   - Walk through Prometheus metrics collection
   - Show Grafana dashboard creation
   - Explain health check strategies

## 🎉 Completion
Once you've successfully run through all the steps, you'll have:
- A working containerized application stack
- Hands-on experience with Docker and Docker Compose
- Understanding of monitoring and observability
- Real-world skills applicable to SRE/DevOps roles

**Ready for the next challenge?** Consider these follow-up tutorials:
- **Kubernetes** - Scale your containers across clusters
- **Terraform** - Provision cloud infrastructure as code
- **CI/CD** - Automate your deployment pipeline

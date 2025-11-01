# 1. Web Application Tutorial - Flask with Monitoring

## 🎯 What You'll Learn
This tutorial will teach you how to build and run a production-ready Flask web application with monitoring capabilities. You'll learn to:

- **Set up Python virtual environments** for isolated development
- **Build a Flask web application** with health checks and metrics
- **Implement Prometheus metrics** for monitoring
- **Add system monitoring** with resource usage tracking
- **Create proper logging** for debugging and observability
- **Run applications locally** for development and testing

## 🏗️ Application Features
This Flask app includes:
- **Health check endpoint** (`/health`) for load balancers
- **Prometheus metrics** (`/metrics`) for monitoring
- **System information** (`/system`) for resource tracking
- **Application info** (`/info`) for version and status
- **Web interface** (`/`) with service overview
- **Request logging** and performance tracking

## 🚀 Step-by-Step Tutorial

### Prerequisites
```bash
# Verify Python 3.11+ is installed
python3 --version

# Verify pip is available
python3 -m pip --version

# Make sure you're in the web-app directory
cd /path/to/infrastructure-automation/apps/web-app
```

### Step 1: Create Virtual Environment
```bash
# Create a new virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate

# Verify you're in the virtual environment (should show venv path)
which python
```

### Step 2: Create Requirements File
```bash
# Create requirements.txt with these dependencies:
cat > requirements.txt << EOF
Flask==2.3.3
prometheus-client==0.17.1
psutil==5.9.5
gunicorn==21.2.0
EOF

# Install dependencies
pip install -r requirements.txt

# Verify installation
pip list
```

### Step 3: Build the Flask Application
```bash
# Create the main application file
touch app.py

# You'll implement the Flask app with:
# - Health check endpoint (/health)
# - Metrics endpoint (/metrics) 
# - System info endpoint (/system)
# - Main web interface (/)
# - Proper logging and error handling
```

### Step 4: Implement Core Features
Your Flask application should include:

**Health Check Endpoint**
- Returns JSON with service status
- Used by load balancers and monitoring

**Metrics Endpoint**
- Prometheus-compatible metrics
- Request counters and histograms
- Custom application metrics

**System Information**
- CPU usage percentage
- Memory usage and availability
- Disk space utilization

### Step 5: Test Your Application
```bash
# Run the application
python app.py

# Test endpoints in another terminal
curl http://localhost:4000/health
curl http://localhost:4000/metrics
curl http://localhost:4000/system
curl http://localhost:4000/info

# Open web interface
open http://localhost:4000
```

### Step 6: Development and Debugging
```bash
# Edit the app.py file to add new endpoints
# Add custom metrics or modify existing ones
# Change the HTML template in the home() function

# Restart the application to see changes
# Press Ctrl+C to stop, then run again:
python app.py
```

### Step 7: Production Mode
```bash
# Install gunicorn for production serving
pip install gunicorn

# Run with gunicorn (production WSGI server)
gunicorn --bind 0.0.0.0:4000 --workers 2 app:app

# Test production mode
curl http://localhost:4000/health
```

### Step 8: Cleanup
```bash
# Stop the application (Ctrl+C)

# Deactivate virtual environment
deactivate

# Optional: Remove virtual environment
rm -rf venv
```

## 🔧 Configuration Options

### Environment Variables
You can customize the application behavior:
```bash
# Change the port (default: 4000)
export PORT="8080"

# Enable debug mode
export DEBUG="true"

# Set application name
export APP_NAME="My Flask App"

# Run with custom config
python app.py
```

### Application Structure
```
apps/web-app/
├── app.py              # Main Flask application (you create this)
├── requirements.txt    # Python dependencies (you create this)
├── venv/              # Virtual environment
└── README.md          # This documentation
```

## 📊 Monitoring Integration

### Health Checks
The `/health` endpoint returns:
- Service status (healthy/unhealthy)
- Uptime information
- Basic system metrics
- JSON format for automation

### Prometheus Metrics
The `/metrics` endpoint exposes:
- HTTP request counts by method and status
- Request duration histograms
- Custom application metrics
- Standard Prometheus format

### System Information
The `/system` endpoint shows:
- CPU usage percentage
- Memory usage and availability
- Disk space utilization
- Real-time system metrics

## 🐛 Troubleshooting

### Common Issues
```bash
# Port already in use
# Solution: Use a different port
export PORT="8080"
python app.py

# Module not found errors
# Solution: Ensure virtual environment is activated
source venv/bin/activate
pip install -r requirements.txt

# Permission denied
# Solution: Check file permissions
chmod +x app.py

# Import errors
# Solution: Verify all dependencies are installed
pip install -r requirements.txt
```

### Debugging
```bash
# Enable debug mode for detailed error messages
export DEBUG="true"
python app.py

# Check application logs
# Logs appear in the terminal where you ran the app

# Test specific endpoints
curl -v http://localhost:4000/health
```

## 🎯 Learning Outcomes
After completing this tutorial, you will understand:

### Python Development Skills
- **Virtual environments**: Isolated Python environments
- **Dependency management**: Using pip and requirements.txt
- **Flask framework**: Building web applications
- **Environment configuration**: Using environment variables

### SRE/DevOps Skills
- **Health checks**: Implementing service health endpoints
- **Metrics collection**: Exposing Prometheus metrics
- **System monitoring**: Tracking resource usage
- **Production deployment**: Using WSGI servers like Gunicorn

### Best Practices
- **Code organization**: Structuring Flask applications
- **Error handling**: Proper exception management
- **Logging**: Application observability
- **Security**: Basic security considerations

## 🚀 Next Steps
After mastering this web application:
1. **Containerize** it with Docker (Tutorial 2)
2. **Deploy** it with Kubernetes (Tutorial 5)
3. **Monitor** it with Prometheus/Grafana (Tutorial 7)
4. **Automate** deployment with CI/CD (Tutorial 6)

## 📚 Interview Preparation
This tutorial prepares you for SRE interview questions about:
- Building monitoring-ready applications
- Implementing health checks and metrics
- Python web development
- Production deployment considerations
- Troubleshooting application issues

**Key Interview Topics:**
- "How do you make an application observable?"
- "What metrics would you expose for a web service?"
- "How do you implement health checks?"
- "What's the difference between development and production deployment?"

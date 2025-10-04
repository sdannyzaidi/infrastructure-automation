# Web Application Tutorial - Flask with Monitoring

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

### Step 2: Install Dependencies
```bash
# Upgrade pip to latest version
python -m pip install --upgrade pip

# Install application dependencies
pip install -r requirements.txt

# Verify installations
pip list
```

### Step 3: Run the Application
```bash
# Run with default settings (development mode)
python app.py

# Or run with custom configuration
export APP_NAME="my-learning-app"
export APP_VERSION="1.0.0"
export ENVIRONMENT="development"
export DEBUG="true"
python app.py
```

### Step 4: Test the Application
Open these URLs in your browser or use curl:

```bash
# Main application page
curl http://localhost:4000/
# or visit: http://localhost:4000

# Health check (for monitoring)
curl http://localhost:4000/health

# Application information
curl http://localhost:4000/info

# System metrics
curl http://localhost:4000/system

# Prometheus metrics
curl http://localhost:4000/metrics
```

### Step 5: Explore the Code
Study these key files to understand the implementation:

```bash
# View the main application code
cat app.py

# Check the dependencies
cat requirements.txt

# Look at the application structure
ls -la
```

### Step 6: Customize and Experiment
Try modifying the application:

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
# Application settings
export APP_NAME="your-app-name"
export APP_VERSION="2.0.0"
export ENVIRONMENT="production"

# Server settings
export HOST="0.0.0.0"        # Listen on all interfaces
export PORT="8080"           # Custom port
export DEBUG="false"         # Disable debug mode

# Run with custom settings
python app.py
```

### Development vs Production
```bash
# Development mode (auto-reload, debug info)
export DEBUG="true"
python app.py

# Production mode (stable, optimized)
export DEBUG="false"
gunicorn --bind 0.0.0.0:4000 app:app
```

## 📊 Understanding the Monitoring Features

### Health Checks
The `/health` endpoint provides:
- Service status (healthy/unhealthy)
- Uptime information
- Version details
- Timestamp for monitoring

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

### Monitoring and Observability
- **Health checks**: Implementing service health endpoints
- **Metrics collection**: Exposing Prometheus metrics
- **System monitoring**: Tracking resource usage
- **Logging**: Structured application logging

### Production Readiness
- **WSGI servers**: Using gunicorn for production
- **Configuration management**: Environment-based config
- **Security considerations**: Non-root execution
- **Performance monitoring**: Request tracking and timing

## 📚 Interview Preparation
After completing this tutorial, you'll be able to discuss:

1. **"How do you build production-ready web applications?"**
   - Explain Flask application structure
   - Discuss health checks and monitoring
   - Show configuration management

2. **"How do you implement application monitoring?"**
   - Demonstrate Prometheus metrics integration
   - Explain health check endpoints
   - Show system resource monitoring

3. **"How do you manage Python dependencies?"**
   - Walk through virtual environment setup
   - Explain requirements.txt usage
   - Discuss development vs production environments

## 🚀 What's Next?
Once you've mastered running the app locally:

1. **Containerize it** - Use the Docker tutorial to containerize this app
2. **Deploy to Kubernetes** - Scale it across multiple containers
3. **Add CI/CD** - Automate testing and deployment
4. **Enhance monitoring** - Add more custom metrics and dashboards

## 🎉 Completion
You now have a solid foundation in:
- Python web application development
- Local development environment setup
- Application monitoring and observability
- Production deployment considerations

This knowledge directly applies to SRE/DevOps roles where you'll work with applications and their operational requirements!

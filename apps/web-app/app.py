#!/usr/bin/env python3
"""
Simple Flask web application for demonstrating CI/CD and monitoring
This app provides health checks, metrics, and basic functionality
"""

from flask import Flask, jsonify, request, render_template_string
import os
import time
import logging
import psutil
from datetime import datetime
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)

# Record start time (needed for uptime calculations)
app.start_time = time.time()

# Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint', 'status'])
REQUEST_DURATION = Histogram('http_request_duration_seconds', 'HTTP request duration')
ACTIVE_USERS = Counter('active_users_total', 'Total active users')
CUSTOM_BUSINESS_METRIC = Counter('business_events_total', 'Business events', ['event_type'])

# Application info
APP_VERSION = os.getenv('APP_VERSION', '1.0.0')
APP_NAME = os.getenv('APP_NAME', 'infrastructure-learning-app')

@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    # Record metrics
    duration = time.time() - request.start_time
    REQUEST_DURATION.observe(duration)
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.endpoint or 'unknown',
        status=response.status_code
    ).inc()
    
    # Log request
    logger.info(f"{request.method} {request.path} - {response.status_code} - {duration:.3f}s")
    return response

@app.route('/')
def home():
    """Home page with application info"""
    # Simulate business metric
    ACTIVE_USERS.inc()
    CUSTOM_BUSINESS_METRIC.labels(event_type='page_view').inc()
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>{{ app_name }}</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            .header { color: #333; border-bottom: 2px solid #007acc; padding-bottom: 10px; }
            .info { background: #e7f3ff; padding: 15px; border-radius: 5px; margin: 20px 0; }
            .endpoints { background: #f0f8f0; padding: 15px; border-radius: 5px; }
            a { color: #007acc; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="header">🚀 {{ app_name }}</h1>
            <div class="info">
                <h3>Application Information</h3>
                <p><strong>Version:</strong> {{ version }}</p>
                <p><strong>Environment:</strong> {{ environment }}</p>
                <p><strong>Current Time:</strong> {{ current_time }}</p>
                <p><strong>Uptime:</strong> {{ uptime }} seconds</p>
            </div>
            <div class="endpoints">
                <h3>Available Endpoints</h3>
                <ul>
                    <li><a href="/health">/health</a> - Health check endpoint</li>
                    <li><a href="/info">/info</a> - Application information (JSON)</li>
                    <li><a href="/metrics">/metrics</a> - Prometheus metrics</li>
                    <li><a href="/system">/system</a> - System information</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """
    
    return render_template_string(html_template,
        app_name=APP_NAME,
        version=APP_VERSION,
        environment=os.getenv('ENVIRONMENT', 'development'),
        current_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        uptime=int(time.time() - app.start_time)
    )

@app.route('/health')
def health_check():
    """Health check endpoint for load balancers and monitoring"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': APP_VERSION,
        'uptime_seconds': int(time.time() - app.start_time)
    })

@app.route('/info')
def app_info():
    """Application information endpoint"""
    return jsonify({
        'name': APP_NAME,
        'version': APP_VERSION,
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'python_version': os.sys.version,
        'start_time': datetime.fromtimestamp(app.start_time).isoformat(),
        'uptime_seconds': int(time.time() - app.start_time)
    })

@app.route('/metrics')
def metrics():
    """Prometheus metrics endpoint"""
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/system')
def system_info():
    """System information for monitoring"""
    return jsonify({
        'cpu_percent': psutil.cpu_percent(interval=1),
        'memory': {
            'total': psutil.virtual_memory().total,
            'available': psutil.virtual_memory().available,
            'percent': psutil.virtual_memory().percent
        },
        'disk': {
            'total': psutil.disk_usage('/').total,
            'free': psutil.disk_usage('/').free,
            'percent': psutil.disk_usage('/').percent
        },
        'timestamp': datetime.now().isoformat()
    })

@app.route('/crash')
def crash_app():
    """Endpoint to simulate application crash (for testing)"""
    logger.error("Application crash simulation triggered!")
    CUSTOM_BUSINESS_METRIC.labels(event_type='crash_simulation').inc()
    import sys
    sys.exit(1)  # This will crash the application

@app.route('/slow')
def slow_endpoint():
    """Endpoint that simulates slow response (for testing)"""
    import time
    delay = request.args.get('delay', 5, type=int)
    logger.info(f"Simulating slow response with {delay}s delay")
    CUSTOM_BUSINESS_METRIC.labels(event_type='slow_request').inc()
    time.sleep(delay)
    return jsonify({
        'message': f'This response was delayed by {delay} seconds',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/cpu-load')
def cpu_load():
    """Endpoint that simulates high CPU usage (for testing)"""
    import threading
    import time

    duration = request.args.get('duration', 10, type=int)
    threads = request.args.get('threads', 2, type=int)

    logger.info(f"Simulating CPU load with {threads} threads for {duration}s")
    CUSTOM_BUSINESS_METRIC.labels(event_type='cpu_load_test').inc()

    def cpu_intensive_task():
        end_time = time.time() + duration
        while time.time() < end_time:
            # CPU intensive calculation
            sum(i * i for i in range(1000))

    # Start multiple threads to create CPU load
    threads_list = []
    for i in range(threads):
        t = threading.Thread(target=cpu_intensive_task)
        t.start()
        threads_list.append(t)

    # Wait for all threads to complete
    for t in threads_list:
        t.join()

    return jsonify({
        'message': f'CPU load test completed: {threads} threads for {duration} seconds',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    # Get configuration from environment
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 4000))
    debug = os.getenv('DEBUG', 'false').lower() == 'true'
    
    logger.info(f"Starting {APP_NAME} v{APP_VERSION}")
    logger.info(f"Listening on {host}:{port}")
    
    app.run(host=host, port=port, debug=debug)

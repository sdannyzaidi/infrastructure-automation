# 7. Monitoring and Observability Stack

## 🎯 Learning Objectives
- Implement comprehensive monitoring with Prometheus
- Create dashboards and visualizations with Grafana
- Set up log aggregation with ELK Stack
- Configure alerting and incident response
- Understand SRE monitoring principles

## 📚 Key Components
- **Prometheus**: Metrics collection and storage
- **Grafana**: Visualization and dashboards
- **Elasticsearch**: Log storage and search
- **Logstash**: Log processing pipeline
- **Kibana**: Log visualization
- **AlertManager**: Alert routing and management

## 🏗️ Stack Architecture
```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Application │───▶│ Prometheus  │───▶│   Grafana   │
│  /metrics   │    │   Server    │    │ Dashboards  │
└─────────────┘    └─────────────┘    └─────────────┘
       │                   │                   │
       │            ┌─────────────┐    ┌─────────────┐
       │            │AlertManager │    │    ELK      │
       └───────────▶│   Alerts    │    │    Stack    │
                    └─────────────┘    └─────────────┘
```

## 🚀 Getting Started

### Prerequisites
```bash
# Ensure Docker and Docker Compose are installed
docker --version
docker-compose --version

# Navigate to monitoring directory
cd monitoring

# You'll create these configuration files:
# - docker-compose.yml (orchestration)
# - prometheus/prometheus.yml (metrics config)
# - grafana/provisioning/ (dashboards and datasources)
# - alertmanager/alertmanager.yml (alert routing)
# - elk/ (log processing configuration)
```

### Step 1: Prometheus Configuration
```bash
# Create Prometheus directory and config
mkdir -p prometheus/rules
touch prometheus/prometheus.yml

# Your prometheus.yml should configure:
# - Scrape intervals and targets
# - Service discovery
# - Alert rule files
# - Remote storage (optional)
```

### Step 2: Grafana Setup
```bash
# Create Grafana provisioning directories
mkdir -p grafana/provisioning/datasources
mkdir -p grafana/provisioning/dashboards
mkdir -p grafana/dashboards

# Create datasource configuration
touch grafana/provisioning/datasources/prometheus.yml

# Create dashboard provisioning
touch grafana/provisioning/dashboards/dashboard.yml
```

### Step 3: AlertManager Configuration
```bash
# Create AlertManager directory
mkdir -p alertmanager
touch alertmanager/alertmanager.yml

# Configure alert routing:
# - Notification channels (email, Slack, PagerDuty)
# - Alert grouping and throttling
# - Escalation policies
```

### Step 4: ELK Stack Setup
```bash
# Create ELK directories
mkdir -p elk/elasticsearch
mkdir -p elk/logstash/pipeline
mkdir -p elk/logstash/config
mkdir -p elk/kibana

# Create Logstash pipeline configuration
touch elk/logstash/pipeline/logstash.conf
touch elk/logstash/config/logstash.yml
```

### Step 5: Docker Compose Orchestration
```bash
# Create docker-compose.yml with services:
# - Prometheus (metrics collection)
# - Grafana (visualization)
# - AlertManager (alert handling)
# - Elasticsearch (log storage)
# - Logstash (log processing)
# - Kibana (log visualization)
# - Node Exporter (system metrics)
# - cAdvisor (container metrics)
```

## 📝 Core Exercises

### Exercise 1: Deploy Monitoring Stack
```bash
# Start all monitoring services
docker-compose up -d

# Verify services are running
docker-compose ps

# Check service logs
docker-compose logs prometheus
docker-compose logs grafana

# Access web interfaces
open http://localhost:3000  # Grafana
open http://localhost:9090  # Prometheus
open http://localhost:5601  # Kibana
```

### Exercise 2: Configure Prometheus Targets
```yaml
# Add scrape configurations for:
# - Your web application (/metrics endpoint)
# - Node Exporter (system metrics)
# - cAdvisor (container metrics)
# - Prometheus itself

scrape_configs:
  - job_name: 'web-app'
    static_configs:
      - targets: ['web-app:4000']
    metrics_path: '/metrics'
    scrape_interval: 15s
```

### Exercise 3: Create Grafana Dashboards
```bash
# Create dashboards for:
# 1. Application metrics (requests, latency, errors)
# 2. System metrics (CPU, memory, disk)
# 3. Container metrics (Docker stats)
# 4. Business metrics (custom application metrics)

# Import community dashboards:
# - Node Exporter Full (ID: 1860)
# - Docker Container & Host Metrics (ID: 179)
# - Prometheus Stats (ID: 2)
```

### Exercise 4: Set Up Alerting Rules
```yaml
# Create alert rules for:
# - High error rate
# - High response time
# - Low disk space
# - Service down
# - High memory usage

# Example alert rule:
groups:
  - name: web-app-alerts
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.1
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"
```

### Exercise 5: Configure Log Processing
```bash
# Set up Logstash to process:
# - Application logs
# - System logs
# - Container logs
# - Access logs

# Create Kibana visualizations for:
# - Log volume over time
# - Error log analysis
# - Request patterns
# - Performance metrics from logs
```

## 📊 Monitoring Principles

### The Four Golden Signals
1. **Latency**: Response time of requests
2. **Traffic**: Rate of requests
3. **Errors**: Rate of failed requests
4. **Saturation**: Resource utilization

### SLI/SLO/SLA Framework
```yaml
# Service Level Indicators (SLIs)
- Availability: 99.9% uptime
- Latency: 95% of requests < 200ms
- Error Rate: < 0.1% of requests fail

# Service Level Objectives (SLOs)
- Target: 99.9% availability over 30 days
- Target: 99% of requests complete in < 500ms
- Target: Error rate < 0.01%

# Service Level Agreements (SLAs)
- Contractual commitment: 99.5% uptime
- Penalty: Credits for downtime exceeding SLA
```

### RED Method (for Services)
- **Rate**: Requests per second
- **Errors**: Error rate
- **Duration**: Response time distribution

### USE Method (for Resources)
- **Utilization**: % time resource is busy
- **Saturation**: Queue length or wait time
- **Errors**: Error count

## 🔧 Essential Queries and Dashboards

### Prometheus Queries (PromQL)
```promql
# Request rate
rate(http_requests_total[5m])

# Error rate
rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])

# Response time percentiles
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))

# CPU usage
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Memory usage
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100

# Disk usage
100 - ((node_filesystem_avail_bytes * 100) / node_filesystem_size_bytes)
```

### Grafana Dashboard Panels
```json
# Request Rate Panel
{
  "title": "Request Rate",
  "type": "graph",
  "targets": [
    {
      "expr": "rate(http_requests_total[5m])",
      "legendFormat": "{{method}} {{status}}"
    }
  ]
}

# Error Rate Panel
{
  "title": "Error Rate",
  "type": "singlestat",
  "targets": [
    {
      "expr": "rate(http_requests_total{status=~\"5..\"}[5m]) / rate(http_requests_total[5m]) * 100"
    }
  ]
}
```

## 🚨 Alerting Configuration

### AlertManager Routing
```yaml
# alertmanager.yml
global:
  smtp_smarthost: 'localhost:587'
  smtp_from: 'alerts@company.com'

route:
  group_by: ['alertname']
  group_wait: 10s
  group_interval: 10s
  repeat_interval: 1h
  receiver: 'web.hook'
  routes:
  - match:
      severity: critical
    receiver: 'critical-alerts'

receivers:
- name: 'critical-alerts'
  email_configs:
  - to: 'oncall@company.com'
    subject: 'CRITICAL: {{ .GroupLabels.alertname }}'
  slack_configs:
  - api_url: 'YOUR_SLACK_WEBHOOK_URL'
    channel: '#alerts'
```

### Alert Rules
```yaml
# prometheus/rules/alerts.yml
groups:
- name: infrastructure
  rules:
  - alert: InstanceDown
    expr: up == 0
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "Instance {{ $labels.instance }} down"
      
  - alert: HighCPUUsage
    expr: 100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[2m])) * 100) > 80
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "High CPU usage on {{ $labels.instance }}"
```

## 🐛 Troubleshooting

### Common Issues
```bash
# Prometheus not scraping targets
# Check: Target configuration, network connectivity, /metrics endpoint

# Grafana not showing data
# Check: Datasource configuration, query syntax, time range

# Alerts not firing
# Check: Alert rule syntax, evaluation interval, AlertManager config

# High memory usage
# Check: Retention settings, scrape intervals, cardinality
```

### Debugging Commands
```bash
# Check Prometheus targets
curl http://localhost:9090/api/v1/targets

# Test PromQL queries
curl 'http://localhost:9090/api/v1/query?query=up'

# Check AlertManager status
curl http://localhost:9093/api/v1/status

# View Grafana logs
docker-compose logs grafana

# Check Elasticsearch cluster health
curl http://localhost:9200/_cluster/health
```

## 🎯 Learning Outcomes

### Monitoring Expertise
- **Metrics collection**: Prometheus configuration and PromQL
- **Visualization**: Grafana dashboard creation
- **Alerting**: Alert rule definition and notification routing
- **Log analysis**: ELK stack configuration and log parsing
- **Performance analysis**: Identifying bottlenecks and issues

### SRE Principles
- **Observability**: Three pillars (metrics, logs, traces)
- **SLI/SLO/SLA**: Service level management
- **Error budgets**: Balancing reliability and velocity
- **Incident response**: Alert handling and escalation
- **Capacity planning**: Resource usage analysis

### Operational Skills
- **Troubleshooting**: Using monitoring data for debugging
- **Performance optimization**: Identifying and resolving issues
- **Capacity management**: Scaling decisions based on metrics
- **Security monitoring**: Detecting anomalies and threats

## 📚 Interview Preparation

### Monitoring Concepts
- "Explain the difference between monitoring and observability"
- "What are the four golden signals of monitoring?"
- "How do you design effective alerts?"
- "What's the difference between SLI, SLO, and SLA?"

### Technical Implementation
- "How would you monitor a microservices architecture?"
- "Explain how Prometheus service discovery works"
- "How do you handle high cardinality metrics?"
- "What's your approach to log aggregation and analysis?"

### Operational Scenarios
- "How do you investigate a performance issue using monitoring data?"
- "What metrics would you monitor for a web application?"
- "How do you prevent alert fatigue?"
- "Explain your incident response process"

### Troubleshooting
- "Prometheus is using too much memory. How do you investigate?"
- "Alerts are not firing when they should. How do you debug?"
- "How do you optimize Grafana dashboard performance?"

## 🔗 Integration with Other Tools

### With Kubernetes
```yaml
# ServiceMonitor for Prometheus Operator
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: web-app
spec:
  selector:
    matchLabels:
      app: web-app
  endpoints:
  - port: metrics
```

### With CI/CD
```yaml
# Deploy monitoring configuration
- name: Update monitoring
  run: |
    kubectl apply -f monitoring/k8s/
    # Update Grafana dashboards
    # Configure new alerts
```

### With Infrastructure as Code
```hcl
# Terraform for cloud monitoring
resource "aws_cloudwatch_dashboard" "main" {
  dashboard_name = "MyApp"
  dashboard_body = jsonencode({
    widgets = [
      # Dashboard configuration
    ]
  })
}
```

## 🚀 Advanced Topics

### Distributed Tracing
```bash
# Add Jaeger for distributed tracing
# Instrument applications with OpenTelemetry
# Correlate traces with metrics and logs
```

### Custom Metrics
```python
# Application instrumentation
from prometheus_client import Counter, Histogram, generate_latest

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency')

@REQUEST_LATENCY.time()
def handle_request():
    REQUEST_COUNT.labels(method='GET', endpoint='/api').inc()
    # Handle request
```

### Machine Learning for Monitoring
```bash
# Anomaly detection with Prometheus
# Forecasting with historical data
# Automated alert threshold adjustment
```

## 🔗 Next Steps
After mastering monitoring:
1. **Advanced observability** with distributed tracing
2. **AIOps** and machine learning for monitoring
3. **Chaos engineering** and reliability testing
4. **Multi-cloud monitoring** strategies

## 📖 Additional Resources
- [Prometheus Documentation](https://prometheus.io/docs/)
- [Grafana Documentation](https://grafana.com/docs/)
- [Site Reliability Engineering Book](https://sre.google/sre-book/table-of-contents/)
- [Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)

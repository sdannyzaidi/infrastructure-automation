# CI/CD Pipeline Demo

This directory contains a complete CI/CD pipeline demonstration using GitHub Actions for the Python web application in the `apps/web-app` directory.

## Pipeline Overview

Our CI/CD pipeline includes:

1. **Continuous Integration (CI)**
   - Code linting and formatting checks
   - Unit tests execution
   - Security vulnerability scanning
   - Docker image building and testing

2. **Continuous Deployment (CD)**
   - Automated deployment to staging environment
   - Production deployment with manual approval
   - Rollback capabilities

## Pipeline Structure

```
.github/
└── workflows/
    ├── ci.yml              # Main CI pipeline
    ├── cd-staging.yml      # Staging deployment
    ├── cd-production.yml   # Production deployment
    └── security.yml        # Security scanning
```

## Features Demonstrated

- **Multi-stage pipeline**: Separate CI and CD workflows
- **Environment-specific deployments**: Staging and Production
- **Security scanning**: SAST, dependency scanning
- **Docker integration**: Build, test, and push containers
- **Manual approvals**: Production deployments require approval
- **Notifications**: Slack/email notifications on failures
- **Rollback strategy**: Automated rollback on deployment failures

## Setup Instructions

1. Copy the `.github` directory to your repository root
2. Configure repository secrets (see secrets section below)
3. Enable GitHub Actions in your repository
4. Push changes to trigger the pipeline

## Required Repository Secrets

Configure these secrets in your GitHub repository settings:

### Docker Registry
- `DOCKER_USERNAME`: Docker Hub username
- `DOCKER_PASSWORD`: Docker Hub password/token

### Cloud Provider (AWS example)
- `AWS_ACCESS_KEY_ID`: AWS access key
- `AWS_SECRET_ACCESS_KEY`: AWS secret key
- `AWS_REGION`: AWS region (e.g., us-east-1)

### Notifications
- `SLACK_WEBHOOK_URL`: Slack webhook for notifications
- `NOTIFICATION_EMAIL`: Email for deployment notifications

### Application Secrets
- `DATABASE_URL`: Database connection string
- `SECRET_KEY`: Application secret key
- `API_KEY`: External API keys

## Pipeline Triggers

- **CI Pipeline**: Triggered on every push and pull request
- **Staging Deployment**: Triggered on push to `main` branch
- **Production Deployment**: Triggered manually or on release tags

## Monitoring and Observability

The pipeline includes:
- Build status badges
- Deployment metrics
- Performance testing
- Log aggregation
- Alert notifications

## Best Practices Implemented

1. **Fail Fast**: Early validation and quick feedback
2. **Security First**: Vulnerability scanning at every stage
3. **Environment Parity**: Consistent environments across stages
4. **Automated Testing**: Comprehensive test coverage
5. **Rollback Strategy**: Quick recovery from failures
6. **Monitoring**: Observability throughout the pipeline

## Getting Started

1. Review the workflow files in `.github/workflows/`
2. Customize environment variables and secrets
3. Test the pipeline with a small change
4. Monitor the Actions tab in GitHub for pipeline execution

## Troubleshooting

Common issues and solutions:
- **Failed tests**: Check test logs and fix failing tests
- **Docker build failures**: Verify Dockerfile and dependencies
- **Deployment failures**: Check environment configuration
- **Secret errors**: Ensure all required secrets are configured

For detailed logs, check the Actions tab in your GitHub repository.

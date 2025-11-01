# 3. Terraform - Infrastructure as Code

## 🎯 Learning Objectives
- Understand Infrastructure as Code (IaC) principles
- Learn Terraform syntax and concepts
- Create and manage cloud resources
- Implement best practices for state management
- Use modules for reusable infrastructure

## 📚 Concepts Covered
- Providers and resources
- Variables and outputs
- State management
- Modules and workspaces
- Remote backends

## 🏗️ Project Structure
```
terraform/
├── 01-basics/              # Basic Terraform concepts
├── 02-aws-resources/       # AWS resource creation
├── 03-modules/             # Reusable modules
├── 04-remote-state/        # Remote state management
└── examples/               # Complete examples
```

## 🚀 Getting Started

### Prerequisites
```bash
# Install Terraform
# macOS:
brew install terraform

# Linux:
wget https://releases.hashicorp.com/terraform/1.6.0/terraform_1.6.0_linux_amd64.zip
unzip terraform_1.6.0_linux_amd64.zip
sudo mv terraform /usr/local/bin/

# Verify installation
terraform --version

# Configure AWS credentials (if using AWS)
aws configure
# OR set environment variables:
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_DEFAULT_REGION="us-west-2"
```

### Step 1: Basic Terraform Concepts
Start with the basics in `01-basics/`:

```bash
cd terraform/01-basics

# Create main.tf with:
# - Provider configuration (AWS/GCP)
# - Simple resource (S3 bucket or storage)
# - Variables for customization
# - Outputs for important values

# Create variables.tf with input variables
# Create outputs.tf with output values
# Create terraform.tfvars.example with sample values
```

**Key Files to Create:**
- `main.tf` - Main configuration
- `variables.tf` - Input variables
- `outputs.tf` - Output values
- `terraform.tfvars.example` - Example variables

### Step 2: AWS Resources
Move to `02-aws-resources/`:

```bash
cd ../02-aws-resources

# Create infrastructure for:
# - VPC with public/private subnets
# - Internet Gateway and NAT Gateway
# - Security groups
# - EC2 instances
# - Application Load Balancer
```

**Infrastructure Components:**
- **Networking**: VPC, subnets, gateways
- **Compute**: EC2 instances with user data
- **Security**: Security groups and NACLs
- **Load Balancing**: ALB with target groups

### Step 3: Modules
Learn modularity in `03-modules/`:

```bash
cd ../03-modules

# Create reusable modules:
# - VPC module (networking)
# - Web server module (compute)
# - Database module (RDS)

# Module structure:
# modules/
# ├── vpc/
# │   ├── main.tf
# │   ├── variables.tf
# │   └── outputs.tf
# └── web-server/
#     ├── main.tf
#     ├── variables.tf
#     └── outputs.tf
```

### Step 4: Remote State
Implement best practices in `04-remote-state/`:

```bash
cd ../04-remote-state

# Configure remote backend:
# - S3 bucket for state storage
# - DynamoDB table for state locking
# - Workspace management
# - State encryption
```

## 📝 Exercises

### Exercise 1: Basic Setup
```bash
cd terraform/01-basics

# Initialize Terraform
terraform init

# Plan changes
terraform plan

# Apply changes
terraform apply

# Verify resources were created
terraform show

# Clean up
terraform destroy
```

### Exercise 2: AWS VPC
```bash
cd ../02-aws-resources

# Create a complete VPC with:
# - Public subnet (web servers)
# - Private subnet (databases)
# - Internet Gateway
# - NAT Gateway
# - Route tables

terraform init
terraform plan
terraform apply
```

### Exercise 3: Web Server Deployment
```bash
# Deploy EC2 instances with:
# - Security groups (HTTP, SSH)
# - User data script (install web server)
# - Elastic IP addresses
# - Load balancer

terraform plan -var="instance_count=2"
terraform apply
```

### Exercise 4: Module Creation
```bash
cd ../03-modules

# Extract VPC configuration into a module
# Use the module in main configuration
# Pass variables to customize behavior

terraform init
terraform plan
terraform apply
```

### Exercise 5: Remote State Setup
```bash
cd ../04-remote-state

# Configure S3 backend
# Enable state locking with DynamoDB
# Test with multiple team members

terraform init
terraform workspace new staging
terraform workspace new production
```

## 🔧 Commands Reference
```bash
# Initialize Terraform
terraform init

# Plan changes
terraform plan

# Apply changes
terraform apply

# Destroy resources
terraform destroy

# Format code
terraform fmt

# Validate configuration
terraform validate

# Show current state
terraform show

# List resources
terraform state list

# Import existing resources
terraform import aws_instance.example i-1234567890abcdef0

# Workspace management
terraform workspace list
terraform workspace new staging
terraform workspace select production
```

## 🏗️ Best Practices

### Code Organization
```bash
# Use consistent file structure
main.tf          # Main configuration
variables.tf     # Input variables
outputs.tf       # Output values
versions.tf      # Provider versions
terraform.tfvars # Variable values (don't commit)
```

### Variable Management
```hcl
# Use descriptive variable names
variable "environment" {
  description = "Environment name (dev, staging, prod)"
  type        = string
  default     = "dev"
}

# Use validation rules
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
  
  validation {
    condition     = contains(["t3.micro", "t3.small", "t3.medium"], var.instance_type)
    error_message = "Instance type must be t3.micro, t3.small, or t3.medium."
  }
}
```

### State Management
```bash
# Always use remote state for teams
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "infrastructure/terraform.tfstate"
    region         = "us-west-2"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

## 🐛 Troubleshooting

### Common Issues
```bash
# State lock errors
# Solution: Force unlock (use carefully)
terraform force-unlock LOCK_ID

# Provider version conflicts
# Solution: Specify provider versions
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Resource already exists
# Solution: Import existing resource
terraform import aws_instance.example i-1234567890abcdef0

# Permission denied
# Solution: Check AWS credentials and IAM permissions
aws sts get-caller-identity
```

### Debugging
```bash
# Enable detailed logging
export TF_LOG=DEBUG
terraform plan

# Validate configuration
terraform validate

# Check formatting
terraform fmt -check

# Dry run with detailed output
terraform plan -detailed-exitcode
```

## 🎯 Learning Outcomes

### Infrastructure as Code Skills
- **Declarative configuration**: Define desired state
- **Version control**: Track infrastructure changes
- **Reproducibility**: Consistent environments
- **Collaboration**: Team-based infrastructure management

### Terraform Expertise
- **Resource management**: Create, update, destroy resources
- **State management**: Track resource state
- **Module development**: Reusable infrastructure components
- **Provider usage**: Multi-cloud deployments

### Cloud Architecture
- **Networking**: VPCs, subnets, routing
- **Security**: Security groups, IAM roles
- **Compute**: EC2, auto-scaling groups
- **Storage**: S3, EBS volumes
- **Load balancing**: ALB, NLB configuration

## 📚 Interview Preparation

### Key Concepts to Master
- "What is Infrastructure as Code and why is it important?"
- "Explain Terraform state and why remote state is crucial"
- "How do you handle secrets in Terraform?"
- "What are Terraform modules and when would you use them?"
- "How do you manage multiple environments with Terraform?"

### Practical Scenarios
- "Design a VPC for a web application with public and private subnets"
- "How would you implement blue-green deployments with Terraform?"
- "Explain how you'd migrate existing infrastructure to Terraform"
- "How do you handle Terraform state conflicts in a team?"

### Best Practices Discussion
- State management strategies
- Module design patterns
- Security considerations
- CI/CD integration
- Cost optimization

## 🔗 Next Steps
After mastering Terraform:
1. **Configuration Management** with Ansible (Tutorial 4)
2. **Container Orchestration** with Kubernetes (Tutorial 5)
3. **CI/CD Integration** for automated deployments (Tutorial 6)
4. **Monitoring** infrastructure with Prometheus (Tutorial 7)

## 📖 Additional Resources
- [Terraform Documentation](https://www.terraform.io/docs)
- [AWS Provider Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Terraform Best Practices](https://www.terraform.io/docs/cloud/guides/recommended-practices/index.html)
- [HashiCorp Learn](https://learn.hashicorp.com/terraform)

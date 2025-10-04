# Terraform - Infrastructure as Code

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

### Step 1: Basic Terraform Concepts
Start with the basics in `01-basics/`:
- Provider configuration
- Simple resource creation
- Variables and outputs

### Step 2: AWS Resources
Move to `02-aws-resources/`:
- VPC and networking
- EC2 instances
- Security groups
- Load balancers

### Step 3: Modules
Learn modularity in `03-modules/`:
- Creating reusable modules
- Module composition
- Version management

### Step 4: Remote State
Implement best practices in `04-remote-state/`:
- S3 backend configuration
- State locking with DynamoDB
- Workspace management

## 📝 Exercises
1. **Basic Setup**: Create your first Terraform configuration
2. **AWS VPC**: Build a complete VPC with subnets
3. **Web Server**: Deploy an EC2 instance with security groups
4. **Load Balancer**: Add an Application Load Balancer
5. **Module Creation**: Extract common patterns into modules
6. **Remote State**: Configure remote state storage

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
```

## 🎯 Key Learning Points
- **Declarative**: Describe desired state, not steps
- **Idempotent**: Safe to run multiple times
- **Plan before apply**: Always review changes
- **State is critical**: Never lose or corrupt state
- **Use modules**: Don't repeat yourself

## 📖 Best Practices
1. Always use version constraints for providers
2. Use variables for configurable values
3. Implement proper naming conventions
4. Use remote state for team collaboration
5. Never commit sensitive data
6. Use `.terraform.lock.hcl` for dependency locking

## 🔗 Resources
- [Terraform Documentation](https://www.terraform.io/docs)
- [AWS Provider Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Terraform Best Practices](https://www.terraform-best-practices.com/)

## ✅ Completion Checklist
- [ ] Understand Terraform basics and syntax
- [ ] Create AWS resources with Terraform
- [ ] Build reusable modules
- [ ] Configure remote state management
- [ ] Implement proper security practices
- [ ] Document infrastructure decisions

Start with `01-basics/main.tf` to begin your Terraform journey!

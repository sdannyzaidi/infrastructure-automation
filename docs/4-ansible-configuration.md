# 4. Ansible - Configuration Management

## 🎯 Learning Objectives
- Understand Infrastructure as Code with Ansible
- Learn playbook structure and best practices
- Manage server configurations and deployments
- Implement role-based organization
- Use Ansible Vault for secrets management

## 📚 Key Concepts
- **Playbooks**: YAML files defining tasks
- **Inventory**: List of managed hosts
- **Roles**: Reusable task collections
- **Modules**: Units of work (copy, service, etc.)
- **Variables**: Dynamic configuration
- **Handlers**: Event-driven tasks

## 🏗️ Project Structure
```
ansible/
├── inventory/              # Host inventories
├── playbooks/             # Main playbooks
├── roles/                 # Reusable roles
├── group_vars/            # Group variables
├── host_vars/             # Host-specific variables
└── ansible.cfg            # Ansible configuration
```

## 🚀 Getting Started

### Prerequisites
```bash
# Install Ansible
# macOS:
brew install ansible

# Linux:
sudo apt-get install ansible

# Python:
pip install ansible

# Verify installation
ansible --version

# Set up SSH key authentication for target hosts
ssh-keygen -t rsa -b 4096
ssh-copy-id user@target-host
```

### Step 1: Basic Configuration
```bash
cd ansible

# Create ansible.cfg
touch ansible.cfg

# Configure basic settings:
# - Inventory location
# - SSH settings
# - Logging options
# - Host key checking
```

### Step 2: Create Inventory
```bash
# Create inventory/hosts.yml
mkdir -p inventory
touch inventory/hosts.yml

# Define host groups:
# - web servers
# - database servers
# - load balancers
# - monitoring servers
```

### Step 3: Write Your First Playbook
```bash
# Create playbooks/site.yml
mkdir -p playbooks
touch playbooks/site.yml

# Include tasks for:
# - System updates
# - Package installation
# - Service configuration
# - File management
```

### Step 4: Test Connectivity
```bash
# Test connection to all hosts
ansible all -m ping

# Run ad-hoc commands
ansible all -m shell -a "uptime"
ansible web -m service -a "name=nginx state=started"

# Gather facts about hosts
ansible all -m setup
```

### Step 5: Run Your First Playbook
```bash
# Check playbook syntax
ansible-playbook playbooks/site.yml --syntax-check

# Dry run (check mode)
ansible-playbook playbooks/site.yml --check

# Execute playbook
ansible-playbook playbooks/site.yml

# Run with verbose output
ansible-playbook playbooks/site.yml -v
```

## 📝 Core Exercises

### Exercise 1: Web Server Setup
```bash
# Create playbooks/webservers.yml
touch playbooks/webservers.yml

# Implement tasks to:
# 1. Install Nginx
# 2. Configure virtual hosts
# 3. Start and enable service
# 4. Configure firewall
# 5. Deploy application code
```

### Exercise 2: Database Configuration
```bash
# Create playbooks/database.yml
touch playbooks/database.yml

# Implement tasks to:
# 1. Install MySQL/PostgreSQL
# 2. Configure database settings
# 3. Create databases and users
# 4. Set up backups
# 5. Configure security
```

### Exercise 3: Role Development
```bash
# Create a web server role
ansible-galaxy init roles/webserver

# Structure:
# roles/webserver/
# ├── tasks/main.yml      # Main tasks
# ├── handlers/main.yml   # Event handlers
# ├── templates/          # Jinja2 templates
# ├── files/             # Static files
# ├── vars/main.yml      # Role variables
# └── defaults/main.yml  # Default variables
```

### Exercise 4: Variable Management
```bash
# Create group variables
mkdir -p group_vars
echo "nginx_port: 80" > group_vars/web.yml
echo "db_name: myapp" > group_vars/database.yml

# Create host-specific variables
mkdir -p host_vars
echo "server_id: 1" > host_vars/web1.example.com.yml
```

### Exercise 5: Secrets Management
```bash
# Create encrypted variables with Ansible Vault
ansible-vault create group_vars/all/vault.yml

# Edit encrypted file
ansible-vault edit group_vars/all/vault.yml

# Run playbook with vault password
ansible-playbook playbooks/site.yml --ask-vault-pass
```

## 🔧 Essential Commands

### Inventory Management
```bash
# List all hosts
ansible all --list-hosts

# List hosts in specific group
ansible web --list-hosts

# Show inventory graph
ansible-inventory --graph
```

### Playbook Operations
```bash
# Syntax check
ansible-playbook playbook.yml --syntax-check

# Dry run
ansible-playbook playbook.yml --check

# Run specific tags
ansible-playbook playbook.yml --tags "install,configure"

# Skip specific tags
ansible-playbook playbook.yml --skip-tags "backup"

# Limit to specific hosts
ansible-playbook playbook.yml --limit "web1,web2"
```

### Ad-hoc Commands
```bash
# Package management
ansible all -m package -a "name=htop state=present"

# Service management
ansible web -m service -a "name=nginx state=restarted"

# File operations
ansible all -m copy -a "src=/local/file dest=/remote/file"

# User management
ansible all -m user -a "name=deploy state=present"
```

### Vault Operations
```bash
# Create encrypted file
ansible-vault create secrets.yml

# Edit encrypted file
ansible-vault edit secrets.yml

# View encrypted file
ansible-vault view secrets.yml

# Change vault password
ansible-vault rekey secrets.yml

# Encrypt existing file
ansible-vault encrypt existing-file.yml
```

## 🏗️ Best Practices

### Playbook Structure
```yaml
---
- name: Configure web servers
  hosts: web
  become: yes
  vars:
    nginx_port: 80
  
  tasks:
    - name: Install Nginx
      package:
        name: nginx
        state: present
      notify: restart nginx
    
    - name: Configure Nginx
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      notify: restart nginx
  
  handlers:
    - name: restart nginx
      service:
        name: nginx
        state: restarted
```

### Role Organization
```bash
# Use roles for reusability
- name: Apply web server role
  hosts: web
  roles:
    - { role: webserver, nginx_port: 80 }
    - { role: monitoring, when: monitoring_enabled }
```

### Variable Precedence
```bash
# Understand variable precedence (highest to lowest):
# 1. Extra vars (-e)
# 2. Task vars
# 3. Block vars
# 4. Role and include vars
# 5. Play vars
# 6. Host facts
# 7. Host vars
# 8. Group vars
# 9. Role defaults
```

## 🐛 Troubleshooting

### Common Issues
```bash
# SSH connection failures
# Solution: Check SSH keys and connectivity
ansible all -m ping -vvv

# Permission denied
# Solution: Use become for privilege escalation
ansible-playbook playbook.yml --become

# Module not found
# Solution: Check Ansible version and module availability
ansible-doc -l | grep module_name

# Syntax errors
# Solution: Use syntax check and linting
ansible-playbook playbook.yml --syntax-check
ansible-lint playbook.yml
```

### Debugging
```bash
# Verbose output
ansible-playbook playbook.yml -vvv

# Debug tasks
- name: Debug variable
  debug:
    var: my_variable

# Check mode (dry run)
ansible-playbook playbook.yml --check --diff

# Step through playbook
ansible-playbook playbook.yml --step
```

## 🎯 Learning Outcomes

### Configuration Management Skills
- **Idempotency**: Ensure consistent system state
- **Automation**: Eliminate manual configuration
- **Scalability**: Manage hundreds of servers
- **Consistency**: Standardize configurations

### Ansible Expertise
- **Playbook development**: Write maintainable automation
- **Role creation**: Build reusable components
- **Inventory management**: Organize infrastructure
- **Variable management**: Handle dynamic configuration
- **Security**: Manage secrets with Vault

### DevOps Integration
- **CI/CD integration**: Automated deployments
- **Infrastructure provisioning**: Post-Terraform configuration
- **Application deployment**: Zero-downtime deployments
- **Monitoring setup**: Automated monitoring configuration

## 📚 Interview Preparation

### Key Concepts
- "What is idempotency and why is it important in Ansible?"
- "Explain the difference between Ansible and other configuration management tools"
- "How do you handle secrets in Ansible?"
- "What are Ansible roles and when would you use them?"
- "How do you test Ansible playbooks?"

### Practical Scenarios
- "How would you deploy a web application with zero downtime?"
- "Explain how you'd manage different environments (dev/staging/prod)"
- "How do you handle configuration drift?"
- "What's your approach to organizing large Ansible projects?"

### Troubleshooting Questions
- "How do you debug failed Ansible tasks?"
- "What would you do if a playbook runs successfully but doesn't make changes?"
- "How do you handle SSH connectivity issues?"

## 🔗 Integration Examples

### With Terraform
```bash
# Use Terraform to provision infrastructure
terraform apply

# Use Ansible to configure provisioned servers
ansible-playbook -i terraform-inventory playbooks/site.yml
```

### With CI/CD
```yaml
# GitHub Actions example
- name: Run Ansible Playbook
  uses: dawidd6/action-ansible-playbook@v2
  with:
    playbook: playbooks/deploy.yml
    directory: ./ansible
    key: ${{ secrets.SSH_PRIVATE_KEY }}
    inventory: inventory/production.yml
```

## 🚀 Next Steps
After mastering Ansible:
1. **Container Orchestration** with Kubernetes (Tutorial 5)
2. **CI/CD Pipelines** with automated configuration (Tutorial 6)
3. **Monitoring Setup** with automated Prometheus deployment (Tutorial 7)
4. **Advanced Automation** with Ansible Tower/AWX

## 📖 Additional Resources
- [Ansible Documentation](https://docs.ansible.com/)
- [Ansible Galaxy](https://galaxy.ansible.com/) - Community roles
- [Ansible Best Practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [Ansible Lint](https://ansible-lint.readthedocs.io/) - Playbook linting tool

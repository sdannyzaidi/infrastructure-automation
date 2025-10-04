# Ansible - Configuration Management

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

### Installation
```bash
# macOS
brew install ansible

# Linux
sudo apt-get install ansible

# Python
pip install ansible
```

### Basic Commands
```bash
# Test connectivity
ansible all -m ping

# Run ad-hoc commands
ansible all -m shell -a "uptime"

# Run playbooks
ansible-playbook playbooks/site.yml

# Check syntax
ansible-playbook --syntax-check playbooks/site.yml

# Dry run
ansible-playbook --check playbooks/site.yml

# Run specific tags
ansible-playbook playbooks/site.yml --tags "web"
```

## 📝 Learning Exercises

### 1. Basic Server Setup
- Configure SSH keys
- Install essential packages
- Set up users and groups
- Configure firewall rules

### 2. Web Server Deployment
- Install and configure Nginx
- Deploy application code
- Set up SSL certificates
- Configure log rotation

### 3. Database Setup
- Install PostgreSQL/MySQL
- Create databases and users
- Configure backups
- Set up monitoring

### 4. Docker Deployment
- Install Docker
- Deploy containerized applications
- Configure Docker Compose
- Set up container monitoring

## 🔧 Best Practices
1. Use roles for organization
2. Keep playbooks idempotent
3. Use variables for flexibility
4. Implement proper error handling
5. Use Ansible Vault for secrets
6. Test with --check mode first

## 📖 Key Modules
- **copy**: Copy files to remote hosts
- **template**: Process Jinja2 templates
- **service**: Manage services
- **package**: Install packages
- **user**: Manage user accounts
- **file**: Manage files and directories
- **shell/command**: Execute commands
- **git**: Manage git repositories

## ✅ Completion Checklist
- [ ] Set up inventory and basic connectivity
- [ ] Create server configuration playbooks
- [ ] Implement application deployment
- [ ] Use roles for code organization
- [ ] Manage secrets with Ansible Vault
- [ ] Set up continuous deployment

Start with the inventory setup and basic playbooks!

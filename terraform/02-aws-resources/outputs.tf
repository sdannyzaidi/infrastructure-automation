# VPC outputs
output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

output "vpc_cidr_block" {
  description = "CIDR block of the VPC"
  value       = aws_vpc.main.cidr_block
}

# Subnet outputs
output "public_subnet_ids" {
  description = "IDs of the public subnets"
  value       = aws_subnet.public[*].id
}

output "internet_gateway_id" {
  description = "ID of the Internet Gateway"
  value       = aws_internet_gateway.main.id
}

# Summary output
output "network_summary" {
  description = "Summary of the created network infrastructure"
  value = {
    vpc_id              = aws_vpc.main.id
    public_subnet_count = length(aws_subnet.public)
    availability_zones  = var.availability_zones
    environment         = var.environment
  }
}
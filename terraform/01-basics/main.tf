# Terraform Basics - Your First Configuration
# This file demonstrates basic Terraform concepts

# Configure the required providers
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.1"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = var.aws_region
  
  # Use default credentials from AWS CLI or environment variables
  # For learning: aws configure or set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
}

# Generate a random suffix for unique resource names
resource "random_id" "suffix" {
  byte_length = 4
}

# Create an S3 bucket (free tier eligible)
resource "aws_s3_bucket" "learning_bucket" {
  bucket = "${var.project_name}-learning-${random_id.suffix.hex}"
  
  tags = {
    Name        = "Learning Bucket"
    Environment = var.environment
    Project     = var.project_name
    ManagedBy   = "Terraform"
  }
}

# Configure bucket versioning
resource "aws_s3_bucket_versioning" "learning_bucket_versioning" {
  bucket = aws_s3_bucket.learning_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

# Configure bucket server-side encryption
resource "aws_s3_bucket_server_side_encryption_configuration" "learning_bucket_encryption" {
  bucket = aws_s3_bucket.learning_bucket.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# Block public access to the bucket
resource "aws_s3_bucket_public_access_block" "learning_bucket_pab" {
  bucket = aws_s3_bucket.learning_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# Create a simple text file in the bucket
resource "aws_s3_object" "welcome_file" {
  bucket = aws_s3_bucket.learning_bucket.id
  key    = "welcome.txt"
  content = "Welcome to Infrastructure as Code with Terraform!\nThis file was created automatically."
  
  tags = {
    Name = "Welcome File"
    Type = "Documentation"
  }
}

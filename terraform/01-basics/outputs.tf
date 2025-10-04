# Outputs - Values to display after terraform apply
# Outputs are useful for sharing information between configurations

output "bucket_name" {
  description = "Name of the created S3 bucket"
  value       = aws_s3_bucket.learning_bucket.bucket
}

output "bucket_arn" {
  description = "ARN of the created S3 bucket"
  value       = aws_s3_bucket.learning_bucket.arn
}

output "bucket_domain_name" {
  description = "Domain name of the S3 bucket"
  value       = aws_s3_bucket.learning_bucket.bucket_domain_name
}

output "bucket_region" {
  description = "Region where the bucket was created"
  value       = aws_s3_bucket.learning_bucket.region
}

output "welcome_file_key" {
  description = "Key of the welcome file in the bucket"
  value       = aws_s3_object.welcome_file.key
}

output "random_suffix" {
  description = "Random suffix used for resource naming"
  value       = random_id.suffix.hex
}

# Example of sensitive output
output "bucket_id" {
  description = "ID of the S3 bucket (marked as sensitive)"
  value       = aws_s3_bucket.learning_bucket.id
  sensitive   = true
}

# Complex output example
output "resource_summary" {
  description = "Summary of created resources"
  value = {
    bucket_name   = aws_s3_bucket.learning_bucket.bucket
    bucket_region = aws_s3_bucket.learning_bucket.region
    environment   = var.environment
    project       = var.project_name
    created_at    = timestamp()
  }
}

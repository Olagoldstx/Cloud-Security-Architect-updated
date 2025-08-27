
# Terraform Guardrails Example: Enforce Encryption on S3 Buckets
resource "aws_s3_bucket" "secure_bucket" {
  bucket = "my-secure-bucket"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "default" {
  bucket = aws_s3_bucket.secure_bucket.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

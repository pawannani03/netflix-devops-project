variable "aws_region" {
  description = "AWS deployment region"
  type        = string
  default     = "ap-south-1"
}

variable "admin_ip_cidr" {
  description = "Your public IP address in CIDR notation"
  type        = string
}

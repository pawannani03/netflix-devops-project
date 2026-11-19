output "ecr_repository_url" {
  value = aws_ecr_repository.netflix.repository_url
}

output "eks_cluster_name" {
  value = module.eks.cluster_name
}

output "aws_region" {
  value = var.aws_region
}

output "vpc_id" {
  value = module.vpc.vpc_id
}

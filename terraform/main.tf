terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "blog" {
  ami                    = "ami-03420506796dd6873"
  instance_type          = "t2.micro"
  key_name               = "blog_app"
  subnet_id              = "subnet-074d693e5f9dcad9d"
  vpc_security_group_ids = [
      "sg-0851156431c72f7d3",
      "sg-0a569ee6952d11594"
  ]

  tags = {
    Name = "blog"
  }
}

resource "aws_vpc" "blog" {
  cidr_block = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support = true
  assign_generated_ipv6_cidr_block = false
  instance_tenancy = "default"

  tags = {
    Name = "blog"
  }
}

resource "aws_internet_gateway" "blog" {
  vpc_id = aws_vpc.blog.id

  tags = {
    Name = "blog"
  }
}

resource "aws_route_table" "public-route" {
  vpc_id = aws_vpc.blog.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.blog.id
  }

  tags = {
    Name = "public-route"
  }
}

resource "aws_route_table_association" "app_public_association" {
  subnet_id      = aws_subnet.app-public.id
  route_table_id = aws_route_table.public-route.id
}

resource "aws_subnet" "app-public" {
  vpc_id                  = aws_vpc.blog.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-west-2a"
  map_public_ip_on_launch = false

  tags = {
    Name = "app-public"
  }
}

resource "aws_db_instance" "blog" {
  identifier               = "blog-db"
  engine                   = "mysql"
  engine_version           = "8.0.42"
  instance_class           = "db.t4g.micro"
  allocated_storage        = 20
  max_allocated_storage    = 1000
  storage_type             = "gp2"
  storage_encrypted        = true
  kms_key_id               = "arn:aws:kms:us-west-2:985539772717:key/33f3ff0a-0afe-4b65-8941-0a6a7650bb40"
  username                 = "admin"
  password                 = var.db_password
  port                     = 3306
  vpc_security_group_ids   = ["sg-01f6132af0819b945"]
  db_subnet_group_name     = "rds-ec2-db-subnet-group-2"
  monitoring_interval      = 60
  monitoring_role_arn      = "arn:aws:iam::985539772717:role/rds-monitoring-role"
  option_group_name        = "default:mysql-8-0"
  parameter_group_name     = "default.mysql8.0"
  backup_retention_period  = 7
  backup_window            = "11:56-12:26"
  maintenance_window       = "tue:09:12-tue:09:42"
  auto_minor_version_upgrade = true
  copy_tags_to_snapshot    = true
  publicly_accessible      = false
  skip_final_snapshot      = true

  tags = {
    Name = "blog"
  }
}


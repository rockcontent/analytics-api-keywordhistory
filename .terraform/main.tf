provider "aws" {
  region = lookup(var.fargate_region_mapping, var.BRANCH)
}

terraform {
  backend "s3" {
    bucket = "tfstate-rock-shared"
    region = "us-east-1"
  }
}

variable "PROJECT" {
  type = string
}

variable "BRANCH" {
  type = string
}

#############################
#    App config var map     #
#############################

variable "sub_domain_mapping" {
  description = "mapping subdomains for each branch"
  default = {
    "master"  = "api.sem.rockcontent.com",
    "development" = "apidev.sem.rockcontent.com"
  }
}
variable "fargate_cpu_mapping" {
  description = "mapping cpu for each branch"
  default = {
    "master"  = 256,
    "development" = 256
  }
}
variable "fargate_memory_mapping" {
  description = "mapping memory for each branch"
  default = {
    "master"  = 512,
    "development" = 512
  }
}
variable "min_capacity_mapping" {
  description = "mapping min capacity for each branch"
  default = {
    "master"  = 1,
    "development" = 1
  }
}
variable "max_capacity_mapping" {
  description = "mapping max capacity for each branch"
  default = {
    "master"  = 4,
    "development" = 1
  }
}
#############################
#  AWS environment var map  #
#############################
# Select region of each branch
variable "fargate_region_mapping" {
  description = "mapping region for branch"
  default = {
    "master"  = "us-east-1",
    "development" = "us-east-1"

  }
}
variable "fargate_loadbalancer_mapping" {
  description = "mapping loadbalancer for branch"
  default = {
    "master"  = "arn:aws:elasticloadbalancing:us-east-1:798853119042:listener/app/rockos/e5531abcf0f98b89/298d409f9070ec47",
    "development" = "arn:aws:elasticloadbalancing:us-east-1:798853119042:listener/app/rockos/e5531abcf0f98b89/298d409f9070ec47"
  }
}
variable "fargate_subnet1_mapping" {
  description = "mapping subnet 1 for branch"
  default = {
    "master"  = "subnet-87e3afa9",
    "development" = "subnet-87e3afa9"
  }
}
variable "fargate_subnet2_mapping" {
  description = "mapping subnet 2 for branch"
  default = {
    "master"  = "subnet-eda3b2a7",
    "development" = "subnet-eda3b2a7"

  }
}
variable "fargate_vpc_mapping" {
  description = "mapping vpc for branch"
  default = {
    "master"  = "vpc-7e5dc004",
    "development" = "vpc-7e5dc004"

  }
}
variable "fargate_sg_mapping" {
  description = "mapping securitygroup for branch"
  default = {
    "master"  = "sg-067e66535d6bc8633",
    "development" = "sg-067e66535d6bc8633"
  }
}
variable "fargate_logsretention_mapping" {
  description = "mapping logs retetion period for branch (days)"
  default = {
    "master"  = 3,
    "development" = 1
  }
}
module "shared-api" {
  source                  = "git::https://sharedgroup:hdS65zJyErjBPvpweHYV@gitlab.rockcontent.com/shared/devops/shared-devops-fargatetf.git"
  project                 = lower(var.PROJECT)
  #############################
  #         App config        #
  #############################
  sub_domain              = "${lookup(var.sub_domain_mapping, var.BRANCH)}"
  app_port                = 80
  fargate_cpu             = "${lookup(var.fargate_cpu_mapping, var.BRANCH)}"
  fargate_memory          = "${lookup(var.fargate_memory_mapping, var.BRANCH)}"
  metric_type             = "ECSServiceAverageCPUUtilization" # ECSServiceAverageMemoryUtilization
  min_capacity            = "${lookup(var.min_capacity_mapping, var.BRANCH)}"
  max_capacity            = "${lookup(var.max_capacity_mapping, var.BRANCH)}"
  target_value            = 80
  tg-interval             = 30
  tg-timeout              = 5
  tg-path	                = "/docs"
  tg-matcher              = "200"
  tg-healthy_threshold    = 5
  tg-unhealthy_threshold  = 2
  #############################
  #      AWS environment      #
  #############################
  fargate_accountid       = 798853119042
  fargate_region          = "${lookup(var.fargate_region_mapping, var.BRANCH)}"
  fargate_loadbalancer    = "${lookup(var.fargate_loadbalancer_mapping, var.BRANCH)}"
  fargate_subnet1         = "${lookup(var.fargate_subnet1_mapping, var.BRANCH)}"
  fargate_subnet2         = "${lookup(var.fargate_subnet2_mapping, var.BRANCH)}"
  fargate_publicip        = "true"
  fargate_vpc             = "${lookup(var.fargate_vpc_mapping, var.BRANCH)}"
  fargate_sg              = "${lookup(var.fargate_sg_mapping, var.BRANCH)}"
  fargate_logsretention   = "${lookup(var.fargate_logsretention_mapping, var.BRANCH)}"
  
  tags = {
    "Branch" = var.BRANCH
    "Cost Center" = "Shared"
    "Project"     = var.PROJECT
    "Created by"     = "Terraform"    
  }
}

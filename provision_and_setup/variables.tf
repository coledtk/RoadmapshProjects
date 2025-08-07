  variable "region" {
    default = "us-west-2"
  }

  variable "ami_id" {
    description = "AMI to use"
    default = "ami-05f991c49d264708f"
  }

  variable "instance_type" {
    default = "t3.micro"
  }

  variable "key_name" {
    default = "terraform-key"
  }

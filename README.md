# Article41-devops-challenge-senior

## Task 1 – Containerization of Time Service API

This project begins with a simple Python-based API service built using FastAPI. The service returns:

- The current UTC timestamp

- The IP address of the client making the request

The service is packaged into a Docker container and published on DockerHub for easy use and testing.

---

### Features

- Lightweight API built with Flask
- Returns:
  - Current UTC timestamp
  - Client IP address
- Dockerized and published to DockerHub for easy access

---

### Docker Image

The image is publicly available on DockerHub:
Here is the URL that everyone can see or access.
```
https://hub.docker.com/r/nitishraja/simple-time-service
```
### How to Run the Service
#### 1. Pull the image from DockerHub:
```
docker pull nitishraja/simple-time-service:latest
```
#### 2. Run the container:
```
docker run -d -p 5050:5050 --name time-service nitishraja/simple-time-service:latest
```
#### 3. Test the API:
  - Open a new terminal window and run:
      ```
      curl http://localhost:5050/
      ```
#### 4. Sample Response:
```
{
  "timestamp": "timestamp_utc,
  "ip": "client_ip"
}
```
#### 5. Notes
  - If port 5050 is already in use, you can run on another port like this:
    ```
    docker run -p port_no:5050 nitishraja/simple-time-service
    curl http://localhost:port_no/
    ```
## Task 2 – Infrastructure Deployment with Terraform (AWS)

In this task, we deploy the containerized time service (from Task 1) on AWS using Terraform with the following architecture:

## Infrastructure Summary
  - VPC with:

    - 2 Public Subnets

    - 2 Private Subnets

  - ECS Cluster with Fargate Launch Type

  - ECS Service running the Docker container on private subnets

  - Application Load Balancer (ALB) in public subnets routing traffic to ECS service

  - Internet Gateway and NAT Gateway for proper routing

  - ECS Task Definition uses the public image from DockerHub

## How to Deploy the Infrastructure
### Prerequisites:

  - Terraform installed

  - AWS CLI configured with valid credentials (aws configure)

  - DockerHub image published (from Task 1)

#### 1. Navigate to the Terraform directory:
```
cd terraform/
```
#### 2. Initialize Terraform:
```
terraform init
```
#### 3. Review the plan:
```
terraform plan
```
#### 4. Apply the infrastructure:
```
terraform apply
```
  - #### Type ``` yes ``` when prompted.

#### 5. After successful deployment, Terraform will output a public Load Balancer DNS like:
```
load_balancer_dns = "simple-time-service-alb-xxxxxxxxxx.us-east-1.elb.amazonaws.com"
```

##  How to Test
### 1. Copy the load_balancer_dns output from Terraform.
### 2. Hit the endpoint in your browser or terminal:
```
curl http://<load_balancer_dns>/
```
### 3. Expected Response:
```
{
  "timestamp": "2025-06-22T11:45:30.123456Z",
  "ip": "xx.xx.xx.xx"
}
```
## Destroy the Infrastructure
Once done testing, you can destroy all AWS resources to avoid charges:
```
terraform destroy
```
## Conclusion
This repository showcases a complete DevOps workflow — from building and containerizing a simple time service API using Docker to deploying it on AWS using Terraform with a fully scalable and production-ready ECS Fargate architecture.

  - Task 1: Dockerizing a lightweight FastAPI service

  - Task 2: Deploying that service to AWS via Terraform

The solution follows best practices in:

  - Containerization (Docker + FastAPI)

  - Infrastructure as Code (Terraform)

  - Cloud deployment (AWS ECS, VPC, ALB)

This setup enables any developer or DevOps engineer to:

  - Pull and test the container image locally

  - Deploy the infrastructure seamlessly on their own AWS account

  - Verify API responses via Load Balancer DNS

# THE END

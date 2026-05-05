# VPC Setup with Bastion Host, Secrets Manager & S3 Flow Logs

![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazon-aws)
![EC2](https://img.shields.io/badge/EC2-Compute-blue)
![S3](https://img.shields.io/badge/S3-Storage-green)
![VPC](https://img.shields.io/badge/VPC-Networking-purple)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

## Overview
This project demonstrates a secure AWS architecture using:
- Custom VPC with public and private subnets  
- Bastion (Jump) server for secure access  
- Private EC2 instance without public exposure  
- Secure key management using AWS Secrets Manager  
- VPC Flow Logs stored in S3 for monitoring  

---

## Architecture Flow


Local Machine
↓
Bastion Host (Public Subnet)
↓
Private EC2 (Private Subnet)

    ↓

VPC Flow Logs
↓
S3


---

## Project Documentation

Detailed step-by-step guide is available here:

👉 [docs/doc.md](docs/doc.md)

---

## Key Features

- Secure access to private EC2 using Bastion Host  
- No public exposure for backend instance  
- SSH key stored securely in AWS Secrets Manager  
- VPC Flow Logs enabled and stored in S3  
- Cost-effective logging solution  

---

## Technologies Used

- AWS VPC  
- EC2  
- AWS Secrets Manager  
- Amazon S3  
- Linux (SSH)  

---

## How It Works

1. User connects to Bastion Host using SSH  
2. Bastion retrieves private key from Secrets Manager  
3. Bastion connects to Private EC2  
4. Network traffic is captured using VPC Flow Logs  
5. Logs are stored in S3 for analysis  

---

## Notes

- No IAM role required for S3 flow logs  
- Bucket policy is mandatory  
- Logs take a few minutes to appear  
- Ensure all services are in the same region  

---

## Future Improvements

- Replace SSH with AWS Systems Manager Session Manager  
- Analyze logs using Athena  
- Automate setup using Terraform  

---

## Author

Rohith T

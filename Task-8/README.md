🌍 Multi-Region AWS Transit Gateway Setup

![AWS](https://img.shields.io/badge/AWS-Transit_Gateway-orange?style=for-the-badge&logo=amazonaws)
![Multi Region](https://img.shields.io/badge/Multi--Region-Networking-blue?style=for-the-badge)
![Transit Gateway](https://img.shields.io/badge/Transit_Gateway-Peering-success?style=for-the-badge)
![VPC](https://img.shields.io/badge/VPC-Full_Mesh-important?style=for-the-badge)
![EC2](https://img.shields.io/badge/EC2-Cross_Region-purple?style=for-the-badge)
![Cloud](https://img.shields.io/badge/Cloud-Architecture-informational?style=for-the-badge)
![Routing](https://img.shields.io/badge/Routing-TGW_Route_Tables-yellow?style=for-the-badge)
![Connectivity](https://img.shields.io/badge/Connectivity-SSH_Jumping-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-AWS-black?style=for-the-badge&logo=amazonaws)

📌 Project Overview

This project demonstrates how to build a Multi-Region AWS Network Architecture using AWS Transit Gateway (TGW) and Transit Gateway Peering.

The setup connects:

Mumbai Region (ap-south-1)
Hyderabad Region (ap-south-2)
N. Virginia Region (us-east-1)

using a Full Mesh Transit Gateway Peering Architecture.

Since Transit Gateway Peering is NOT transitive, all TGWs are interconnected manually.

🏗️ Architecture Diagram


                                 ┌──────────────────────────┐
                                 │     AWS CLOUD            │
                                 └──────────────────────────┘


      ┌──────────────────────┐           TGW PEERING           ┌──────────────────────┐
      │     MUMBAI REGION    │◄──────────────────────────────►│   HYDERABAD REGION   │
      │     ap-south-1       │                                │     ap-south-2       │
      └──────────────────────┘                                └──────────────────────┘
                 │                                                         │
                 │                                                         │
         ┌───────▼────────┐                                       ┌────────▼───────┐
         │   Mumbai TGW   │◄──────────── TGW PEERING ───────────►│ Hyderabad TGW  │
         └───────┬────────┘                                       └────────┬───────┘
                 │                                                         │
                 │                                                         │
         ┌───────▼────────┐                                       ┌────────▼───────┐
         │ Mumbai VPC     │                                       │ Hyderabad VPC  │
         │ 10.0.0.0/16    │                                       │ 11.0.0.0/16    │
         └───────┬────────┘                                       └────────┬───────┘
                 │                                                         │
         ┌───────▼────────┐                                       ┌────────▼───────┐
         │ Public Subnet  │                                       │ Public Subnet  │
         │ 10.0.1.0/24    │                                       │ 11.0.1.0/24    │
         └───────┬────────┘                                       └────────┬───────┘
                 │                                                         │
         ┌───────▼────────┐                                       ┌────────▼───────┐
         │  Mumbai EC2    │                                       │ Hyderabad EC2  │
         └────────────────┘                                       └────────────────┘



                          TGW PEERING
             ┌───────────────────────────────────────┐
             │                                       │
             ▼                                       ▼


                    ┌────────────────────────────┐
                    │     N. VIRGINIA REGION     │
                    │        us-east-1           │
                    └────────────────────────────┘
                                   │
                           ┌───────▼────────┐
                           │  Virginia TGW  │
                           └───────┬────────┘
                                   │
                           ┌───────▼────────┐
                           │  Virginia VPC  │
                           │  12.0.0.0/16   │
                           └───────┬────────┘
                                   │
                           ┌───────▼────────┐
                           │ Public Subnet  │
                           │ 12.0.1.0/24    │
                           └───────┬────────┘
                                   │
                           ┌───────▼────────┐
                           │  Virginia EC2  │
                           └────────────────┘
🌐 Regions & CIDR Blocks
Region	VPC CIDR
Mumbai (ap-south-1)	10.0.0.0/16
Hyderabad (ap-south-2)	11.0.0.0/16
N. Virginia (us-east-1)	12.0.0.0/16
🚀 Services Used
Amazon VPC
Amazon EC2
AWS Transit Gateway
Transit Gateway Peering
Internet Gateway
Route Tables
Security Groups
📂 Documentation

Detailed implementation steps are available inside the docs/ folder.

📄 Reference document:
docs/8.Multi-Region Transit Gateway Setup.docx

🛠️ Architecture Components
✅ VPCs
Region	VPC Name	CIDR
Mumbai	mumbai-vpc	10.0.0.0/16
Hyderabad	hyderabad-vpc	11.0.0.0/16
Virginia	virginia-vpc	12.0.0.0/16
✅ Public Subnets
Region	Subnet	CIDR
Mumbai	mumbai-public-subnet	10.0.1.0/24
Hyderabad	hyderabad-public-subnet	11.0.1.0/24
Virginia	virginia-public-subnet	12.0.1.0/24
✅ EC2 Instances
Region	Instance
Mumbai	mumbai-ec2
Hyderabad	hyderabad-ec2
Virginia	virginia-ec2
✅ Transit Gateways
Region	TGW
Mumbai	mumbai-tgw
Hyderabad	hyderabad-tgw
Virginia	virginia-tgw
🔗 TGW Peering Connections
Source TGW	Destination TGW
Mumbai TGW	Hyderabad TGW
Mumbai TGW	Virginia TGW
Hyderabad TGW	Virginia TGW
🧠 Key Learning
Why Full Mesh Peering?

AWS Transit Gateway Peering is:

❌ NOT Transitive
✅ Region-to-Region Direct Connectivity Only

Therefore:

Mumbai cannot automatically route traffic to Virginia through Hyderabad.
Direct peering between all TGWs is required.
🛣️ Route Configuration
TGW Route Tables

Each TGW route table contains:

Local VPC CIDR
Remote VPC CIDRs via TGW Peering attachments
VPC Route Tables

Each VPC route table contains:

Routes to remote VPC CIDRs
Target → Regional Transit Gateway
🔐 Security Group Rules

Allowed:

Type	Source
SSH (22)	0.0.0.0/0
ICMP	0.0.0.0/0
🧪 Connectivity Testing

SSH Jumping was used for testing private connectivity.

Example
ssh -i mumbai-key.pem ec2-user@MUMBAI-PUBLIC-IP

From Mumbai EC2:

ssh -i hyderabad-key.pem ec2-user@11.0.1.X
ssh -i virginia-key.pem ec2-user@12.0.1.X
📘 Real-World Use Cases
Multi-Region Enterprise Networks
Disaster Recovery (DR)
Hybrid Cloud Connectivity
Global Application Architecture
Cross-Region Internal Communication
Centralized Networking Architecture
📚 Project Structure
project/
│
├── README.md
│
├── docs/
│   └── 8.Multi-Region Transit Gateway Setup.docx
│
└── architecture/
    └── multi-region-tgw-diagram.png
✅ Final Result

Successfully achieved:

Multi-Region Connectivity
TGW Full Mesh Peering
Cross-Region SSH Communication
Private Routing Between Regions
Highly Scalable AWS Network Architecture
👨‍💻 Author

Rohith

AWS | Cloud | Networking | DevOps Enthusiast

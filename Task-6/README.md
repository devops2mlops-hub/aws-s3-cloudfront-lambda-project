# 🔗 AWS Cross-Account VPC Peering Setup

![AWS](https://img.shields.io/badge/AWS-VPC%20Peering-orange?style=for-the-badge&logo=amazonaws)
![Network](https://img.shields.io/badge/Networking-Cross%20Account-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-yellow?style=for-the-badge)

---

# 📌 Project Overview

This project demonstrates how to configure **Cross-Account VPC Peering** between two AWS accounts to enable **private communication** between EC2 instances using private IP addresses.

The setup includes:

- Two separate AWS accounts
- Two different VPCs
- VPC Peering Connection
- Route Table Configuration
- Security Group Configuration
- Private EC2-to-EC2 Communication

---

# 🏗️ Architecture Diagram
<img width="1693" height="929" alt="image" src="https://github.com/user-attachments/assets/8e3d58b4-0887-42fd-a1c0-6d7b4c994459" />


```text
                ┌─────────────────────────────┐
                │        AWS Account A        │
                │─────────────────────────────│
                │ VPC CIDR: 10.0.0.0/16      │
                │ Subnet: 10.0.1.0/24        │
                │ EC2-A: 10.0.1.214          │
                └─────────────┬───────────────┘
                              │
                              │  VPC Peering
                              │
                ┌─────────────┴───────────────┐
                │        AWS Account B        │
                │─────────────────────────────│
                │ VPC CIDR: 11.0.0.0/16      │
                │ Subnet: 11.0.1.0/24        │
                │ EC2-B: 11.0.1.109          │
                └─────────────────────────────┘
```

---

# 🎯 Objective

Enable:

- `EC2-A (10.0.1.214)`  
to communicate privately with  
- `EC2-B (11.0.1.109)`

using **AWS VPC Peering**.

---

# 📋 Prerequisites

Before starting, ensure you have:

- Two AWS Accounts
- IAM permissions for:
  - VPC
  - EC2
  - Route Tables
  - Security Groups
  - VPC Peering
- Existing EC2 key pairs
- Non-overlapping CIDR blocks

---

# 🧱 Account Details

| Resource | Account A | Account B |
|---|---|---|
| VPC CIDR | 10.0.0.0/16 | 11.0.0.0/16 |
| Subnet CIDR | 10.0.1.0/24 | 11.0.1.0/24 |
| EC2 Private IP | 10.0.1.214 | 11.0.1.109 |

---

# 🚀 Step-by-Step Implementation

---

# PART 1 — Create VPC in Account B

## Step 1.1 — Create VPC

Navigate to:

```bash
VPC → Your VPCs → Create VPC
```

Configuration:

| Field | Value |
|---|---|
| Name | vpc-b |
| IPv4 CIDR | 11.0.0.0/16 |

---

## Step 1.2 — Create Subnet

Navigate to:

```bash
VPC → Subnets → Create subnet
```

Configuration:

| Field | Value |
|---|---|
| Subnet CIDR | 11.0.1.0/24 |

---

## Step 1.3 — Launch EC2

Launch an EC2 instance inside:

```bash
11.0.1.0/24
```

Example private IP:

```bash
11.0.1.109
```

---

# PART 2 — Create VPC Peering

## Step 2.1 — Login to Account A

Navigate to:

```bash
VPC → Peering Connections
```

Click:

```bash
Create Peering Connection
```

---

## Step 2.2 — Configure Peering

| Field | Value |
|---|---|
| Name | peer-ab |
| Requester VPC | Account A VPC |
| Account | Another account |
| Account ID | Account B ID |
| VPC ID | Account B VPC ID |

Click:

```bash
Create Peering Connection
```

---

# PART 3 — Accept Peering Request

Login to **Account B**

Navigate to:

```bash
VPC → Peering Connections
```

You will see:

```bash
Pending Acceptance
```

Select the peering request.

Click:

```bash
Actions → Accept Request
```

Status becomes:

```bash
Active
```

---

# PART 4 — Update Route Table in Account A

Navigate to:

```bash
VPC → Route Tables
```

Find the route table attached to:

```bash
10.0.1.0/24
```

---

## Add Route

| Destination | Target |
|---|---|
| 11.0.0.0/16 | pcx-xxxxxxxx |

Example:

```bash
11.0.0.0/16 → pcx-01a155902940a7038
```

Save changes.

---

# PART 5 — Update Route Table in Account B

Navigate to:

```bash
VPC → Route Tables
```

Find the route table attached to:

```bash
11.0.1.0/24
```

---

## Add Route

| Destination | Target |
|---|---|
| 10.0.0.0/16 | pcx-xxxxxxxx |

Example:

```bash
10.0.0.0/16 → pcx-01a155902940a7038
```

Save changes.

---

# PART 6 — Configure Security Groups

## Account B EC2 Security Group

Add inbound rules:

| Type | Port | Source |
|---|---|---|
| SSH | 22 | 10.0.0.0/16 |
| All ICMP IPv4 | All | 10.0.0.0/16 |

---

## Account A EC2 Security Group

(Optional ping rule)

| Type | Source |
|---|---|
| All ICMP IPv4 | 11.0.0.0/16 |

---

# PART 7 — Test Connectivity

Login to:

```bash
EC2-A (10.0.1.214)
```

---

## Step 7.1 — Ping EC2-B

Run:

```bash
ping 11.0.1.109
```

Expected output:

```bash
64 bytes from 11.0.1.109
```

---

## Step 7.2 — SSH into EC2-B

### Amazon Linux

```bash
ssh -i key.pem ec2-user@11.0.1.109
```

### Ubuntu

```bash
ssh -i key.pem ubuntu@11.0.1.109
```

---

# ✅ Final Result

Successfully established:

- Cross-Account VPC Peering
- Private EC2 Communication
- Secure Internal Networking

---

# 🧠 Key Concepts Learned

- AWS VPC Peering
- Cross-Account Networking
- Route Tables
- Security Groups
- Private Communication
- CIDR Routing
- AWS Networking Fundamentals

---

# ⚠️ Important Notes

- CIDR blocks must NOT overlap
- VPC Peering is non-transitive
- Security Groups must allow traffic
- Route tables are mandatory for communication

---

# 📷 Suggested Screenshots to Add

You can improve this repo by adding screenshots for:

- VPC Creation
- Peering Request
- Peering Acceptance
- Route Tables
- Security Groups
- Ping Test
- SSH Connection

Recommended folder structure:

```bash
images/
├── architecture.png
├── peering-active.png
├── route-table-a.png
├── route-table-b.png
├── ping-test.png
└── ssh-success.png
```

---

# 📚 AWS Services Used

- Amazon VPC
- EC2
- Route Tables
- Security Groups
- VPC Peering

---

# 👨‍💻 Author

## Rohith

AWS | Cloud | Networking | DevOps Enthusiast

---

# ⭐ Repository Purpose

This repository is created for:

- AWS Networking Practice
- Interview Preparation
- Cloud Portfolio Projects
- Learning Cross-Account Connectivity

---

# 📌 Tags

`AWS` `VPC` `VPC-Peering` `Cross-Account` `EC2` `Networking` `Cloud` `DevOps`

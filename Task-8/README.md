# 🌍 Multi-Region AWS Transit Gateway Setup

<div align="center">

![AWS](https://img.shields.io/badge/AWS-Transit_Gateway-orange?style=for-the-badge&logo=amazonaws)
![Multi Region](https://img.shields.io/badge/Multi--Region-Networking-blue?style=for-the-badge)
![TGW](https://img.shields.io/badge/TGW-Full_Mesh-success?style=for-the-badge)
![VPC](https://img.shields.io/badge/VPC-Cross_Region-important?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

</div>

---

## 📌 Overview

This project demonstrates a **Multi-Region AWS Network Architecture** using:

- AWS Transit Gateway (TGW)
- TGW Peering
- Cross-Region VPC Connectivity
- SSH Connectivity Between Regions

### 🌐 Regions Used

| Region | Code | CIDR |
|---|---|---|
| Mumbai | `ap-south-1` | `10.0.0.0/16` |
| Hyderabad | `ap-south-2` | `11.0.0.0/16` |
| N. Virginia | `us-east-1` | `12.0.0.0/16` |

---

# 🏗️ Architecture Diagram

```text
                         ┌────────────────────┐
                         │      AWS CLOUD     │
                         └────────────────────┘


      ┌──────────────────────┐        TGW Peering       ┌──────────────────────┐
      │    Mumbai Region     │◄────────────────────────►│  Hyderabad Region    │
      │     ap-south-1       │                          │     ap-south-2       │
      └──────────────────────┘                          └──────────────────────┘
                 │                                                   │
         ┌───────▼────────┐                                 ┌────────▼───────┐
         │   Mumbai TGW   │◄──────── TGW Peering ─────────►│ Hyderabad TGW  │
         └───────┬────────┘                                 └────────┬───────┘
                 │                                                   │
         ┌───────▼────────┐                                 ┌────────▼───────┐
         │   Mumbai VPC   │                                 │ Hyderabad VPC  │
         │  10.0.0.0/16   │                                 │  11.0.0.0/16   │
         └───────┬────────┘                                 └────────┬───────┘
                 │                                                   │
         ┌───────▼────────┐                                 ┌────────▼───────┐
         │   Mumbai EC2   │                                 │ Hyderabad EC2  │
         └────────────────┘                                 └────────────────┘


                         TGW Peering
      ┌──────────────────────────────────────────────────────────────┐
      ▼                                                              ▼


                  ┌────────────────────────────┐
                  │   N. Virginia Region       │
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
                           │  Virginia EC2  │
                           └────────────────┘
```

---

## 🚀 Services Used

- Amazon VPC
- Amazon EC2
- AWS Transit Gateway
- Transit Gateway Peering
- Internet Gateway
- Route Tables
- Security Groups

---

## 🛠️ Infrastructure Components

### ✅ VPCs

| Region | VPC Name | CIDR |
|---|---|---|
| Mumbai | `mumbai-vpc` | `10.0.0.0/16` |
| Hyderabad | `hyderabad-vpc` | `11.0.0.0/16` |
| Virginia | `virginia-vpc` | `12.0.0.0/16` |

---

### ✅ Public Subnets

| Region | Subnet | CIDR |
|---|---|---|
| Mumbai | `10.0.1.0/24` |
| Hyderabad | `11.0.1.0/24` |
| Virginia | `12.0.1.0/24` |

---

### ✅ EC2 Instances

| Region | Instance |
|---|---|
| Mumbai | `mumbai-ec2` |
| Hyderabad | `hyderabad-ec2` |
| Virginia | `virginia-ec2` |

---

### ✅ Transit Gateways

| Region | TGW |
|---|---|
| Mumbai | `mumbai-tgw` |
| Hyderabad | `hyderabad-tgw` |
| Virginia | `virginia-tgw` |

---

## 🔗 TGW Peering Connections

| Source TGW | Destination TGW |
|---|---|
| Mumbai TGW | Hyderabad TGW |
| Mumbai TGW | Virginia TGW |
| Hyderabad TGW | Virginia TGW |

---

## 🛣️ Route Configuration

### TGW Route Tables

Configured with:

- Local VPC CIDR
- Remote VPC CIDRs
- TGW Peering Attachments

### VPC Route Tables

Configured with:

- Cross-region CIDR routes
- Transit Gateway targets

---

## 🔐 Security Group Rules

| Type | Source |
|---|---|
| SSH (22) | `0.0.0.0/0` |
| ICMP | `0.0.0.0/0` |

---

## 🧪 Connectivity Testing

### Connect to Mumbai EC2

```bash
ssh -i mumbai-key.pem ec2-user@MUMBAI-PUBLIC-IP
```

### SSH From Mumbai → Hyderabad

```bash
ssh -i hyderabad-key.pem ec2-user@11.0.1.X
```

### SSH From Mumbai → Virginia

```bash
ssh -i virginia-key.pem ec2-user@12.0.1.X
```

---

## 🧠 Key Learning

### Why Full Mesh Peering?

AWS Transit Gateway Peering is:

- ❌ NOT Transitive
- ✅ Direct Region-to-Region Connectivity

Therefore:

- Mumbai cannot automatically communicate with Virginia through Hyderabad.
- Direct TGW peering is required between all regions.

---

## 📘 Real-World Use Cases

- Multi-Region Enterprise Networks
- Disaster Recovery Architecture
- Hybrid Cloud Networking
- Global Infrastructure Design
- Cross-Region Application Communication

---

## 📂 Project Structure

```bash
project/
│
├── README.md
│
├── docs/
│   └── 8.Multi-Region Transit Gateway Setup.docx

```

---

## 📄 Documentation

Detailed setup steps are available inside:

```bash
docs/8.Multi-Region Transit Gateway Setup.docx
```

Reference documentation provided by the user :contentReference[oaicite:0]{index=0}

---

## ✅ Final Result

✔ Multi-Region Connectivity Achieved  
✔ Full Mesh TGW Peering Configured  
✔ Cross-Region SSH Connectivity Working  
✔ Private Routing Between Regions Enabled  
✔ Scalable AWS Network Architecture Built  

---

## 👨‍💻 Author

**Rohith**

AWS | Cloud | Networking | DevOps Enthusiast

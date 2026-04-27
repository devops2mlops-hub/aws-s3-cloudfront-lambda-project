# 🚀 AWS Full Stack Deployment (S3 + CloudFront + Lambda + API Gateway)

![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![Serverless](https://img.shields.io/badge/Architecture-Serverless-blue)
![Frontend](https://img.shields.io/badge/Frontend-S3%20%2B%20CloudFront-green)
![Backend](https://img.shields.io/badge/Backend-Lambda%20%2B%20API%20Gateway-yellow)
![Status](https://img.shields.io/badge/Project-Production%20Ready-brightgreen)

---

## 📌 Overview

This project demonstrates how to build and deploy a **production-grade full stack application on AWS** using **serverless architecture**.

---

## 🧱 Architecture Diagram

![Architecture](architecture.png)

---

## 🧠 What is Serverless?

Serverless means:
- No server management
- Auto scaling
- Pay only when used

---

## 🏗️ Architecture Flow

### 🌐 Frontend
User → DNS → CloudFront → S3

### ⚙️ Backend
User → API Gateway → Lambda → Response

---

## ⚔️ Traditional vs Serverless

| Feature        | EC2 Based        | Serverless |
|---------------|-----------------|------------|
| Server Mgmt   | Required        | Not needed |
| Scaling       | Manual          | Automatic  |
| Cost          | Always running  | Pay per use |
| Maintenance   | High            | Low        |


aws-s3-cloudfront-lambda-project/
│
├── frontend/
│ ├── index.html
│ └── script.js
│
├── backend/
│ ├── app.js
│ ├── lambda-handler.js
│ └── package.json
│
├── docs/
│ ├── frontend-setup.docx
│ └── backend-setup.docx
│
├── architecture.png
└── README.md



---

## 🚀 Setup Guide

### 🔹 Frontend (S3 + CloudFront)

- Create S3 bucket  
- Upload static files  
- Enable static hosting  
- Create CloudFront  
- Attach ACM SSL  
- Connect domain  

---

### 🔹 Backend (Lambda + API Gateway)

- Create Lambda  
- Upload ZIP  
- Create API Gateway  
- Add routes:
  - ANY /
  - ANY /{proxy+}
- Deploy API  
- Add custom domain  

---

## 🔐 SSL Setup

- Frontend → us-east-1  
- Backend → ap-south-1  
- Use DNS validation  

---

## 🧪 Output

Frontend:

https://www.yourdomain.com


Backend:

https://api.yourdomain.com


---

## 📄 Documentation

- Frontend Setup → docs/frontend-setup.docx  
- Backend Setup → docs/backend-setup.docx  

---

## 🎯 Key Learnings

- S3 static hosting  
- CloudFront CDN  
- Serverless backend  
- API Gateway routing  
- SSL using ACM  
- DNS configuration  

---

## 🚀 Future Improvements

- Add DynamoDB / RDS  
- Add authentication (JWT)  
- Add CI/CD  
- Add monitoring  

---

## 👨‍💻 Author

Rohith

<img width="1358" height="679" alt="NDgsmKkvf7OtHYh7Grmq6Z2XadSRDUOTWD-vD21efbRrkSI6_TklxgygUQ3chB5BjzE1Y-xyDD8IdPCVCDgg8aNUP0XjGE7XSCC_DwMYRwQVCGDvGVtOVVd5m3H1KdTEcPhXiTJTu_kmxo_3GnObJnqmpugbLFJsZUJzydfQ_X_RiPHvY7KvlT69Ov3qtlbh" src="https://github.com/user-attachments/assets/ab45799d-aa61-4be0-9c84-ac47f4cf49ea" />


---

## 📁 Project Structure

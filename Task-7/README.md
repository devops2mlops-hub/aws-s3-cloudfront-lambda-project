# Cross-Account EC2 → S3 Access in AWS
![AWS](https://img.shields.io/badge/AWS-S3%20Cross%20Account-orange?style=for-the-badge&logo=amazonaws)
![Service](https://img.shields.io/badge/Service-Amazon%20S3-blue?style=for-the-badge)
![Compute](https://img.shields.io/badge/Compute-EC2-yellow?style=for-the-badge&logo=amazon-ec2)
![Security](https://img.shields.io/badge/Security-IAM-red?style=for-the-badge)
![Access](https://img.shields.io/badge/Access-Cross%20Account-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-yellow?style=for-the-badge)
## Architecture Diagram with Labels

# CASE 1 — Public Bucket Access

```text
┌──────────────────────────────────────────────┐
│              AWS ACCOUNT A                  │
│                                              │
│  ┌──────────────────────────────────────┐    │
│  │            EC2 INSTANCE              │    │
│  │                                      │    │
│  │  AWS CLI Commands                    │    │
│  │  aws s3 ls                           │    │
│  │  aws s3 cp                           │    │
│  └──────────────────────────────────────┘    │
└──────────────────────────────────────────────┘
                     │
                     │ Public Internet Access
                     │
                     ▼
┌──────────────────────────────────────────────┐
│              AWS ACCOUNT B                  │
│                                              │
│  ┌──────────────────────────────────────┐    │
│  │          PUBLIC S3 BUCKET            │    │
│  │                                      │    │
│  │  Bucket Name: portfolio-rohith       │    │
│  │                                      │    │
│  │  Permissions:                        │    │
│  │  ✅ s3:GetObject                     │    │
│  │  ✅ s3:ListBucket                    │    │
│  │  ❌ Public Upload                    │    │
│  └──────────────────────────────────────┘    │
└──────────────────────────────────────────────┘
```

---

# CASE 2 — Private Bucket Access using IAM Role

```text
┌──────────────────────────────────────────────┐
│              AWS ACCOUNT A                  │
│                                              │
│  ┌──────────────────────────────────────┐    │
│  │            EC2 INSTANCE              │    │
│  │                                      │    │
│  │  Attached IAM Role:                  │    │
│  │  ec2-s3-FACcess                      │    │
│  │                                      │    │
│  │  Temporary Credentials via STS       │    │
│  └──────────────────────────────────────┘    │
└──────────────────────────────────────────────┘
                     │
                     │ Cross-Account IAM Access
                     │
                     ▼
┌──────────────────────────────────────────────┐
│              AWS ACCOUNT B                  │
│                                              │
│  ┌──────────────────────────────────────┐    │
│  │         PRIVATE S3 BUCKET            │    │
│  │                                      │    │
│  │  Bucket Policy Allows:               │    │
│  │  IAM Role ARN                        │    │
│  │                                      │    │
│  │  Allowed Actions:                    │    │
│  │  ✅ s3:GetObject                     │    │
│  │  ✅ s3:PutObject                     │    │
│  │  ✅ s3:ListBucket                    │    │
│  └──────────────────────────────────────┘    │
└──────────────────────────────────────────────┘
```

---

# CASE 3 — Private Bucket Access using IAM User

```text
┌──────────────────────────────────────────────┐
│              AWS ACCOUNT A                  │
│                                              │
│  ┌──────────────────────────────────────┐    │
│  │              IAM USER                │    │
│  │                                      │    │
│  │  User Name: New-user                 │    │
│  │                                      │    │
│  │  AWS CLI Credentials                 │    │
│  │  Access Key + Secret Key             │    │
│  └──────────────────────────────────────┘    │
└──────────────────────────────────────────────┘
                     │
                     │ Cross-Account Access
                     │
                     ▼
┌──────────────────────────────────────────────┐
│              AWS ACCOUNT B                  │
│                                              │
│  ┌──────────────────────────────────────┐    │
│  │         PRIVATE S3 BUCKET            │    │
│  │                                      │    │
│  │  Bucket Policy Allows:               │    │
│  │  IAM User ARN                        │    │
│  │                                      │    │
│  │  Allowed Actions:                    │    │
│  │  ✅ s3:GetObject                     │    │
│  │  ✅ s3:PutObject                     │    │
│  │  ✅ s3:ListBucket                    │    │
│  └──────────────────────────────────────┘    │
└──────────────────────────────────────────────┘
```

---

# Project Overview

This project demonstrates how resources from one AWS account can securely access Amazon S3 buckets located in another AWS account.

The project covers:

1. Public S3 Bucket Access
2. Private S3 Bucket Access using IAM Role
3. Private S3 Bucket Access using IAM User

---

# AWS Services Used

- Amazon EC2
- Amazon S3
- IAM Roles
- IAM Policies
- Bucket Policies
- AWS CLI

---

# CASE 1 — Access PUBLIC S3 Bucket

## Objective

Allow EC2 in Account A to access a PUBLIC S3 bucket in Account B.

---

## Step 1 — Create S3 Bucket

Navigate to:

```text
S3 → Create Bucket
```

Example bucket name:

```text
portfolio-rohith
```

Upload sample files.

---

## Step 2 — Disable Block Public Access

Navigate to:

```text
Bucket → Permissions
```

Disable:

```text
Block all public access
```

Save changes.

---

## Step 3 — Add Bucket Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadAccess",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::portfolio-rohith",
        "arn:aws:s3:::portfolio-rohith/*"
      ]
    }
  ]
}
```

---

## Step 4 — Access from EC2

### List Bucket

```bash
aws s3 ls s3://portfolio-rohith --no-sign-request
```

### Download File

```bash
aws s3 cp s3://portfolio-rohith/test.txt . --no-sign-request
```

---

## Important Notes

### Public Bucket Permissions

✅ Read Access  
✅ List Access  
❌ Upload Access normally blocked

---

# CASE 2 — Access PRIVATE Bucket using IAM Role

## Objective

Allow EC2 instance in Account A to securely access private S3 bucket in Account B using IAM Role.

---

## Step 1 — Create IAM Role

Navigate to:

```text
IAM → Roles → Create Role
```

Choose:

- AWS Service
- EC2

---

## Step 2 — Attach Policy

Attach:

```text
AmazonS3ReadOnlyAccess
```

OR create custom policy.

Example role name:

```text
ec2-s3-FACcess
```

---

## Step 3 — Attach Role to EC2

Navigate to:

```text
EC2 → Instances
```

Select instance:

```text
Actions → Security → Modify IAM Role
```

Attach:

```text
ec2-s3-FACcess
```

Save changes.

---

## Step 4 — Add Bucket Policy in Account B

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ListBucketPermission",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::489449993146:role/ec2-s3-FACcess"
      },
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::portfolio-rohith"
    },
    {
      "Sid": "ObjectPermissions",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::489449993146:role/ec2-s3-FACcess"
      },
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::portfolio-rohith/*"
    }
  ]
}
```

---

## Step 5 — Verify Access

### Verify IAM Role

```bash
aws sts get-caller-identity
```

### List Bucket

```bash
aws s3 ls s3://portfolio-rohith
```

### Upload File

```bash
echo "hello" > test.txt
aws s3 cp test.txt s3://portfolio-rohith/
```

### Download File

```bash
aws s3 cp s3://portfolio-rohith/test.txt .
```

---

# CASE 3 — Access PRIVATE Bucket using IAM User

## Objective

Allow IAM User from Account A to access private S3 bucket in Account B.

---

## Step 1 — Create IAM User

Navigate to:

```text
IAM → Users → Create User
```

Example username:

```text
New-user
```

Enable:

```text
Programmatic Access
```

---

## Step 2 — Create Access Keys

Navigate to:

```text
IAM → Users → Security Credentials
```

Create:
- Access Key ID
- Secret Access Key

---

## Step 3 — Attach IAM Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetBucketLocation",
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::portfolio-rohith"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::portfolio-rohith/*"
    }
  ]
}
```

---

## Step 4 — Add Bucket Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCrossAccountUser",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::489449993146:user/New-user"
      },
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::portfolio-rohith"
    },
    {
      "Sid": "AllowObjectAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::489449993146:user/New-user"
      },
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::portfolio-rohith/*"
    }
  ]
}
```

---

## Step 5 — Configure AWS CLI

```bash
aws configure
```

Provide:
- Access Key
- Secret Key
- Region

---

## Step 6 — Verify User

```bash
aws sts get-caller-identity
```

---

## Step 7 — Access Bucket

### List Bucket

```bash
aws s3 ls s3://portfolio-rohith
```

### Upload File

```bash
echo "hello" > test.txt
aws s3 cp test.txt s3://portfolio-rohith/
```

### Download File

```bash
aws s3 cp s3://portfolio-rohith/test.txt .
```

---

# Important Configuration Changes

## Replace Bucket Name

Replace:

```text
portfolio-rohith
```

with your bucket name.

Example:

```text
arn:aws:s3:::your-bucket-name
arn:aws:s3:::your-bucket-name/*
```

---

## Replace AWS Account ID

Replace:

```text
489449993146
```

with your AWS Account ID.

Example:

```text
arn:aws:iam::<YOUR-ACCOUNT-ID>:role/ec2-s3-FACcess
```

---

## Replace IAM Role Name

Replace:

```text
ec2-s3-FACcess
```

with your IAM Role name.

Example:

```text
arn:aws:iam::<ACCOUNT-ID>:role/<YOUR-ROLE-NAME>
```

---

## Replace IAM User Name

Replace:

```text
New-user
```

with your IAM User name.

Example:

```text
arn:aws:iam::<ACCOUNT-ID>:user/<YOUR-USER-NAME>
```

---

## Replace File Name

Replace:

```text
test.txt
```

with your desired filename.

---

# AWS CLI Requirement

Install AWS CLI on:
- EC2 Instance
- Local Machine

Verify installation:

```bash
aws --version
```

---

# Required Permissions

## IAM Role Permissions

- s3:ListBucket
- s3:GetObject
- s3:PutObject

## IAM User Permissions

- s3:GetBucketLocation
- s3:ListBucket
- s3:GetObject
- s3:PutObject

---

# Common Errors

## AccessDenied

Possible reasons:
- Wrong bucket policy
- Wrong IAM permissions
- Incorrect ARN
- IAM role not attached

---

## Unable to Locate Credentials

Possible reasons:
- AWS CLI not configured
- Access keys missing
- IAM role not attached

---

## NoSuchBucket

Possible reasons:
- Incorrect bucket name
- Wrong region

---

# Security Best Practices

## Recommended Method

✅ IAM Role Access

Reasons:
- Uses temporary credentials
- No hardcoded access keys
- More secure
- AWS recommended

---

# Comparison Table

| Feature | Public Bucket | IAM Role | IAM User |
|---|---|---|---|
| IAM Required | No | Yes | Yes |
| Security | Low | High | Medium |
| Upload Allowed | Usually No | Yes | Yes |
| Credentials | None | Temporary | Access Keys |
| Recommended | No | Yes | Limited Use |

---

# Recommended Folder Structure

```text
project/
│
├── README.md
├── docs/
│   └── Cross Account Ec2 -S3 Access.docx
├── screenshots/
│   ├── architecture.png
│   ├── public-bucket.png
│   ├── iam-role-access.png
│   └── iam-user-access.png
└── policies/
    ├── public-bucket-policy.json
    ├── iam-role-policy.json
    └── iam-user-policy.json
```

---

# Author

Rohith

# Cross-Account EC2 → S3 Access in AWS

## Project Overview

This project demonstrates how an EC2 instance or IAM User from one AWS account can access an S3 bucket located in another AWS account.

The implementation covers three different scenarios:

1. Public S3 Bucket Access
2. Private S3 Bucket Access using IAM Role (Recommended)
3. Private S3 Bucket Access using IAM User

---

# Architecture Overview

AWS Account A contains:
- EC2 Instance
- IAM Role / IAM User

AWS Account B contains:
- S3 Bucket

Cross-account permissions are controlled using:
- Bucket Policies
- IAM Policies
- IAM Roles
- Access Keys

---

# CASE 1 — Public S3 Bucket Access

## Objective

Allow EC2 in Account A to access a PUBLIC S3 bucket in Account B.

## Architecture

EC2 (Account A)
        |
 Public Internet
        |
Public S3 Bucket (Account B)

---

## Step 1 — Create S3 Bucket

Go to:

S3 → Create Bucket

Example:

portfolio-rohith

Upload sample files.

---

## Step 2 — Disable Block Public Access

Go to:

Bucket → Permissions

Disable:
- Block all public access

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
````

---

## Step 4 — Test from EC2

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

### Public Bucket Access

✅ Read Access
❌ Upload Access normally blocked

Reason:
Public upload is insecure.

---

# CASE 2 — Private Bucket Access using IAM Role (Recommended)

## Objective

Allow EC2 instance in Account A to securely access private S3 bucket in Account B using IAM Role.

---

## Architecture

EC2 (Account A)
|
IAM Role
|
Private S3 Bucket (Account B)

---

## Step 1 — Create IAM Role

Go to:

IAM → Roles → Create Role

Choose:

* AWS Service
* EC2

---

## Step 2 — Attach Policy

Attach:

AmazonS3ReadOnlyAccess

OR create custom S3 policy.

Example role name:

ec2-s3-FACcess

---

## Step 3 — Attach Role to EC2

Go to:

EC2 → Instances

Select instance:

Actions → Security → Modify IAM Role

Attach:

* ec2-s3-FACcess

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

### Download File

```bash
aws s3 cp s3://portfolio-rohith/test.txt .
```

### Upload File

```bash
echo "hello" > test.txt
aws s3 cp test.txt s3://portfolio-rohith/
```

---

# CASE 3 — IAM User Accessing Private S3 Bucket

## Objective

Allow IAM User from Account A to access private S3 bucket in Account B.

---

## Architecture

IAM User (Account A)
|
AWS CLI Credentials
|
Private S3 Bucket (Account B)

---

## Step 1 — Create IAM User

Go to:

IAM → Users → Create User

Example:

* New-user

Enable:

* Programmatic Access

---

## Step 2 — Create Access Keys

Go to:

IAM → Users → Security Credentials

Create:

* Access Key ID
* Secret Access Key

Save credentials securely.

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

* Access Key
* Secret Key
* Region

---

## Step 6 — Verify User

```bash
aws sts get-caller-identity
```

---

## Step 7 — List Bucket

```bash
aws s3 ls s3://portfolio-rohith
```

---

## Step 8 — Upload File

```bash
echo "hello" > test.txt
aws s3 cp test.txt s3://portfolio-rohith/
```

---

## Step 9 — Download File

```bash
aws s3 cp s3://portfolio-rohith/test.txt .
```

---

# Security Best Practices

## Recommended Approach

✅ IAM Role Method

Reasons:

* Temporary credentials
* No hardcoded access keys
* More secure
* AWS recommended

---

# Comparison Table

| Feature        | Public Bucket | IAM Role  | IAM User    |
| -------------- | ------------- | --------- | ----------- |
| IAM Required   | No            | Yes       | Yes         |
| Security       | Low           | High      | Medium      |
| Upload Allowed | Usually No    | Yes       | Yes         |
| Credentials    | None          | Temporary | Access Keys |
| Recommended    | No            | Yes       | Limited Use |

---

# AWS Services Used

* Amazon EC2
* Amazon S3
* IAM Roles
* IAM Policies
* Bucket Policies
* AWS CLI

---

# Author

Rohith

````

---

# Architecture Diagram Ideas

## CASE 1 — Public Bucket

```text
+------------------------+
| AWS Account A          |
|                        |
|  EC2 Instance          |
+-----------+------------+
            |
            | Public Internet
            |
+-----------v------------+
| AWS Account B          |
|                        |
| Public S3 Bucket       |
| portfolio-rohith       |
+------------------------+
````

---

## CASE 2 — IAM Role Access

```text
+------------------------+
| AWS Account A          |
|                        |
| EC2 Instance           |
|     |                  |
| IAM Role Attached      |
+-----------+------------+
            |
            | Cross Account Access
            |
+-----------v------------+
| AWS Account B          |
|                        |
| Private S3 Bucket      |
| Bucket Policy Allowing |
| IAM Role ARN           |
+------------------------+
```

---

## CASE 3 — IAM User Access

```text
+------------------------+
| AWS Account A          |
|                        |
| IAM User               |
| Access Keys            |
| AWS CLI                |
+-----------+------------+
            |
            | Cross Account Access
            |
+-----------v------------+
| AWS Account B          |
|                        |
| Private S3 Bucket      |
| Bucket Policy Allowing |
| IAM User ARN           |
+------------------------+
```

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

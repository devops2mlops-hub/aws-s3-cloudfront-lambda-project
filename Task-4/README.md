# 🔄 Log Rotation & Automated S3 Upload (AWS + Linux)

![AWS](https://img.shields.io/badge/AWS-S3-orange?logo=amazonaws)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-yellow?logo=linux)
![Automation](https://img.shields.io/badge/Automation-Cron-blue)
![Logging](https://img.shields.io/badge/Logs-Logrotate-green)

---

## 📌 Project Overview

This project demonstrates a **complete log management system** using:

* Log generation via Python application
* Log rotation using Linux `logrotate`
* Automated upload of rotated logs to **Amazon S3**
* Scheduled execution using `cron`

---

## 🧱 Architecture Flow

```id="flow1"
Application → Log Files → Logrotate → Compressed Logs → Cron Job → S3 Upload → Cleanup
```

---

## 📁 Log Directory Setup

```bash id="cmd1"
sudo mkdir -p /var/log/myapp
sudo chown root:root /var/log/myapp
sudo chmod 755 /var/log/myapp
```

---

## 🐍 Sample Logging Application

```python id="code1"
import logging
import time

logging.basicConfig(
    filename='/var/log/myapp/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

while True:
    logging.info("This is a sample log message")
    time.sleep(2)
```

---

## ▶️ Run Application in Background

```bash id="cmd2"
nohup python3 app.py > /var/log/myapp/app.log 2>&1 &
```

Verify:

```bash id="cmd3"
ps aux | grep app.py
tail -f /var/log/myapp/app.log
```

---

## 🔧 Install Logrotate

```bash id="cmd4"
sudo apt update
sudo apt install logrotate -y
```

---

## ⚙️ Configure Logrotate

Create config file:

```bash id="cmd5"
sudo nano /etc/logrotate.d/myapp
```

```bash id="code2"
/var/log/myapp/*.log {
    size 1k
    rotate 5
    compress
    missingok
    notifempty
    create 0644 root root
}
```

---

## 🧪 Test Log Rotation

```bash id="cmd6"
sudo logrotate -f /etc/logrotate.d/myapp
ls /var/log/myapp
```

Expected:

```id="exp1"
app.log
app.log.1.gz
```

---

## ☁️ AWS S3 Setup

Create an S3 bucket:

```id="bucket1"
myapp-logs-bucket-123
```

---

## 🔐 IAM Role Policy

Attach to EC2:

```json id="json1"
{
  "Effect": "Allow",
  "Action": [
    "s3:PutObject",
    "s3:ListBucket"
  ],
  "Resource": [
    "arn:aws:s3:::myapp-logs-bucket-123",
    "arn:aws:s3:::myapp-logs-bucket-123/*"
  ]
}
```

---

## 🛠️ Install AWS CLI

```bash id="cmd7"
sudo apt install awscli -y
aws s3 ls
```

---

## 📤 Upload Script

```bash id="cmd8"
sudo nano /usr/local/bin/upload_to_s3.sh
```

```bash id="code3"
#!/bin/bash

BUCKET="myapp-logs-bucket-123"
LOG_DIR="/var/log/myapp"

for file in $LOG_DIR/*.gz
do
    [ -e "$file" ] || continue

    aws s3 cp "$file" s3://$BUCKET/$(hostname)/$(date +%F)/$(basename $file)

    if [ $? -eq 0 ]; then
        rm -f "$file"
    fi
done
```

---

## 🔑 Set Permissions

```bash id="cmd9"
sudo chmod +x /usr/local/bin/upload_to_s3.sh
sudo chown root:root /usr/local/bin/upload_to_s3.sh
```

---

## 🧪 Test Upload

```bash id="cmd10"
/usr/local/bin/upload_to_s3.sh
aws s3 ls s3://myapp-logs-bucket-123
```

---

## ⏰ Setup Cron Job

```bash id="cmd11"
sudo crontab -e
```

Add:

```bash id="code4"
*/5 * * * * /usr/local/bin/upload_to_s3.sh >> /var/log/myapp/upload.log 2>&1
```

---

## 🔍 Verify Cron

```bash id="cmd12"
sudo crontab -l
tail -f /var/log/myapp/upload.log
```

---

## 🔄 Final Workflow

```id="flow2"
App running → logs generated
      ↓
logrotate rotates & compresses
      ↓
cron runs every 5 minutes
      ↓
script uploads to S3
      ↓
local logs removed
```

---

## 🎯 Key Features

* Automated log rotation
* Compressed log storage
* Scheduled S3 uploads
* Cleanup of local logs
* Fully automated pipeline

---

## 📄 Reference Document

Detailed setup available here:


---

## 👨‍💻 Author

**Rohith**

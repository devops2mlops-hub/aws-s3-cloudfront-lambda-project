# 🔄 Log Rotation & Automated S3 Upload (AWS + Linux)

![AWS](https://img.shields.io/badge/AWS-S3-orange?logo=amazonaws)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-yellow?logo=linux)
![Automation](https://img.shields.io/badge/Cron-Automation-blue)
![Logging](https://img.shields.io/badge/Logrotate-Enabled-green)

---

## 📌 Project Overview

This project implements an automated **log management system**:

* Python app generates logs
* Logrotate rotates & compresses logs
* Cron job triggers upload script
* Logs are uploaded to Amazon S3
* Local logs are cleaned automatically

---

## 📁 Project Structure

```bash
log-rotate-project/
│
├── app/
│   └── app.py
│
├── scripts/
│   └── upload_to_s3.sh
│
├── config/
│   └── logrotate_myapp.conf
│
├── docs/
│   └── Log-Rotate-Setup.docx
│
├── README.md
```

---

## 🧱 Architecture Flow

```text
Python App → Log File → Logrotate → Compressed Logs → Cron → S3 Upload → Cleanup
```

---

## ⚙️ Setup Steps

### 1️⃣ Create Log Directory

```bash
sudo mkdir -p /var/log/myapp
sudo chmod 755 /var/log/myapp
```

---

### 2️⃣ Run Python App

```bash
nohup python3 app/app.py > /var/log/myapp/app.log 2>&1 &
```

---

### 3️⃣ Install Logrotate

```bash
sudo apt update
sudo apt install logrotate -y
```

---

### 4️⃣ Configure Logrotate

```bash
sudo cp config/logrotate_myapp.conf /etc/logrotate.d/myapp
```

---

### 5️⃣ Test Rotation

```bash
sudo logrotate -f /etc/logrotate.d/myapp
```

---

### 6️⃣ Setup AWS S3

* Create bucket: `myapp-logs-bucket-123`
* Attach IAM role to EC2

---

### 7️⃣ Install AWS CLI

```bash
sudo apt install awscli -y
```

---

### 8️⃣ Setup Upload Script

```bash
sudo cp scripts/upload_to_s3.sh /usr/local/bin/
sudo chmod +x /usr/local/bin/upload_to_s3.sh
```

---

### 9️⃣ Setup Cron Job

```bash
sudo crontab -e
```

```bash
*/5 * * * * /usr/local/bin/upload_to_s3.sh >> /var/log/myapp/upload.log 2>&1
```

---

## 🎯 Key Features

* Automated log rotation
* Log compression
* Scheduled S3 uploads
* Log cleanup
* Fully automated pipeline

---

## 📄 Documentation

Detailed steps available in:

* `docs/Log-Rotate-Setup.docx`

---

## 👨‍💻 Author

**Rohith**

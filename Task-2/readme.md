# 🚀 AWS Smart Inventory Alert System

## 📌 Project Overview

This project implements a **real-time inventory monitoring system** for an e-commerce warehouse using AWS services.

It automatically detects **low stock levels** and sends alerts to warehouse managers via email.

---

## 🧠 Problem Statement

In large-scale warehouse systems:

* Manual stock checking is inefficient
* Low stock leads to:

  * Order failures
  * Revenue loss
  * Poor customer experience

---

## 💡 Solution

This system automates stock monitoring using AWS:

* Stores inventory in **DynamoDB**
* Periodically checks stock using **Lambda**
* Sends alerts via **SNS**
* Triggered automatically using **EventBridge**

---

## 🏗️ Architecture

DynamoDB → EventBridge → Lambda → SNS → Email
<img width="1693" height="929" alt="dd13d192-8e64-4659-86b7-565e4d64ffcb" src="https://github.com/user-attachments/assets/45dd9b71-4d71-4320-990f-6a649272d5a4" />


---


## ⚙️ AWS Services Used

* Amazon DynamoDB
* AWS Lambda
* Amazon SNS
* Amazon EventBridge

---

## 🔧 Setup Instructions

### 1. Create DynamoDB Table

* Table Name: `InventoryTable`
* Partition Key: `product_id`

---

### 2. Insert Sample Data

Example:

```json
[
  {
    "product_id": "P001",
    "product_name": "Rice Bag",
    "stock": 5,
    "threshold": 10
  },
  {
    "product_id": "P002",
    "product_name": "Wheat Flour",
    "stock": 20,
    "threshold": 15
  },
  {
    "product_id": "P003",
    "product_name": "Cooking Oil",
    "stock": 8,
    "threshold": 12
  },
  {
    "product_id": "P004",
    "product_name": "Milk Pack",
    "stock": 30,
    "threshold": 25
  },
  {
    "product_id": "P005",
    "product_name": "Sugar",
    "stock": 3,
    "threshold": 10
  },
  {
    "product_id": "P006",
    "product_name": "Salt",
    "stock": 50,
    "threshold": 20
  },
  {
    "product_id": "P007",
    "product_name": "Tea Powder",
    "stock": 6,
    "threshold": 10
  },
  {
    "product_id": "P008",
    "product_name": "Coffee Powder",
    "stock": 18,
    "threshold": 15
  },
  {
    "product_id": "P009",
    "product_name": "Biscuits Pack",
    "stock": 2,
    "threshold": 8
  },
  {
    "product_id": "P010",
    "product_name": "Vegetable Oil",
    "stock": 25,
    "threshold": 20
  }
]
```

---

### 3. Create SNS Topic

* Name: `InventoryAlerts`
* Subscribe using Email

---

### 4. Create Lambda Function

Runtime: Python 3.x

```python
import boto3

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

TABLE_NAME = "InventoryTable"
SNS_TOPIC_ARN = "YOUR_ARN"

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)

    response = table.scan()
    items = response.get('Items', [])

    low_stock_items = []

    for item in items:
        stock = int(item.get('stock', 0))
        threshold = int(item.get('threshold', 0))

        if stock < threshold:
            low_stock_items.append(item)

    if low_stock_items:
        message = "Low Stock Alert:\n\n"

        for i in low_stock_items:
            message += f"{i.get('product_name')} - Stock: {i.get('stock')} (Threshold: {i.get('threshold')})\n"

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="Inventory Alert",
            Message=message
        )

    return {
        "statusCode": 200,
        "body": "Check completed"
    }
```

---

### 5. IAM Permissions

Attach:

* AmazonDynamoDBFullAccess
* AmazonSNSFullAccess

---

### 6. Schedule with EventBridge

* Rule Type: Schedule
* Example:

```
rate(5 minutes)
```

---

## ✅ Output

* Automatically detects low stock
* Sends email alerts
* Runs continuously without manual intervention

---

## 📸 Project Documentation

Detailed setup document included:



---

## 🎯 Use Cases

* E-commerce platforms (Amazon, BigBasket)
* Warehouse management systems
* Retail inventory automation

---

## 🔮 Future Enhancements

* Dashboard using React
* Auto restocking system
* SMS/WhatsApp alerts
* Integration with mobile apps

---

## 👨‍💻 Author

Rohith
AWS & DevOps Enthusiast

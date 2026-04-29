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

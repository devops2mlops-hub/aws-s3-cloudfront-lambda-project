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

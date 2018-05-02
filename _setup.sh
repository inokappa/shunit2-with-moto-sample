#!/usr/bin/env bash
moto_server s3 > /dev/null 2>&1 &
echo 'aaaaaaaaaaaaaaaa' > data1.txt
aws --endpoint=http://127.0.0.1:5000 s3api create-bucket --bucket=sample-bucket > /dev/null
aws --endpoint=http://127.0.0.1:5000 s3api put-object --bucket=sample-bucket --key=data1 --body=data1.txt > /dev/null
rm -f data1.txt

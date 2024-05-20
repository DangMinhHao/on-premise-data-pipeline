#!/usr/bin/env bash
echo "Set jobs for faker-generator"

cd ~/Documents/PersonalProject/on-premise-data-pipeline/  
source .venv/bin/activate

echo "Start to generate data"
python /Users/techx/Documents/PersonalProject/on-premise-data-pipeline/faker/UserGenerator.py >> /Users/techx/Documents/PersonalProject/on-premise-data-pipeline/monitoring/logs/user_logs.txt
python /Users/techx/Documents/PersonalProject/on-premise-data-pipeline/faker/ProductGenerator.py >> /Users/techx/Documents/PersonalProject/on-premise-data-pipeline/monitoring/logs/product_logs.txt
python /Users/techx/Documents/PersonalProject/on-premise-data-pipeline/faker/TransactionGenerator.py >> /Users/techx/Documents/PersonalProject/on-premise-data-pipeline/monitoring/logs/transaction_logs.txt
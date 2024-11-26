from elasticsearch import Elasticsearch
import json

# Connect to Elasticsearch
es = Elasticsearch("http://your-ec2-public-ip:9200")  # Replace with your EC2 IP and port

# Load test data from JSON file
with open('test_data.json', 'r') as file:
    test_data = json.load(file)

# Index each document
index_name = 'chat_messages'
for doc in test_data:
    es.index(index=index_name, id=doc['id'], document=doc)

print("Test data successfully indexed!")

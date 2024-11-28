from elasticsearch import Elasticsearch
import json

print("starting load_test_data.py !!!... ")
# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")  # Replace with your EC2 IP and port

print("Got es client")
# Load test data from JSON file
with open('test_data.json', 'r') as file:
    test_data = json.load(file)

print("________test_data ______\n", test_data)
# Index each document
index_name = 'chat_messages'
for doc in test_data:
    print("Indexing the data")
    es.index(index=index_name, id=doc['id'], document=doc)

print("Test data successfully indexed!")

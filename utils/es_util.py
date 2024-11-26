from elasticsearch import Elasticsearch
from config import ES_HOST

# Initialize Elasticsearch client
es = Elasticsearch(ES_HOST)

# Example function to index data
def index_data(index_name, doc_id, data):
    es.index(index=index_name, id=doc_id, document=data)

# Example function to search data
def search_data(index_name, query):
    return es.search(index=index_name, body=query)

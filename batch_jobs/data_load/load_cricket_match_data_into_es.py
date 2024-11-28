import os
import json
from elasticsearch import Elasticsearch, helpers

# Elasticsearch configuration
ES_HOST = "http://localhost:9200"  # Change to your ES endpoint if different
INDEX_NAME = "cricket_matches"  # Change to your preferred index name
DATA_FOLDER = "/Users/nitin.alex/Documents/chatckt_app/batch_jobs/test/data"  # Change to the folder containing your JSON files


def load_json_files(folder_path):
    """Load JSON data from files in the specified folder."""
    files_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                files_data.append(data)
    return files_data


def insert_data_to_es(es, data_list):
    """Insert data into Elasticsearch."""
    actions = []
    for match_data in data_list:
        source_data = dict()
        source_data["info"] = match_data["info"]
        source_data["innings"] = match_data["innings"]
        actions.append({
            "_index": INDEX_NAME,
            "_source": source_data
        })

    try:
        helpers.bulk(es, actions)
        print(f"Successfully inserted {len(actions)} documents into '{INDEX_NAME}' index.")
    except Exception as e:
        print(f"Error inserting data: {e}")


def main():
    # Initialize Elasticsearch client
    es = Elasticsearch(ES_HOST)

    # Load data from the folder
    match_data_list = load_json_files(DATA_FOLDER)

    # Insert data into Elasticsearch
    if match_data_list:
        insert_data_to_es(es, match_data_list)
    else:
        print("No JSON files found in the specified folder.")


if __name__ == "__main__":
    main()

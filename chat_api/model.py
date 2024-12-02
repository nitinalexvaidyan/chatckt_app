import sys
import os
import traceback
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import nls_to_dsl_util
from utils import es_util

def get_query_answer(query):
    try:
        try:
            print("first try")
            es_query = nls_to_dsl_util.get_dsl_query(query)
            if es_query.get("status", "").lower() != "success":
                print("Second try")
                es_query = nls_to_dsl_util.get_dsl_query(query)
        except Exception:
            print("Exception try")
            es_query = nls_to_dsl_util.get_dsl_query(query)


        print("\ndsl_query >>>>> \n", json.dumps(es_query))
        es_query = {"query": es_query["dsl_query"], "aggs": es_query.get("dsl_query", {}).get("bool", {}).get("aggs", {})}
        if "aggs" in es_query.get("query", {}).get("bool"):
            del es_query["query"]["bool"]["aggs"]
        print("\nes_query >>>>> \n", json.dumps(es_query))
        es_response = es_util.search_data("cricket_matches", es_query)
        print("\nes_response >>>>> \n", json.dumps(es_response))
        final_response = nls_to_dsl_util.get_final_response(es_response, query)
        print(f"\nfinal_response >>>>> \n: {final_response}")
        return final_response
    except Exception as e:
        traceback.print_exc()
        return "Sorry, I am unable to find the result for the question asked at the moment."

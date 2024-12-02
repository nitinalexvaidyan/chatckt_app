import sys
import os
import traceback
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import nls_to_dsl_util
from utils import es_util

def get_query_answer(query):
    try:
        es_query = nls_to_dsl_util.get_dsl_query(query)
        es_query = {"query": es_query["dsl_query"], "aggs": es_query.get("aggs", {})}
        if "aggs" in es_query["query"]:
            del es_query["query"]["aggs"]
        print("es_query >>>>> \n", es_query)
        es_response = es_util.search_data("cricket_matches", es_query)
        print("es_response >>>>> \n", es_response)
        final_response = nls_to_dsl_util.get_final_response(es_response, query)
        print(f"final_response >>>>> \n: {final_response}")
        return final_response
    except Exception as e:
        traceback.print_exc()
        return "Sorry, I am unable to find the result for the question asked."

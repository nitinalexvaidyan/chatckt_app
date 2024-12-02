from utils import nls_to_dsl_util
from utils import es_util

def get_query_answer(query):
    es_query = nls_to_dsl_util.get_dsl_query(query)
    es_response = es_util.search_data("cricket_matches", es_query)
    final_response = nls_to_dsl_util.get_final_response(es_response, query)
    print(f"final_response: {final_response}")
    return final_response

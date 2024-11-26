import model


def process_query(req_payload):
    try:
        # Basic validation
        if 'query' not in req_payload:
            return {"error": "query field is required"}, 400

        query = req_payload['query']
        answer = model.get_query_answer(query)
        return {"query": query, "response": answer}

    except Exception as e:
        return {"error": str(e)}, 500

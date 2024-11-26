import model


def process_query(req_payload):
    try:
        # Basic validation
        if 'query' not in req_payload:
            return {"success": False, "error": "query field is required"}, 400

        query = req_payload['query']
        answer = model.get_query_answer(query)
        return {"success": True, "query": query, "response": answer}, 200

    except Exception as e:
        return {"error": str(e)}, 500

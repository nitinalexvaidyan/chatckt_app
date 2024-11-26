import service
from flask import request, jsonify


def register_routes(app):

    @app.route('/', methods=['GET'])
    def home():
        return "Hello from Flask on AWS EC2!"

    @app.route('/nitin', methods=['GET'])
    def nitin():
        return "Hello from Nitin Alex Vaidyan"

    @app.route('/query', methods=['POST'])
    def query():
        req_payload = request.get_json()  # Extract JSON payload
        return service.process_query(req_payload)  # Call service layer

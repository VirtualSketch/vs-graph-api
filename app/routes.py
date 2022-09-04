from flask import make_response, jsonify, request, Response
from app import app
from app.controllers.expression_controller import expression_controller


from .controllers.graph_controller import graph_controller

@app.route('/', methods=['GET'])
def init():
    return 'Hello Python Graph API'

@app.route('/api/get_graph', methods=['POST'])
def get_graph():
    params = request.get_json()
    graph_base64_image = graph_controller(params)
    return make_response(jsonify({ 'graph_base64_image': graph_base64_image }), 200)

@app.route('/api/get_equation', methods=['POST'])
def get_equation():
    params = request.get_json()
    equation = expression_controller(params)
    return make_response(jsonify({ 'equation': equation }), 200)

@app.errorhandler(500)
def handle_500_error(e):
    return Response(str(e), status=500)
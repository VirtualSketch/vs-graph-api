from flask import make_response, jsonify, request, Response
from app import app
import uuid

from .controllers.graph_controller import graph_controller

@app.route('/', methods=['GET'])
def init():
    return 'Hello Python Graph API'

@app.route('/create_session', methods=['GET'])
def index():
    return make_response(jsonify({ 'session_id': uuid.uuid4().__str__() }), 200)

@app.route('/api/get_graph', methods=['POST'])
def get_graph():
    params = request.get_json()
    graph_path = graph_controller(params)
    print(graph_path)
    return make_response(jsonify({ 'graph_image_url': graph_path }), 200)

@app.route('/api/get_resolved-account/', methods=['POST'])
def get_resolved_account():
    return 'Retorna a conta'

@app.route('/finish_session', methods=['POST'])
def finish_session():
    return 'Fim da sessão'

@app.errorhandler(500)
def handle_400_error(e):
    return Response(str(e), status=500)
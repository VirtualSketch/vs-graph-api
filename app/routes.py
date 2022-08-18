from flask import make_response, jsonify, request, Response
from app import app
import uuid

from app.controllers.kill_session_controller import kill_session_controller

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
    return make_response(jsonify({ 'graph_image_url': graph_path }), 200)

@app.route('/api/get_resolved-account/', methods=['POST'])
def get_resolved_account():
    return 'Retorna a conta'

@app.route('/kill_session/<session_id>', methods=['GET'])
def kill_session(session_id):
    kill_session_controller(session_id)
    return Response('Directory deleted successfully', status=200)
@app.errorhandler(500)
def handle_500_error(e):
    return Response(str(e), status=500)
from flask import make_response, jsonify, request, abort, Response
from app import app
import uuid

from .controllers.graph_controller import graph_controller

@app.route('/', methods=['GET'])
def init():
    return 'Hello Python Graph API'

@app.route('/create_session', methods=['GET'])
def index():
    headers = {"Content-Type": "application/json"}
    return make_response(jsonify({ 'session_id': uuid.uuid4().__str__() }), 200, headers=headers)

@app.route('/api/get_graph', methods=['POST'])
def get_graph():
    params = request.get_json()
    graph_controller(params)
    return 'Retorna o grafico'

@app.route('/api/get_resolved-account/', methods=['POST'])
def get_resolved_account():
    return 'Retorna a conta'

@app.route('/finish_session', methods=['POST'])
def finish_session():
    return 'Fim da sessão'

@app.errorhandler(400)
def handle_400_error(e):
    return Response('Erro teste', status=400)
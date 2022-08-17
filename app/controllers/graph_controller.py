from flask import make_response, jsonify, abort
from ..models.graph import Graph

def graph_controller(params):
    raw_account = params.get('raw_account')
    session_id = params.get('session_id')

    graph = Graph(raw_account=raw_account, session_id=session_id)

    try:
        validate = graph.validate_params(params)
        print(validate)

        if not validate:
            raise Exception('Custom Error')
    except:
        abort(400, 'Internal server error')   
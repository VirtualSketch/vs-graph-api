from flask import abort
from app.errors.validate_json_error import ValidateJsonError
from ..models.graph import Graph

def graph_controller(params):
    raw_account = params.get('raw_account')
    session_id = params.get('session_id')

    graph = Graph(raw_account=raw_account, session_id=session_id)

    try:
        graph.validate_params(params)
        return graph.get_graph()
    except ValidateJsonError:
        abort(500, 'JSON Schema is not valid')
    except:
        abort(500, 'Unknown error')
from flask import abort
from app.errors.validate_json_error import ValidateJsonError
from ..models.graph import Graph

def graph_controller(params):
    raw_expression = params.get('raw_expression')
    session_id = params.get('session_id')
    graph_color = params.get('graph_color')

    graph = Graph(raw_expression=raw_expression, session_id=session_id, graph_color=graph_color)

    try:
        graph.validate_params(params)
        return graph.get_graph()
    except ValidateJsonError:
        abort(500, 'JSON Schema is not valid')
    except:
        abort(500, 'Unknown error')
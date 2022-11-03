from flask import abort
from app.errors.validate_json_error import ValidateJsonError
from ..models.graph import Graph
import re

def graph_controller(params):
    raw_expression = params.get('raw_expression')
    graph_color = params.get('graph_color')

    has_letter_after_digit = re.search(r"(\d)([a-z])", raw_expression)

    if has_letter_after_digit is not None:
        raw_expression = re.sub(r"\d[a-z]", has_letter_after_digit.group(1) + " * " + has_letter_after_digit.group(2), raw_expression)

    has_square = re.search(r"([a-z])(\d)", raw_expression)

    if has_square is not None:
        raw_expression = re.sub(r"[a-z]\d", has_square.group(1) + " ** " + has_square.group(2), raw_expression)

    graph = Graph(raw_expression=raw_expression, graph_color=graph_color)

    try:
        graph.validate_params(params)
        return graph.get_graph()
    except ValidateJsonError:
        abort(500, 'JSON Schema is not valid')
    except:
        abort(500, 'Unknown error')
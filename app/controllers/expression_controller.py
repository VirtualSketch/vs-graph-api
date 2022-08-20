from flask import abort

from app.errors.validate_json_error import ValidateJsonError
from app.models.expression import Expression

def expression_controller(params):
    raw_expression = params.get('raw_expression')
    expression = Expression(raw_expression=raw_expression)

    try:
        expression.validate_params(params)
        equation = expression.get_equation()
        return equation
    except ValidateJsonError:
        abort(500, 'JSON Schema is not valid')
    except:
        abort(500, 'Unknown error')

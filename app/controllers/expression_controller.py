from flask import abort

from app.errors.validate_json_error import ValidateJsonError
from app.models.expression import Expression

import re

def expression_controller(params):
    raw_expression = params.get('raw_expression')

    has_letter_after_digit = re.search(r"(\d)([a-z])", raw_expression)

    if has_letter_after_digit is not None:
        raw_expression = re.sub(r"\d[a-z]", has_letter_after_digit.group(1) + " * " + has_letter_after_digit.group(2), raw_expression)

    has_square = re.search(r"([a-z])(\d)", raw_expression)

    if has_square is not None:
        raw_expression = re.sub(r"[a-z]\d", has_square.group(1) + " ** " + has_square.group(2), raw_expression)

    expression = Expression(raw_expression=raw_expression)

    try:
        expression.validate_params(params)
        equation = expression.get_equation()
        return equation
    except ValidateJsonError:
        abort(500, 'JSON Schema is not valid')
    except:
        abort(500, 'Unknown error')

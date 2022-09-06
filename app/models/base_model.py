from app.errors.validate_json_error import ValidateJsonError
from ..utils.validate_json import validate_json

class BaseModel:
    def __init__(self, raw_expression):
        self.raw_expression = raw_expression

    def validate_params(self, json_data, json_schema):
        validate = validate_json(json_data=json_data, json_schema=json_schema)

        if not validate:
            raise ValidateJsonError

        return validate


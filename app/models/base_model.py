from ..utils.validate_json import validate_json

class BaseModel:
    def __init__(self, session_id, raw_account):
        self.session_id = session_id
        self.raw_account = raw_account

    def validate_params(self, json_data, json_schema):
        validate = validate_json(json_data=json_data, json_schema=json_schema)
        return validate
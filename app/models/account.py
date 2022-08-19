from .base_model import BaseModel

class Account(BaseModel):
    def __init__(self, raw_account) -> None:
        session_id = ''
        super().__init__(session_id, raw_account)
    
    _graph_params_schema = {
        "type": "object",
        "properties": {
            "raw_account": {"type": "string"},
            },
        "required": ["raw_account"]
    }

    def get_resolved_account(self):
        return str('x + y')

    def validate_params(self, json_data):
        return super().validate_params(json_data, self._graph_params_schema)

from .base_model import BaseModel


class Graph(BaseModel):
    def __init__(self, session_id, raw_account) -> None:
        super().__init__(session_id, raw_account)
    
    _graph_params_schema = {
        "type": "object",
        "properties": {
            "session_id": {"type": "string"},
            "raw_account": {"type": "string"},
            },
        "required": ["session_id", "raw_account"]
    }

    def validate_params(self, json_data):
        return super().validate_params(json_data, self._graph_params_schema)
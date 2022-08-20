from app.scripts.create_equation_steps import equation_steps
from .base_model import BaseModel

class Expression(BaseModel):
    def __init__(self, raw_expression) -> None:
        session_id = ''
        super().__init__(session_id, raw_expression)
    
    _graph_params_schema = {
        "type": "object",
        "properties": {
            "raw_expression": {"type": "string"},
            },
        "required": ["raw_expression"]
    }

    def get_equation(self):
        return equation_steps(self.raw_expression)

    def validate_params(self, json_data):
        return super().validate_params(json_data, self._graph_params_schema)
from app.scripts.create_cartesian_graph import simple_degree_graph
from .base_model import BaseModel

class Graph(BaseModel):
    def __init__(self, raw_expression, graph_color) -> None:
        self.graph_color = graph_color
        super().__init__(raw_expression)

    _graph_params_schema = {
        "type": "object",
        "properties": {
            "raw_expression": {"type": "string"},
            "graph_color": {"type": "string"},
            },
        "required": ["raw_expression", "graph_color"]
    }

    def get_graph(self):
        graph_base64 = simple_degree_graph(equation=self.raw_expression, color=self.graph_color)
        
        return graph_base64

    def validate_params(self, json_data):
        return super().validate_params(json_data, self._graph_params_schema)

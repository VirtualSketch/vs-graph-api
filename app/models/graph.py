import os
from pathlib import Path
from app.utils.get_image_url import get_image_url
from app.utils.get_random_string import get_random_string

from app.scripts.create_cartesian_graph import simple_degree_graph
from app.utils.get_static_path import get_static_path
from .base_model import BaseModel

class Graph(BaseModel):
    def __init__(self, session_id, raw_expression, graph_color) -> None:
        self.graph_color = graph_color
        super().__init__(session_id, raw_expression)


    image_path = ''
    _graph_params_schema = {
        "type": "object",
        "properties": {
            "session_id": {"type": "string"},
            "raw_expression": {"type": "string"},
            "graph_color": {"type": "string"},
            },
        "required": ["session_id", "raw_expression", "graph_color"]
    }

    def get_graph(self):
        static_path = get_static_path()
        is_exists_static_dir = os.path.exists(static_path)
        is_exists_graph_dir = os.path.exists(Path(static_path, self.session_id))
        
        if not is_exists_static_dir:
            os.mkdir(static_path)

        if not is_exists_graph_dir:
            self.image_path = os.path.join(static_path, self.session_id)
            os.mkdir(self.image_path)
        else:
            self.image_path = os.path.join(static_path, self.session_id)

        graph_name = get_random_string(8)
        image_url = f'{get_image_url(session_id=self.session_id, file_name=graph_name)}.png'

        simple_degree_graph(fileName=graph_name, equation=self.raw_expression, path=self.image_path, color=self.graph_color)

        return image_url

    def validate_params(self, json_data):
        return super().validate_params(json_data, self._graph_params_schema)

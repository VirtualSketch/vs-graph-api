import os
from app.utils.get_image_url import get_image_url
from app.utils.get_random_string import get_random_string

from app.utils.get_static_path import get_static_path
from pathlib import Path
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

    def get_graph(self):
        static_path = get_static_path()
        is_exists_static_dir = os.path.exists(static_path)
        is_exists_graph_dir = os.path.exists(Path(static_path, self.session_id))
        
        if not is_exists_static_dir:
            os.mkdir(static_path)

        if not is_exists_graph_dir:
            image_path = os.path.join(static_path, self.session_id)
            os.mkdir(image_path)

        graph_name = get_random_string(8)
        image_url = get_image_url(session_id=self.session_id, file_name=graph_name)

        print('call generate graph function')
        return image_url

    def validate_params(self, json_data):
        return super().validate_params(json_data, self._graph_params_schema)

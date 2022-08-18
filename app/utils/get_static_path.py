from pathlib import Path
import os

def get_static_path():
    root_dir = Path(os.path.dirname(__file__))
    static_dir = Path(root_dir.parent.parent, 'static')
    return static_dir
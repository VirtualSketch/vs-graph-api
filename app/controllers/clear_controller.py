from flask import abort
import shutil

from app.utils.get_static_path import get_static_path

def clear_controller():
    try:
        static_dir = get_static_path()
        shutil.rmtree(static_dir)
    except:
        abort(500, 'Fail to cleaning static directory')

from flask import abort
from pathlib import Path
import shutil

from app.utils.get_static_path import get_static_path

def kill_session_controller(session_id):
    try:
        static_dir = get_static_path()
        session_dir = Path(static_dir, session_id)
        shutil.rmtree(session_dir)
    except:
        abort(500, 'Fail to delete session directory')

from flask import request

def get_image_url(session_id, file_name):
    domain = request.url_root
    image_url = f'{domain}static/{session_id}/{file_name}'

    return image_url
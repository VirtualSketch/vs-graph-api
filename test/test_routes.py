from ast import Assert
import pytest
import json
import requests

from app.routes import get_equation

@pytest.mark.parametrize("equation", [({"raw_expression": "- 2 * x + 3"})])

def test_post_equation(equation):
    url = "https://virtualsketch.herokuapp.com/api/get_equation"
    response = requests.post(url, json=equation)
    validResponse = json.loads(response.content)
    if(isinstance(validResponse, object)):
        result = validResponse.get('equation')
        print(result)
        assert type(result) == list
    else:
        assert False

# @pytest.mark.parametrize("graph", [({"raw_expression": "x ** 2 - 4 * x - 12", "graph_color": "#fff"})])

# def test_post_graph(graph):
#     url = "https://virtualsketch.herokuapp.com/api/get_graph"
#     response = requests.post(url, json=graph)
#     validResponse = json.loads(response.content)
#     print(response)
    


import base64
from sre_compile import isstring
import pytest
import json
import requests

#Defining parameters of the test
@pytest.mark.parametrize("equation", 
[
    ({"raw_expression": "- 2 * x + 3"}), 
    ({"raw_expression": "- x ** 2 + 5 * x + 6",}), 
    ({"raw_expression": "- 4 * x + 2",})
])

#Test definition
def test_post_equation(equation):
    #Doing a post request to the API
    url = "https://virtualsketch.herokuapp.com/api/get_equation"
    response = requests.post(url, json=equation)
    validResponse = json.loads(response.content)
    #If the return from the API is a object and a list, pass the test
    if(isinstance(validResponse, object)):
        result = validResponse.get('equation')
        assert type(result) == list
    else:
        assert False

#Defining parameters of the test
@pytest.mark.parametrize("graph", 
[
    ({"raw_expression": "x ** 2 - 4 * x - 12", "graph_color": "#fff"}), 
    ({"raw_expression": "2 * x + 2", "graph_color": "#000"}),
    ({"raw_expression": "2 * x + 4", "graph_color": "#fff"})
])

#Test definition
def test_post_graph(graph):
    #Doing a post request to the API
    url = "https://virtualsketch.herokuapp.com/api/get_graph"
    response = requests.post(url, json=graph)
    validResponse = json.loads(response.content)
    content = validResponse.get('graph_base64_image')
    
    #If the return of the API is a string and a base64, the test will pass
    if(isstring(content)):
        print("It is a base64")
        assert base64.b64decode(content)
    else:
        print("Not a string and is not a base64.")
        assert False

#Defining parameters of the test
@pytest.mark.parametrize("errors", 
[
    ({"raw_expression": "x ** 2 - 4 * x - 12", "graph": "#fff"}), 
    ({"expression": "x ** 2 - 4 * x - 12", "graph_color": "#fff"}),
    ({"raw": "x ** 2 - 4 * x - 12", "color": "#fff"}),
    ({"raw_expression": "x ** 2 - 4 * x - 12", "graph_color": "%*"}),
    ({"raw_expression": "k ** 2 - 4 * t - 12", "graph_color": "#fff"}),
    ({"raw_expression": "k ** 2 - 4 * t - 12", "graph_color": "#/*"})
])

#Test definition
def test_post_graph_error(errors):
    #Doing a post request to the API
    url = "https://virtualsketch.herokuapp.com/api/get_graph"
    result = requests.post(url, json=errors)
    #If the return from the API is error mesage that we programed, pass the test
    if(result.content == b'500 Internal Server Error: JSON Schema is not valid' or result.content == b'500 Internal Server Error: Unknown error'):
        assert True
    else:
        print("Is not a valid error.")
        assert False

#Defining parameters of the test
@pytest.mark.parametrize("errors_equation", 
[
    ({"raw": "- 2 * x + 3"}), 
    ({"expression": "- 2 * x + 3"}), 
    ({"raw_expression": "- 2d - r"}), 
    ({"raw_expression": ""}) 
])

#Test definition
def test_post_expression_error(errors_equation):
    #Doing a post request to the API
    url = "https://virtualsketch.herokuapp.com/api/get_equation"
    result = requests.post(url, json=errors_equation)
    #If the return from the API is error mesage that we programed, pass the test
    if(result.content == b'500 Internal Server Error: JSON Schema is not valid' or result.content == b'500 Internal Server Error: Unknown error'):
        assert True
    else:
        print("Is not a valid error.")
        assert False
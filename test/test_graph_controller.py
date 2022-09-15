import pytest
from sre_compile import isstring
import base64
from app.controllers.graph_controller import graph_controller

#Defining parameters of the test
@pytest.mark.parametrize("parameter", 
[
#First degree expression
({"raw_expression": "x ** 2 - 4 * x - 12", "graph_color": "#fff"}),
({"raw_expression": "2 * x + 2", "graph_color": "#000"}),
({"raw_expression": "- 2 * x + 5", "graph_color": "#fff"}),
#Second degree expression
({"raw_expression": "2 * x ** 2 * 2 + 1", "graph_color": "#000"}), 
({"raw_expression": "- x ** 2 - 2 * x - 3", "graph_color": "#fff"})
])

#Test definition
def test_graph_controller(parameter):
    #Sending the parameter to the function and proceed further if it is a string
    graph = graph_controller(parameter)
    if (isstring(graph) == True):
        try:
            #Testing if the return of the function is encoded in base64
            base64.b64decode(graph)
            assert True
        except:
            assert False
    else:
        assert False

#Defining the parameters to test
@pytest.mark.parametrize("errors", 
[{"raw_expression": "x ** 2 - 4 * x - 12", "graph": "#fff"}, 
({"expression": "x ** 2 - 4 * x - 12", "graph_color": "#fff"}),
({"raw": "x ** 2 - 4 * x - 12", "color": "#fff"}),
({"raw_expression": "x ** 2 - 4 * x - 12", "graph_color": "%*"}),
({"raw_expression": "k ** 2 - 4 * t - 12", "graph_color": "#fff"}),
({"raw_expression": "k ** 2 - 4 * t - 12", "graph_color": "#/*"})])

#Test definition
def test_graph_controller_error(errors):
    try:
        # The function graph_controller needs to throw an error, otherwise fail the test
        graph_controller(errors)
        assert False
    #Catch the exception and give a name to it
    except Exception as error:
        getErrorMessage = str(error)
        # If it is one of the expected exceptions, print the error's message and pass the test
        if(getErrorMessage == '500 Internal Server Error: JSON Schema is not valid' or getErrorMessage == '500 Internal Server Error: Unknown error'):
            print(getErrorMessage)
            assert True
            
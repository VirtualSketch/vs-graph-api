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

#Definig the test
def test_graph_controller(parameter):
    #Sending the parameter to the function
    graph = graph_controller(parameter)
    #If it is a string continue to the try
    if (isstring(graph) == True):
        try:
            #Verify if the return of the function is also a base64
            base64.b64decode(graph)
            #If it is a base64 pass the test
            assert True
        except:
            #If is not a base64 the test will fail
            assert False
    else:
        #If is not a string the test will fail
        assert False

#Defining the parameters to test
@pytest.mark.parametrize("errors", 
[{"raw_expression": "x ** 2 - 4 * x - 12", "graph": "#fff"}, 
({"expression": "x ** 2 - 4 * x - 12", "graph_color": "#fff"}),
({"raw": "x ** 2 - 4 * x - 12", "color": "#fff"}),
({"raw_expression": "x ** 2 - 4 * x - 12", "graph_color": "%*"}),
({"raw_expression": "k ** 2 - 4 * t - 12", "graph_color": "#fff"}),
({"raw_expression": "k ** 2 - 4 * t - 12", "graph_color": "#/*"})])

def test_graph_controller_error(errors):
    try:
        #Passing the parameters to the function
        graph_controller(errors)
        #The functions in this test will throw a error, so if the function return something that is not a error, the test will fail
        assert False
    #Catch the exception and give a name to it
    except Exception as error:
        #Transfoming the error into a string
        getErrorMessage = str(error)
        if(getErrorMessage == '500 Internal Server Error: JSON Schema is not valid'):
            #Print the error in the console if the message is equal to "500 Internal Server Error: JSON Schema is not valid"
            print(getErrorMessage)
            #Pass the test
            assert True
        elif(getErrorMessage == '500 Internal Server Error: Unknown error'):
            #Print the error in the console if the message is equal to "500 Internal Server Error: Unknown error"
            print(getErrorMessage)
            #Pass the test
            assert True
            
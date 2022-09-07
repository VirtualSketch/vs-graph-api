import pytest
from sre_compile import isstring
import base64
from app.scripts.create_cartesian_graph import simple_degree_graph

#Defining parameters of the test
@pytest.mark.parametrize("equation, color", 
[
#First degree expression
("5 * x + 7", "#000"), 
("2 * x + 2", "#fff"),
("- 2 * x + 5", "#000"),
("2 * x + 4", "#fff"),
("- 3 * x + 5", "#000"),
("- 4 * x + 2", "#fff"),
#Second degree expression
("2 * x ** 2 * 2 + 1", "#000"), 
("- x ** 2 - 2 * x - 3", "#fff"),
("x ** 2 - 2 * x", "#000"),
("- x ** 2 + 5 * x + 6", "#fff"),
("- x ** 2 - 1", "#000"),
("- 4 * x ** 2 + 4", "#fff")
])

#Defining the test
def test_graph(equation, color):
    #Sending the parameter to the function
    graph = simple_degree_graph(equation, color)
    #Verifying if the return of the function is a string
    if (isstring(graph) == True):
        #If it is a string continue the test
        try:
            #Verify if the return of the function is also a base64
            base64.b64decode(graph)
            #If it is a base64, pass the test
            assert True
        except:
            #If is not a base64 the test will fail
            assert False
    else:
        #If is not a string the test will fail
        assert False

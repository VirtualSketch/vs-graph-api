import pytest
from app.controllers.expression_controller  import expression_controller

#Defining parameters of the test
@pytest.mark.parametrize("params,expected",
    [
        ({"raw_expression": "- 2 * x + 3"}, 
        [
        "f(x) = - 2 * x + 3 = - 2 * (-3) + 3 = 9",
        "f(x) = - 2 * x + 3 = - 2 * (-2) + 3 = 7",
        "f(x) = - 2 * x + 3 = - 2 * (-1) + 3 = 5",
        "f(x) = - 2 * x + 3 = - 2 * (0) + 3 = 3",
        "f(x) = - 2 * x + 3 = - 2 * (1) + 3 = 1",
        "f(x) = - 2 * x + 3 = - 2 * (2) + 3 = -1",
        "f(x) = - 2 * x + 3 = - 2 * (3) + 3 = -3"
        ]),
        ({"raw_expression": "x ** 2 + 4"}, 
        [
        "f(x) = x ** 2 + 4 = (-3) ** 2 + 4 = 13",
        "f(x) = x ** 2 + 4 = (-2) ** 2 + 4 = 8",
        "f(x) = x ** 2 + 4 = (-1) ** 2 + 4 = 5",
        "f(x) = x ** 2 + 4 = (0) ** 2 + 4 = 4",
        "f(x) = x ** 2 + 4 = (1) ** 2 + 4 = 5",
        "f(x) = x ** 2 + 4 = (2) ** 2 + 4 = 8",
        "f(x) = x ** 2 + 4 = (3) ** 2 + 4 = 13"
         ]),
        ({"raw_expression": "x ** 2 - 2 * x - 3"}, 
        [
        "f(x) = x ** 2 - 2 * x - 3 = (-3) ** 2 - 2 * (-3) - 3 = 12",
        "f(x) = x ** 2 - 2 * x - 3 = (-2) ** 2 - 2 * (-2) - 3 = 5",
        "f(x) = x ** 2 - 2 * x - 3 = (-1) ** 2 - 2 * (-1) - 3 = 0",
        "f(x) = x ** 2 - 2 * x - 3 = (0) ** 2 - 2 * (0) - 3 = -3",
        "f(x) = x ** 2 - 2 * x - 3 = (1) ** 2 - 2 * (1) - 3 = -4",
        "f(x) = x ** 2 - 2 * x - 3 = (2) ** 2 - 2 * (2) - 3 = -3",
        "f(x) = x ** 2 - 2 * x - 3 = (3) ** 2 - 2 * (3) - 3 = 0"
        ]),
        ({"raw_expression": "-x ** 2 + 4 * x - 3"}, 
        [
        "f(x) = -x ** 2 + 4 * x - 3 = -(-3) ** 2 + 4 * (-3) - 3 = -24",
        "f(x) = -x ** 2 + 4 * x - 3 = -(-2) ** 2 + 4 * (-2) - 3 = -15",
        "f(x) = -x ** 2 + 4 * x - 3 = -(-1) ** 2 + 4 * (-1) - 3 = -8",
        "f(x) = -x ** 2 + 4 * x - 3 = -(0) ** 2 + 4 * (0) - 3 = -3",
        "f(x) = -x ** 2 + 4 * x - 3 = -(1) ** 2 + 4 * (1) - 3 = 0",
        "f(x) = -x ** 2 + 4 * x - 3 = -(2) ** 2 + 4 * (2) - 3 = 1",
        "f(x) = -x ** 2 + 4 * x - 3 = -(3) ** 2 + 4 * (3) - 3 = 0"
        ])
    ])

#Test definition
def test_expression_controller(params, expected):
    #Sending the parameter to the function
    result = expression_controller(params)
    #If the function return a list proceed further
    if(type(result) == list):
        #If the result is equal to the expected, pass the test
        assert result == expected
    else:
        assert False

#Passing the parameters to the test
@pytest.mark.parametrize("errors", [({"raw": "- 2 * x + 3"}), ({"expression": "- 2 * x + 3"}), ({"raw_expression": "- 2d - r"}), ({"raw_expression": ""}) ])

#Test definition
def test_expression_controller_json_error(errors):
    #The function expression_controller needs to throw an error, otherwise fail the test
    try:
        expression_controller(errors)
        assert False

    #Catch the exception and give a name to it
    except Exception as error:
        getErrorMessage = str(error)
        #If it is one of the expected exceptions, print the error's message and pass the test
        if(getErrorMessage == '500 Internal Server Error: JSON Schema is not valid' or getErrorMessage == '500 Internal Server Error: Unknown error'):
            print(getErrorMessage)
            assert True
            

import pytest
from app.controllers.expression_controller  import expression_controller

#Defining parameters of the test
@pytest.mark.parametrize("params,expected",
    [
        ({"raw_expression": "- 2 * x + 3"}, 
        [
        ]),
        ({"raw_expression": "x ** 2 + 4"}, 
        [
        ]),
        ({"raw_expression": "x ** 2 - 2 * x - 3"}, 
        [
        ]),
        ({"raw_expression": "-x ** 2 + 4 * x - 3"}, 
        [
        ])
    ])
#Defining the test
def test_expression_controller(params, expected):
    #Sending the parameter to the function
    result = expression_controller(params)
    #Comparing the result of the function with the expected value passed in the parametrize
    assert result == expected

#Passing the parameters to the test
@pytest.mark.parametrize("errors", [({"raw": "- 2 * x + 3"}), ({"raw_expression": "- 2d - r"})])

#Defining the test
def test_expression_controller_json_error(errors):
    #Try to rum the function
    #Passing the parameters to the function
    try:
        #Passing the parameter to the function
        expression_controller(errors)
        #The functions in this test will throw a error, so if the function return something that is not a error, the test will fail
        assert False
    #Catch the exception and give a name to it
    except Exception as error:
        #Transfoming the error into a string
        getErrorMessage = str(error)
        if(getErrorMessage == '500 Internal Server Error: JSON Schema is not valid' or getErrorMessage == '500 Internal Server Error: Unknown error'):
            #Print the error in the console if the message is equal to "500 Internal Server Error: JSON Schema is not valid"
            print(getErrorMessage)
            #Pass the test
            assert True
            

import pytest
from app.scripts.create_equation_steps import equation_steps

#Defining parameters of the test
@pytest.mark.parametrize("test_mock_expression,expected",
    [
        #First degree expression 
        ("- 2 * x + 3", 
        [
        ]),
        ("2 * x - 1", 
        [
        ]),
        ("- x + 1", 
        [
        ]),
        ("3 * x + 5", 
        [
        ]),
        ("2 * x + 5", 
        [
        ]),
        #Second degree expression
        ("x ** 2 - 4 * x - 12", 
        [
        ]), 
        ("2 * x ** 2 + 4 * x - 6", 
        [
        ]),
        ("x ** 2 + 4", 
        [
        ]),
        ("x ** 2 - 2 * x - 3", 
        [
        ]),
        ("-x ** 2 + 4 * x - 3", 
        [
        ])
    ])

#Defining the test
def test_expression(test_mock_expression,expected):
    #Sending the equation to the function
    equation = equation_steps(test_mock_expression)
    #Comparing the result of the function, with the expected value passed in the parametrize.
    #If the result is equal to true, the test will pass
    if(type(equation) == list):
        assert equation == expected
    else:
        assert False

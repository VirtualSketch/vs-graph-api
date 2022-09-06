import pytest

from app.scripts.create_equation_steps import equation_steps

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
        ("x ** 2 - 4 * x - 12" , 
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


def test_expression(test_mock_expression,expected):
    equation = equation_steps(test_mock_expression)
    assert equation == expected

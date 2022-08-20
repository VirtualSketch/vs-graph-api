import re

# Return the solving steps for the equation
def equation_steps(equation):
    steps = []
    # Iterates based on the range of x axis
    for xaxis in range(-3, 3+1):
        # Replace the x variable with the iteration value
        literal = re.sub('[a-z]', str(xaxis), equation.strip())
        # Return the equation result
        result = eval(literal)
        expression = f'f(x) = {equation} = {literal} = {result}'
        steps.append(expression)

    return steps
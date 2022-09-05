import base64
import matplotlib.pyplot as pyplot
import numpy as np
import io

# Defining the function that will generate the graph
def simple_degree_graph(fileName, path, equation, color): # The parameters to define the graph's file name, its path, the equation and its color    
    # Calculating the x and y to generate the graph
    x = np.linspace(-16, 16, 1000)
    y = eval(equation)
    
    # The variable that will be used to hold the figure/graph
    elements = pyplot.figure(figsize=(8, 6))
    
    # Adding axes to the graph
    axes = elements.add_subplot()
    
    # Defining the positions of the x axis and y axis
    axes.spines['left'].set_position('center')
    axes.spines['bottom'].set_position('center')
    
    # Defining the color of the right axis and top axis
    axes.spines['right'].set_color('none')
    axes.spines['top'].set_color('none')
    
    # Defining the color of the x axis and y axis based in the parameter color
    axes.spines['left'].set_color(color)
    axes.spines['bottom'].set_color(color)
    
    # Changing the size of the line that was calculated to be inserted into the graph
    pyplot.rcParams['axes.linewidth'] = 1.5 
    
    # Defining the color of the numbers that are in the x axis and y axis
    axes.tick_params(axis = 'x', colors = color)
    axes.tick_params(axis = 'y', colors = color)
    
    # Defining the limit of numbers that will be shown in the graph
    pyplot.xlim(-8,8)
    pyplot.ylim(-20,20)        
    
    # Generating the graph
    pyplot.plot(x,y, color='#8075FF', linewidth=2.5)
    
    # Returns the graph in base64 

    graph_stringIObytes = io.BytesIO()
    
    pyplot.savefig(graph_stringIObytes, format='png', transparent=True)
    graph_stringIObytes.seek(0)
    
    graph_base64_data = base64.b64encode(graph_stringIObytes.read()).decode('utf-8')
    
    return graph_base64_data


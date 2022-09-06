from sre_compile import isstring
import pytest
import base64

from app.scripts.create_cartesian_graph import simple_degree_graph

@pytest.mark.parametrize("fileName, path, equation, color", 
[
#First degree expression
("test", "./test", "5 * x + 7", "#000"), 
("test2", "./test", "2 * x + 2", "#fff"),
("test3", "./test", "- 2 * x + 5", "#000"),
("test4", "./test", "2 * x + 4", "#fff"),
("test5", "./test", "- 3 * x + 5", "#000"),
("test6", "./test", "- 4 * x + 2", "#fff"),
#Second degree expression
("test7", "./test", "2 * x ** 2 * 2 + 1", "#000"), 
("test8", "./test", "- x ** 2 - 2 * x - 3", "#fff"),
("test9", "./test", "x ** 2 - 2 * x", "#000"),
("test10", "./test", "- x ** 2 + 5 * x + 6", "#fff"),
("test11", "./test", "- x ** 2 - 1", "#000"),
("test12", "./test", "- 4 * x ** 2 + 4", "#fff")
])

def test_graph(fileName, path, equation, color):
    graph = simple_degree_graph(fileName, path, equation, color)
    if (isstring(graph) == True):
        try:
            base64.b64decode(graph)
            assert True
        except:
            assert False

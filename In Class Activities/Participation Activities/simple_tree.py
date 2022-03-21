# import Graph class
from graphviz import Graph
from graphviz import Digraph

def main():

    # create simple graph
    h = Graph("simple_tree")

    # define nodes and edges
    h.node("a")
    h.node("b")
    h.node("c")
    h.edge("a", "b")
    h.edge("a", "c")

    # render the graph
    h.render(view=True)
    h.render(filename = "simple_tree")

if __name__ == "__main__":
    main()

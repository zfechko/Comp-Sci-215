from graph import Graph
import networkx as nx
import matplotlib.pyplot as plt
import graphviz as gv

class Game:
    """
    Wrapper game class that contains all the methods needed to run the kevin bacon game
    """
    def __init__(self):
        self.g = Graph()
        self.g.build_graph()
        self.g.bfs(self.g.find_actor_id("Kevin Bacon"))
        
    def print_rules(self):
        """
        Prints the rules of the game and prompts the user to hit enter to start
        """
        print("Welcome to the Kevin Bacon game! Where you get to see the chain that connects one actor to Kevin Bacon!")
        input("Press enter to start!")

    def print_results(self, actor: str):
        """
        Given an actor name, this function prints the path back to Kevin Bacon
        """
        start_vertex = self.g.get_vertex(self.g.find_actor_id("Kevin Bacon")) #gets the kevin bacon vertex
        id = self.g.find_actor_id(actor.title())
        end = end_vertex = self.g.get_vertex(id)
        kb_number = 0
        while end_vertex is not None and end_vertex is not start_vertex:
            print(end_vertex.name, "is in", end_vertex.get_movie(end_vertex.predecessor), "with", end_vertex.predecessor.name)
            end_vertex = end_vertex.predecessor
            kb_number += 1
        print(end.name, "'s kevin bacon number is", kb_number)

    def search(self):
        """
        Prompts the user for an actor name to search, or to type "return" as the quit case
        if a valid
        """
        actor = str(input("Enter the name of an actor, or type 'return' to quit: "))
        if actor.title() in self.g.actors.values() or actor.lower() == "return":
            return actor
        else:
            print("Actor not valid")
            return

    def graph_results(self, actor: str):
        """
        Given an actor's name, this function constructs a networkx graph and then uses plt.show() to display it, either in a figure window or in a jupyter notebook
        """
        plt.tight_layout()
        plt.axis("off")
        start_vertex = self.g.get_vertex(self.g.find_actor_id("Kevin Bacon"))
        end_vertex = self.g.get_vertex(self.g.find_actor_id(actor.title()))
        G = nx.Graph()
        while end_vertex is not None and end_vertex is not start_vertex:
            G.add_node(end_vertex.name)
            if end_vertex.predecessor:
                G.add_edge(end_vertex.name, end_vertex.predecessor.name, label=end_vertex.get_movie(end_vertex.predecessor))
            end_vertex = end_vertex.predecessor
        pos = nx.circular_layout(G)
        labels = {node:str(node) for i, node in enumerate(G.nodes())}
        elabels = {edge:G[edge[0]][edge[1]]["label"] for i, edge in enumerate(G.edges())}
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos, labels)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=elabels)
        axis = plt.gca()
        axis.set_xlim([1.2*x for x in axis.get_xlim()])
        axis.set_ylim([1.2*y for y in axis.get_ylim()])
        plt.tight_layout()
        plt.show()
        



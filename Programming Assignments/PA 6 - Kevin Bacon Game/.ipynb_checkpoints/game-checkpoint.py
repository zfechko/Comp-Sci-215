from graph import Graph
import networkx as nx
import matplotlib.pyplot as plt

class Game:
    def __init__(self):
        self.g = Graph()
        self.g.build_graph()
        self.g.bfs(self.g.find_actor_id("Kevin Bacon"))
        
    def print_rules(self):
        print("Welcome to the Kevin Bacon game! Where you get to see the chain that connects one actor to Kevin Bacon!")
        input("Press enter to start!")

    def print_results(self, actor: str):
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
        actor = str(input("Enter the name of an actor, or type 'return' to quit: "))
        if actor.title() in self.g.actors.values() or actor.lower() == "return":
            return actor
        else:
            print("Actor not valid")

    def graph_results(self, actor: str):
        start_vertex = self.g.get_vertex(self.g.find_actor_id("Kevin Bacon"))
        end_vertex = self.g.get_vertex(self.g.find_actor_id(actor.title()))
        G = nx.Graph()
        while end_vertex is not None and end_vertex is not start_vertex:
            G.add_node(end_vertex.name)
            if end_vertex.predecessor:
                G.add_edge(end_vertex.name, end_vertex.predecessor.name, label=end_vertex.get_movie(end_vertex.predecessor))
            end_vertex = end_vertex.predecessor
        pos = nx.spring_layout(G)
        labels = {node:str(node) for i, node in enumerate(G.nodes())}
        elabels = {edge:G[edge[0]][edge[1]]["label"] for i, edge in enumerate(G.edges())}
        nx.draw_networkx_labels(G, pos, labels)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=elabels)


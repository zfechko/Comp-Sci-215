"""
Title: Graph implementation
Author: Srini Badri
Version: 1.0
Description: An implementation of Vertex and Graph classes
"""

import sys
from collections import deque


class Vertex:
    '''
    keep track of the vertices to which it is connected, and the weight of each edge
    '''
    def __init__(self, key, distance=0, predecessor=None):
        '''

        '''
        self.ID = key
        self.distance = distance
        self.predecessor = predecessor
        self.connected_to = {}

    def __str__(self):
        '''
        returns all of the vertices in the adjacency list, as represented by the connectedTo instance variable
        '''
        return str(self.ID) + ' connected to: ' + str([x.ID for x in self.connected_to])

    def add_neighbor(self, neighbor, weight=0):
        '''
        add a connection from this vertex to another
        '''
        self.connected_to[neighbor] = weight

    def get_connections(self):
        '''

        '''
        return self.connected_to.keys()

    def get_ID(self):
        '''

        '''
        return self.ID

    def get_weight(self, neighbor):
        '''
        returns the weight of the edge from this vertex to the vertex passed as a parameter
        '''
        return self.connected_to[neighbor]

    def get_distance(self):
        '''

        '''
        return self.distance

    def get_predecessor(self):
        '''

        '''
        return self.predecessor

    def set_distance(self, dist):
        '''

        '''
        self.distance = dist

    def set_predecessor(self, pred):
        '''

        '''
        self.predecessor = pred


class Graph:
    '''
    contains a dictionary that maps vertex names to vertex objects.
    '''
    def __init__(self):
        '''

        '''
        self.vert_list = {}
        self.num_vertices = 0

    def __str__(self):
        '''

        '''
        edges = ""
        for vert in self.vert_list.values():
            for vert2 in vert.get_connections():
                edges += "(%s, %s: %d)\n" %(vert.get_ID(), vert2.get_ID(), vert.get_weight(vert2))
        return edges

    def add_vertex(self, key, distance=0, predecessor=None):
        '''
        adding vertices to a graph
        '''
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key, distance, predecessor)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        '''

        '''
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def __contains__(self, n):
        '''
        in operator
        '''
        return n in self.vert_list

    def add_edge(self, f, t, cost=0):
        '''
        connecting one vertex to another
        '''
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], cost)

    def get_vertices(self):
        '''
        returns the names of all of the vertices in the graph
        '''
        return self.vert_list.keys()

    def __iter__(self):
        '''
        for functionality
        '''
        return iter(self.vert_list.values())
        
    def bfs(self, start):
        '''
        enqueue: append left
        dequeue: pop right
        '''
        frontier_queue = deque() #create queue to store vertices in order they are discovered
        start_vertex = self.get_vertex(start)
        start_vertex.set_distance(0)
        frontier_queue.appendleft(start_vertex) #enqueue start vertex to the queue
        discovered_set = set([start_vertex]) #create set 
    
        while len(frontier_queue) > 0: #while queue is not empty
            curr_v = frontier_queue.pop() #dequeue curr_v for processing
            print(curr_v, "distance", curr_v.distance) #print curr_v and its distance
            for adj_v in curr_v.get_connections():
                new_dist = curr_v.get_distance() + curr_v.get_weight(adj_v)
                if adj_v not in discovered_set:
                    frontier_queue.appendleft(adj_v)
                    discovered_set.add(adj_v)
                if new_dist < adj_v.get_distance():
                    adj_v.set_distance(new_dist)
                    adj_v.set_predecessor(curr_v)


def main():
    g = Graph()
    g.add_vertex("121", sys.maxsize, None)
    g.add_vertex("122", sys.maxsize, None)
    g.add_vertex("131", sys.maxsize, None)
    g.add_vertex("132", sys.maxsize, None)
    g.add_vertex("215", sys.maxsize, None)
    g.add_vertex("315", sys.maxsize, None)
    g.add_vertex("415", sys.maxsize, None)
    g.add_vertex("451", sys.maxsize, None)

    g.add_edge("121", "122", 1)
    g.add_edge("121", "131", 1)
    g.add_edge("131", "132", 1)
    g.add_edge("131", "121", 1)
    g.add_edge("122", "215", 1)
    g.add_edge("132", "215", 1)
    g.add_edge("215", "315", 1)
    g.add_edge("215", "415", 1)
    g.add_edge("215", "451", 1)
    g.add_edge("315", "415", 1)
    g.add_edge("315", "451", 1)
    g.add_edge("415", "315", 1)
    g.add_edge("415", "451", 1)
    g.add_edge("451", "315", 1)
    g.add_edge("451", "415", 1)
    
    g.bfs("121")
    
    start_vertex = g.get_vertex("121")
    end_vertex = g.get_vertex("315")
    s = str(end_vertex.get_ID())
    
    # This code will generate error if bfs() method is not implemented correctly
    while end_vertex is not None and end_vertex is not start_vertex:
        s = end_vertex.get_predecessor().get_ID() + "->" + s
        end_vertex = end_vertex.get_predecessor()
        
    print()
    print("Shortest path from 121 to 315:")
    print(s, "\n")


if __name__ == "__main__":
    main()

import pandas as pd
import matplotlib.pyplot as plt
from rich.console import Console
import networkx as nx
from collections import deque
import sys

def create_movies_dict():
    """
    opens moviesTest.txt (will later be changed to movies.txt) and creates a dictionary by parsing each line of the file,
    returns a dictionary of movie ids and movie titles
    """
    movies = dict()
    with open(r'data/movies.txt', "r", encoding="latin-1") as file:
        for line in file:
            k, v = line.strip().split('|')
            movies[k.strip()] = v.strip()
    return movies

def create_actors_dict():
    """
    opens actorsTest.txt (will later be changed to actors.txt) and creates a dictionary by parsing each line of the file,
    returns a dictionary of actor ids and actor names
    """
    actors = dict()
    with open(r'data/actors.txt', "r", encoding="latin-1") as file:
        for line in file:
            k, v = line.strip().split('|')
            actors[k.strip()] = v.strip()
    return actors 


def create_pairs_dict():
    """
    opens movie-actorsTest.txt (will later be changed to movie-actors.txt) and parses the data, if the key doesn't exist, create a list at that index with the value
    if it does exist in the dict, just append the value to that list
    returns a dictionary made up movie ids, and a list of actor ids that star in that film
    """
    pairs = dict()
    with open(r'data/movie-actors.txt', "r", encoding="latin-1") as file:
        for line in file:
            k, v = line.strip().split('|')
            if k not in pairs:
                pairs[k.strip()] = [v.strip()]
            else:
                pairs[k].append(v.strip())
    return pairs 

class Vertex:
    def __init__(self, actor_ID, actor_name, predecessor=None, distance=0):
        self.actor_ID = actor_ID #this will take on the role of the key
        self.name = actor_name
        self.connected_to = dict()
        self.distance = distance
        self.predecessor = predecessor

    def __str__(self):
        '''
        returns all of the vertices in the adjacency list, as represented by the connectedTo instance variable
        '''
        return str(self.name) + ' connected to: ' + str([x.name for x in self.connected_to])


    def add_neighbor(self, neighbor, movie_name: str):
        self.connected_to[neighbor] = movie_name

    def get_connections(self):
        return self.connected_to.keys()

    def get_ID(self):
        return self.actor_ID

    def get_name(self):
        return self.name

    def get_movie(self, neighbor): #get_weight
        return self.connected_to[neighbor]

    def get_movie_id(self, neighbor, dict):
        v = self.connected_to[neighbor]
        for row in dict:
            if dict[row] == v:
                return int(row)



    def get_distance(self):
        return self.distance 
    
    def get_predecessor(self):
        return self.predecessor 

    def set_distance(self, dist: int):
        self.distance = dist

    def set_predecessor(self, pred):
        self.predecessor = pred

    
class Graph:
    def __init__(self):
        self.vert_list = dict()
        self.movies = create_movies_dict()
        self.actors = create_actors_dict()
        self.pairs = create_pairs_dict()
        self.KBNums = dict()
        self.num_vertices = 0

    def add_vertex(self, id, distance=0, predecessor=None):
        """
        given an actor id from the pairs dictionary
        find actor name in actors dict
        create vertex object with actor name, and ID
        return the vertex
        """
        self.num_vertices += 1
        name = self.actors[id] # gives the name of the actor
        new_vertex = Vertex(id, name, predecessor, distance)
        self.vert_list[id] = new_vertex
        return new_vertex

    def __str__(self):
        '''
        String representation of all the connections in the gr4aph
        '''
        edges = ""
        for vert in self.vert_list.values():
            for vert2 in vert.get_connections():
                edges += "(%s, %s: %s)\n" %(vert.get_name(), vert2.get_name(), vert.get_movie(vert2))
        return edges

    def add_edge(self, actor1, actor2, movie_id):
        """
        adds an edge between two existing vertices, there is no 
        """
        common_movie = self.movies[movie_id] #need to change this so it sets the edge weight to the name of the movie, not the id
         #if the two actors have an edge they can use
        self.vert_list[actor1.actor_ID].add_neighbor(self.vert_list[actor2.actor_ID], common_movie)

    def get_vertex(self, id):
        '''
        gets the vertex of an actor in the graph provided an actor id
        '''
        if id in self.vert_list:
            return self.vert_list[id]
        else:
            return None

    def find_actor_id(self, name: str) -> str:
        """
        given an actor name, this function iterates through the actors dictionary and returns the actor's id
        """
        for row in self.actors:
            if self.actors[row] == name:
                return row

    def build_graph(self):
        """
        builds the graph by adding vertices and adding edges if they have a common movie
        """
        for movie in self.movies:
            temp = [] #temp list
            if movie in self.pairs.keys():
                for actor in self.pairs[movie]: #if an actor stars in the given movie
                    if actor not in self.vert_list: #if the actor id has not been added before
                        v = self.add_vertex(actor, sys.maxsize, None)
                    else:
                        v = self.get_vertex(actor)
                    temp.append(v) #append the vertex to the temp list
            for v in temp: #for each vertex in the list
                for i in range(len(temp)): #another pointer
                    if temp[i] != v: #check if it's not pointing to the same vertex
                        self.add_edge(v, temp[i], movie) #adds an edge between the two nodes
                        self.add_edge(temp[i], v, movie)

    def bfs(self, start):
        '''
        performs breadth first search given a start vertex
        '''
        frontier_queue = deque() #create queue to store vertices in order they are discovered
        start_vertex = self.get_vertex(start)
        start_vertex.set_distance(0)
        frontier_queue.appendleft(start_vertex) #enqueue start vertex to the queue
        discovered_set = set([start_vertex]) #create set 
    
        while len(frontier_queue) > 0: #while queue is not empty
            curr_v = frontier_queue.pop() #dequeue curr_v for processing
           # print(curr_v, "distance", curr_v.distance) #print curr_v and its distance
            for adj_v in curr_v.get_connections():
                new_dist = curr_v.get_distance() + curr_v.get_movie_id(adj_v, self.movies)
                if adj_v not in discovered_set:
                    frontier_queue.appendleft(adj_v)
                    discovered_set.add(adj_v)
                if new_dist < adj_v.get_distance():
                    adj_v.set_distance(new_dist)
                    adj_v.set_predecessor(curr_v)
    
    def findAllKBNumbers(self):
        #assuming that we BFS, we can go back to the last pred to find the actor with the highest KB number
        for x in self.vert_list:
            self.KBNums[x] = 0
            vertLookUp = self.vert_list[x].predecessor
            while(vertLookUp != None):
                    vertLookUp = vertLookUp.predecessor
                    self.KBNums[x] += 1
        return 

    def findLargest(self):
        """
        pre-req: must have ran findAllKBNumbers
        finds the largest kb number in the dictionary and returns a list of [the actor vertex, the kb number]
        """
        maxKey = max(self.KBNums, key=self.KBNums.get)
        return [self.actors[maxKey], self.KBNums[maxKey]]

    def findAverage(self):
        """
        Finds the average floor value kevin bacon number and returns it
        """
        values = self.KBNums.values()
        avgKCNumber = sum(values) // len(self.KBNums)
        return avgKCNumber
            

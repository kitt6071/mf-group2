from collections import deque

class Edge:
    def __init__(self, from_node, to, capacity):
        self.from_node = from_node  
        self.to = to  
        self.capacity = capacity  
        self.flow = 0  

    
    def remaining_capacity(self):
        return self.capacity - self.flow

    
    def augment(self, bottleneck):
        self.flow += bottleneck
        self.reverse_edge.flow -= bottleneck  

class Dinics:

    def __init__(self, n, s, t):
        # Initializes the flow network solver

    def add_edge(self, from_node, to, capacity):
        # Adds a directed edge to the flow network

    def bfs(self):
        # Breadth-first search to update levels of nodes, returns True if sink is reachable

    def dfs(self, at, next, flow):
        # Depth-first search to find blocking flow, returns flow value

    def dinic(self):
        # Main function to execute Dinic's algorithm


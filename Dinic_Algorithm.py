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

    def __init__(graph, number, start, end):
        graph.number = number  # Number of nodes in the graph
        graph.start = start  # beginning node index
        graph.end = end  # end node index
        graph.max_flow = 0  # Maximum flow through the network, starts at 0
        graph.list = [[] for _ in range(number)]  # Adjacency list representation of the graph
        #this is a list that explains what nodes are connected to the index node and we will not need this if all the 
        #nodes are connected to eachother
        graph.level = [0] * number  # Level graph used in BFS
        graph.min_cut = [False] * number  # Tracks nodes reachable in the residual graph for min-cut
        #This list is used to keep track of which nodes are reachable from the source node in the residual 
        # graph after the flow has been maximized
        

    def add_edge(self, from_node, to, capacity):
        # Adds a directed edge to the flow network

    def bfs(self):
        # Breadth-first search to update levels of nodes, returns True if sink is reachable

    def dfs(self, at, next, flow):
        # Depth-first search to find blocking flow, returns flow value

    def dinic_Algorithm(self):
        # Main function to execute Dinic's algorithm


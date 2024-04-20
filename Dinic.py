from collections import deque

class Graph:
    # Constructor
    def __init__(self, vertices):
        self.V = vertices # number of vertices in the graph
        self.graph = [[] for _ in range(vertices)] # Initialize graph with empty adj lists for each vertex

    # Adds edges in graph with their capacity
    def add_edge(self, u, v, capacity):
        # Append foward edge with capacity and index of of reverse edge
        self.graph[u].append([v, capacity, len(self.graph[v])])
        # Reverse edge for residual graph
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])

    # Check for path from s -> t
    # Builds level graph by assigning levels
    def breadth_first_search(self, s, t, level):
        # Initialize levels for all nodes that have not been visited
        for i in range(len(level)):
            level[i] = -1

        queue = deque()
        queue.append(s) # Start from source
        level[s] = 0 # Level at source is 0

        while queue:
            u = queue.popleft()

            # Go through all edges of current vertex
            for v, cap, rev in self.graph[u]:
                # If there is a path and capacity is available, update level of vertex 
                if level[v] < 0 and cap > 0:
                    level[v] = level[u] + 1
                    queue.append(v)

        # reutrn true if there is path from s -> t in level graph
        return level[t] >= 0
    
    # Sends flow along paths returned by BFS
    # Takes current node, sink, current flow, and level graph
    def depth_first_search(self, u, t, flow, level):
        # If sink node is reached, return the flow
        if u == t:
            return flow
        
        # Go through all edges in current vertex
        for i in range(len(self.graph[u])):
            # Send min of available flow and edges capacity
            v, cap, rev = self.graph[u][i]

            # If flow is possible, adjust capacities in the graph and return flow
            if level[v] == level[u] + 1 and cap > 0:
                pushed = self.depth_first_search(v, t, min(flow, cap), level)

                if pushed:
                    self.graph[u][i][1] -= pushed
                    self.graph[v][rev][1] += pushed
                    
                    return pushed
        
        # If no flow is possible, return 0
        return 0
    
    # Dinics algorithm to calculate maximum flow from s -> t
    def dinics_algorithm(self, s, t):
        # Initialize levels as not visited
        level = [-1] * self.V
        maxFlow = 0

        # Loop until there is no path from s -> t
        while self.breadth_first_search(s, t, level):
            # Send flow while there is flow from s -> t
            flow = self.depth_first_search(s, t, float('inf'), level)

            # Sum max flow
            while flow:
                maxFlow += flow
                flow = self.depth_first_search(s, t, float('inf'), level)

        # Return calculated max flow
        return maxFlow
    
# Read in a graph from .graph file and create graph object
def read_graph_from_file(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
        nodeCount = len(lines) # Determine number of nodes by number of lines
        graph = Graph(nodeCount) # Initialize graph of size nodeCount

        # Reading each line of the file 
        for u, line in enumerate(lines):
            weights = list(map(int, line.split()))

            # Add edges with capacity to graph
            for v, weight in enumerate(weights):
                if weight > 0:
                    graph.add_edge(u, v, int(weight))
    
    # Return graph object
    return graph


graph = read_graph_from_file('graphs/size4.graph') # *** Change this to match your file path ***
source = 0 # Assumes source vertex is vertex 0
sink = graph.V - 1 # Assumes sink vertex is last vertex in graph
maxFlow = graph.dinics_algorithm(source, sink)

print(f'Maximum flow: {maxFlow}')
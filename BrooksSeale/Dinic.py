from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, capacity):
        self.graph[u].append([v, capacity, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1]) # reverse edge for residual graph

    def breadth_first_search(self, s, t, level):
        for i in range(len(level)):
            level[i] = -1

        queue = deque()
        queue.append(s)
        level[s] = 0

        while queue:
            u = queue.popleft()

            for v, cap, rev in self.graph[u]:
                if level[v] < 0 and cap > 0:
                    level[v] = level[u] + 1
                    queue.append(v)

        return level[t] >= 0
    
    def depth_first_search(self, u, t, flow, level):
        if u == t:
            return flow
        
        for i in range(len(self.graph[u])):
            v, cap, rev = self.graph[u][i]

            if level[v] == level[u] + 1 and cap > 0:
                pushed = self.depth_first_search(v, t, min(flow, cap), level)

                if pushed:
                    self.graph[u][i][1] -= pushed
                    self.graph[v][rev][1] += pushed
                    
                    return pushed
                
        return 0
    
    def dinics_algorithm(self, s, t):
        level = [-1] * self.V
        maxFlow = 0

        while self.breadth_first_search(s, t, level):
            flow = self.depth_first_search(s, t, float('inf'), level)

            while flow:
                maxFlow += flow
                flow = self.depth_first_search(s, t, float('inf'), level)

        return maxFlow
    
def read_graph_from_file(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
        nodeCount = len(lines)
        graph = Graph(nodeCount)

        for u, line in enumerate(lines):
            weights = list(map(int, line.split()))

            for v, weight in enumerate(weights):
                if weight > 0:
                    graph.add_edge(u, v, int(weight))
    
    return graph

# Example usage: Will most likely need to change as project gets more complex.
graph = read_graph_from_file('/Users/brooksseale/Project02/mf-group2/BrooksSeale/graphs/size9.graph')
source = 0 # Assumes source vertex is vertex 0
sink = graph.V - 1 # Assumes sink vertex is last vertex in graph
maxFlow = graph.dinics_algorithm(source, sink)
print(f'Maximum flow: {maxFlow}')
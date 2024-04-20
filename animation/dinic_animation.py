# This is the code for the Dinic's algorithm with animation. It first reads the graph from the file, then it draws the graph. 
# It then runs the Dinic's algorithm and animates the steps of the algorithm.
# Dinic's algorithm is a maximum flow algorithm that finds the maximum flow from a source to a target node in a graph.
# In the breadth first search function, the algorithm finds the shortest path from the source to the target node. 
# It then stores the steps of the algorithm in the animation steps list.
# In the depth first search function, the algorithm finds the maximum flow from the source to the target node. 
# It then stores the steps of the algorithm in the animation steps list.
# Dinic's first runs the breadth first search to find the shortest path from the source to the target node. 
# It then runs the depth first search to find the maximum flow.
# The animation steps are stored in a list of tuples. Each tuple contains the step type, and the nodes involved in the step. 
# The step type is a string, and the nodes are integers.
# The animation steps are then used to animate the steps of the Dinic's algorithm.
# For the breadth first search, the step type is 'bfs_visit', and the nodes are the source and target nodes.
# For the depth first search, the step type is 'dfs_explore', 'dfs_backtrack', or 'dfs_update'.

from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys
from matplotlib.animation import PillowWriter

import numpy as np

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
        # Initialize queue with source node
        queue = deque([s])
        # Set level of source node to 0
        level[s] = 0
        while queue:
            # Dequeue a node from the queue
            u = queue.popleft()
            # Visit all adjacent nodes
            for v, cap, rev in self.graph[u]:
                # If the node has not been visited and there is capacity
                if level[v] < 0 and cap > 0:
                    # Set the level of the node to the current level + 1
                    level[v] = level[u] + 1
                    # Enqueue the node
                    queue.append(v)
                    # Add the step to the animation steps
                    animation_steps.append(('bfs_visit', u, v, list(level)))  # Add 'bfs_visit' identifier
        return level[t] >= 0 # Return True if target node is reached

    # Depth first search to find the maximum flow
    def depth_first_search(self, u, t, flow, level):
        # If the current node is the target node
        if u == t:
            return flow

        # Visit all adjacent nodes
        for i in range(len(self.graph[u])):
            # If the node is reachable and there is capacity
            v, cap, rev = self.graph[u][i]
            if level[v] == level[u] + 1 and cap > 0:
                # Explore the node and add the step to the animation steps
                animation_steps.append(('dfs_explore', u, v))
                # Recursively search for the maximum flow
                pushed = self.depth_first_search(v, t, min(flow, cap), level)
                # If flow is pushed
                if pushed:
                    print(f"DFS at node {u}, pushing flow {pushed} to node {v}")
                    # Add the step to the animation steps of flow update
                    animation_steps.append(('dfs_update', u, v, pushed))
                    # Update the capacity of the edge
                    self.graph[u][i][1] -= pushed
                    # Update the capacity of the reverse edge
                    self.graph[v][rev][1] += pushed
                    return pushed
                else:
                    # Add the step to the animation steps of backtracking
                    animation_steps.append(('dfs_backtrack', u, v))
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

def draw_graph(graph):
    # Draw the graph
    G = nx.DiGraph()
    # Add edges to the graph
    for u in range(len(graph.graph)):
        for v, cap, _ in graph.graph[u]:
            if cap > 0:
                G.add_edge(u, v, capacity=cap)
    # Calculate the layout
    node_count = len(G.nodes())
    k_value = min(1.0, max(0.1, 0.3 * np.sqrt(node_count)))
    # Uses Kamada-Kawai layout to calculate the layout
    pos = nx.kamada_kawai_layout(G)
    fig, ax = plt.subplots(figsize=(15, 10)) 
    # Draw the graph
    nx.draw(G, pos, ax=ax, with_labels=True, node_color='skyblue', node_size=700, edge_color='k', linewidths=1, font_size=15, arrows=True)
    # Draw the edge labels
    edge_labels = {(u, v): d['capacity'] for u, v, d in G.edges(data=True)}
    # Creates the figure for the graph for the animation
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    return fig, ax, G, pos


def read_graph_from_file(fileName):
    # Reads the graph from the file
    with open(fileName, 'r') as file:
        # Reads the lines from the file
        lines = file.readlines()
        # Number of nodes in the graph
        nodeCount = len(lines) 
        graph = Graph(nodeCount) 
        # Adds the edges to the graph
        for u, line in enumerate(lines):
            # Weights of the edges
            weights = list(map(int, line.split()))
            for v, weight in enumerate(weights):
                if weight > 0:
                    graph.add_edge(u, v, int(weight))
    
    return graph

# Animates the steps of the Dinic's algorithm
def animate_step(frame, ax, graph, G, pos):
    print(f"Animating frame {frame}: {animation_steps[frame]}")
    # Clear the graph
    ax.clear()
    # Get the step information
    step_info = animation_steps[frame]
    step_type = step_info[0]

    G.clear()
    # Add edges to the graph
    for u in range(len(graph.graph)):
        for v, cap, _ in graph.graph[u]:
            if cap > 0:  
                G.add_edge(u, v, capacity=cap) 
    # Initialize color map for nodes
    color_map = ['skyblue' for _ in G.nodes()]
    # Initialize color map for edges
    edge_colors = ['k' for _ in G.edges()]

    # Update the color map based on the step type, this is for the breadth first search
    if step_type == 'bfs_visit':
        _, u, v, levels = step_info
        # Update the color map for the nodes
        color_map = ['red' if levels[node] >= 0 else 'skyblue' for node in G.nodes()]
        # Update the color map for the edges
        if (u, v) in G.edges():
            edge_index = list(G.edges()).index((u, v))
            edge_colors[edge_index] = 'green'

    # Update the color map based on the step type, this is for the depth first search
    elif step_type in ['dfs_explore', 'dfs_backtrack', 'dfs_update']:
        _, u, v = step_info[:3]
        explore_color = 'red' if step_type == 'dfs_explore' else 'grey'
        if (u, v) in G.edges():
            edge_index = list(G.edges()).index((u, v))
            edge_colors[edge_index] = explore_color
        color_map[u] = 'green'
        color_map[v] = 'red' if step_type == 'dfs_explore' else 'grey'

    # Draw the graph    
    nx.draw(G, pos, ax=ax, with_labels=True, node_color=color_map, edge_color=edge_colors, node_size=700, linewidths=1, font_size=15, arrows=True)
    # Draw the edge labels
    edge_labels = {(u, v): f"{data['capacity']}" for u, v, data in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

if __name__ == "__main__":
    # Initialize the animation steps
    animation_steps = []
    try:
            graph = read_graph_from_file("size4.graph")
    except Exception as e:
        print("Failed to read graph from file:", e)
        sys.exit(1)
    # Draw the graph
    fig, ax, G, pos = draw_graph(graph)
    # Assumes sink vertex is last vertex in graph
    sink = graph.V - 1 
    graph.dinics_algorithm(0, sink)
    # Print the total number of animation steps
    print(f"Total animation steps: {len(animation_steps)}")
    # Animate the steps
    ani = FuncAnimation(fig, lambda frame: animate_step(frame, ax, graph, G, pos), frames=len(animation_steps), interval=1000, repeat=False)
    plt.show()
    # Save the animation as a gif
    ani.save("dinicsize4.gif", writer=PillowWriter(fps=15))

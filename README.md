# Project Title: Dinic's Algorithm

## Description

This project implements Dinic's Algorithm, a method for computing the maximum flow in a flow network. It leverages the concept of level graphs and blocking flows to efficiently find the maximum flow from a source node to a sink node in a directed graph. The implementation is written in Python and provides an example of applying the algorithm to solve real-world problems that can be modeled as maximum flow problems, such as network traffic optimization, resource allocation, and more.

## Getting Started

### Dependencies

Python 3.x
No external libraries required

### Installing
No installation is necessary, just ensure you have Python 3.x installed on your system.
Download the project files to a local directory.

## Executing Program

1. Prepare Your Graph Data: The program reads the graph data from a .graph file, where the graph is represented as an adjacency matrix. Each line in the file corresponds to a node, and each value in the line represents the capacity of the edge from the node of that line to the node of that column. An example of the contents of a .graph file is provided below.

2. Modify the Main Script (Optional): If necessary, modify the read_graph_from_file function call in the script to match the path to your .graph file.

3. Run the Script: Execute the script using Python.

python Dinic.py

View the Output: After running the script, the maximum flow from the source to the sink node will be printed to the console.
Example .graph File Content

Copy code
0 16 13 0 0 0
0 0 10 12 0 0
0 4 0 0 14 0
0 0 9 0 0 20
0 0 0 7 0 4
0 0 0 0 0 0

This represents a graph with 6 nodes, where the first line represents the capacities of edges going out from the first node to other nodes, and so on.

## Main Functions

add_edge(u, v, capacity): Adds an edge from node u to node v with the specified capacity.
dinics_algorithm(s, t): Computes the maximum flow in the graph from source node s to sink node t.

## Help

Any issues or questions can be raised as issues within the project's repository, or you may directly contact the contributors.

(205)515-2279
(Tripp Davies)

## Authors

### Max Flow Group 2
Alex 
Kittson
Rodney
Sean
Travis 
Tripp 


## Acknowledgments

Inspiration, code snippets, etc.

Dinic's Algorithm Explanation
Python Documentation
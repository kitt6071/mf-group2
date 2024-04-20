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

python3 Dinic.py

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

## Executing Testing 

1. Prepare Your Environment: Ensure Python is installed on your system through the process mentioned previously. 
Install necessary Python libraries (networkx, matplotlib, numpy) by running this installation command:
    pip install networkx matplotlib numpy

2. Prepare Your Graph Data: This script automatically creates graphs through the create graph script that is run after you launch the testing script. Any graph automatically created when running this script is stored in the /testing/graphs directory. The graph_images directory has sample images from the Dinic's algorithm.

3. Modify the Script (Optional):
The testing script is inside the /testing directory. Go to this directory, and run the benchmark_dinics.py through the command:
    python benchmark_dinics.py
Currently, the default graph sizes it creates and tests are hardcoded already inside of the script in the main function as sizes = [10, 20, 50, 100, 200, 500, 1000]. You can change these sizes to change the graph you produce and the graph sizes you test. 

4. Run the Script:
Execute the script using the command:
    python benchmark_dinics.py

5. View the Output:
The script generates random graphs of specified sizes and runs Dinic's algorithm on each graph multiple times to measure the runtime and maximum flow.
For each graph size, it calculates the average runtime and records the maximum flow found. It then plots two graphs:
The first graph shows the average runtime of Dinic's algorithm as a function of the graph size (number of vertices). This plot helps in understanding how the algorithm's performance scales with the size of the graph.
The second graph shows the maximum flow found for each graph size. This plot helps in analyzing the relationship between the graph size and the flow capacity that the algorithm can maximize.
These plots are saved as PNG files with timestamps in their filenames, e.g., dinics_runtime_average_YYYY-MM-DD_HH-MM-SS.png and dinics_max_flow_YYYY-MM-DD_HH-MM-SS.png in the testing directory.

## Main Testing Functions
generate_graphs(sizes): Generates random graphs of specified sizes. It calls an external script (graphs/graphCreator.py) to create these graphs.
run_dinics_algorithm(graph_file): Runs Dinic's algorithm on a specified graph file. It measures the runtime and extracts the maximum flow from the algorithm's output.

## Executing Animation

1. Prepare Your Environment: Ensure Python is installed on your system through the process mentioned previously. 
Install necessary Python libraries (networkx, matplotlib, numpy) by running this installation command:
    pip install networkx matplotlib numpy

2. Prepare Your Graph Data: The script expects a graph file in a specific format. Ensure you have a .graph file ready. For example, size4.graph. 

3. Modify the Main Script (Optional): The dinic_animation.py script is in the /animation directory. Migrate to this directory to run the script. There is a graphs file with graph images and the same graph creation code, but this was just kept to create the size 4, 10, and 20 graphs in the /animation directory. You do not need to migrate to or open files from the animation/graphs directory unless you want to create a new graph. If necessary, modify the main function call in the script to match the path to your .graph file. The code you would change is this code:
    graph = read_graph_from_file("size4.graph")
And you can set it to any graph file in the directory, like size 10 and 20. 

4. Run the Script:
Execute the script using the command in the /animation directory:
    python dinic_animation.py

5. View the Output:
This script visualizes the steps of Dinic's algorithm on a given graph. It first reads the graph from a file, then it animates the process of finding the maximum flow from a source to a target node.
The animation includes steps for both the breadth-first search (BFS) to build level graphs and the depth-first search (DFS) to find augmenting paths.
Each step in the BFS and DFS is visualized, including node visits (highlighted), path explorations, and flow updates.
Finally, the script saves the animation as a GIF file named dinicsize4.gif (this is hardcoded in the dinics_algorithm.py script and will need to be changed if you want to update the name). This file shows the entire process of the algorithm in an animated format.

The directory also has pre-run graph gifs that show both the bfs and dfs algorithms working for Dinic's. 

## Main Animation Functions
read_graph_from_file(fileName): Reads a graph from a specified file. The graph is expected to be in a specific format where each line represents the edges and their capacities from a vertex.
draw_graph(graph): Draws the initial state of the graph using networkx and matplotlib. It visualizes the vertices, edges, and capacities.
animate_step(frame, ax, graph, G, pos): This function is called for each frame of the animation. It updates the graph visualization based on the current step of the algorithm (e.g., BFS visit, DFS explore, DFS backtrack, DFS update).
Graph class: Represents the graph. Contains methods for adding edges (add_edge), performing breadth-first search (breadth_first_search), depth-first search (depth_first_search), and Dinic's algorithm (dinics_algorithm).

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
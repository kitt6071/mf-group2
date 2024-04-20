# This is the code for the benchmarking script. It generates random graphs of specified sizes.
# It then runs the Dinic's algorithm on the graphs and measures the runtime and maximum flow.
# It then plots the results.

import subprocess
import time
import matplotlib.pyplot as plt
from datetime import datetime

# This function generates random graphs of specified sizes.
def generate_graphs(sizes):
    size_args = list(map(str, sizes))
    subprocess.run(['python', 'graphs/graphCreator.py'] + size_args)

# This function runs the Dinic's algorithm on the specified graph file and returns the runtime and maximum flow.
def run_dinics_algorithm(graph_file):
    # Starts the timer
    start_time = time.time()
    # Runs the Dinic's algorithm
    result = subprocess.run(['python', 'Dinic.py', graph_file], capture_output=True, text=True)
    end_time = time.time()
    # Calculates the runtime
    runtime = end_time - start_time
    # Gets the output of the Dinic's algorithm
    output = result.stdout.strip()
    max_flow = int(output.split(':')[-1].strip())
    return runtime, max_flow

def main():
    # These are the hardcoded sizes of the graphs to be generated and benchmarked.
    sizes = [10, 20, 50, 100, 200, 500, 1000]
    # These are the number of iterations to run the Dinic's algorithm.
    iterations = 3  

    print("Generating graphs...")
    generate_graphs(sizes)

    average_runtimes = []
    average_max_flows = []

    # Runs the Dinic's algorithm on each graph and calculate the average runtime and maximum flow.
    for size in sizes:
        total_runtime = 0
        total_max_flow = 0
        for _ in range(iterations):
            # Gets the graph file name
            graph_file = f'graphs/size{size}.graph'
            print(f"Running Dinic's algorithm on graph of size {size}...")
            # Runs the Dinic's algorithm
            runtime, max_flow = run_dinics_algorithm(graph_file)
            # Adds the runtime to the total runtime
            total_runtime += runtime
            total_max_flow = max_flow
            print(f"Runtime: {runtime} seconds, Max Flow: {max_flow}")
        
        # Calculates the average runtime and maximum flow
        avg_runtime = total_runtime / iterations
        average_runtimes.append(avg_runtime)
        average_max_flows.append(total_max_flow)
        print(f"Average runtime for size {size}: {avg_runtime} seconds")
        print(f"Max flow for size {size}: {total_max_flow}\n")

    # Plots the average runtime
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, average_runtimes, 'bo-', label='Average Runtime')
    plt.title('Average Dinic\'s Algorithm Runtime by Graph Size')
    plt.xlabel('Graph Size (Number of Vertices)')
    plt.ylabel('Average Runtime (Seconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'dinics_runtime_average_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png')
    plt.show()

    # Plotting maximum flow
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, average_max_flows, 'ro-', label='Average Max Flow')
    plt.title('Maximum Flow by Graph Size')
    plt.xlabel('Graph Size (Number of Vertices)')
    plt.ylabel('Maximum Flow')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'dinics_max_flow_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png')
    plt.show()

if __name__ == "__main__":
    main()
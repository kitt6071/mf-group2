import subprocess
import time
import matplotlib.pyplot as plt
from datetime import datetime

def generate_graphs(sizes):
    size_args = list(map(str, sizes))
    subprocess.run(['python', 'graphs/graphCreator.py'] + size_args)

def run_dinics_algorithm(graph_file):
    start_time = time.time()
    result = subprocess.run(['python', 'Dinic.py', graph_file], capture_output=True, text=True)
    end_time = time.time()
    runtime = end_time - start_time
    output = result.stdout.strip()
    max_flow = int(output.split(':')[-1].strip())
    return runtime, max_flow

def main():
    sizes = [10, 20, 50, 100, 200, 500, 1000]
    iterations = 3  # Adjust the number of iterations as needed

    print("Generating graphs...")
    generate_graphs(sizes)

    average_runtimes = []
    average_max_flows = []

    for size in sizes:
        total_runtime = 0
        total_max_flow = 0
        for _ in range(iterations):
            graph_file = f'graphs/size{size}.graph'
            print(f"Running Dinic's algorithm on graph of size {size}...")
            runtime, max_flow = run_dinics_algorithm(graph_file)
            total_runtime += runtime
            total_max_flow = max_flow
            print(f"Runtime: {runtime} seconds, Max Flow: {max_flow}")
        
        avg_runtime = total_runtime / iterations
        average_runtimes.append(avg_runtime)
        average_max_flows.append(total_max_flow)
        print(f"Average runtime for size {size}: {avg_runtime} seconds")
        print(f"Max flow for size {size}: {total_max_flow}\n")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, average_runtimes, 'bo-', label='Average Runtime')
    plt.title('Average Dinic\'s Algorithm Runtime by Graph Size')
    plt.xlabel('Graph Size (Number of Vertices)')
    plt.ylabel('Average Runtime (Seconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'dinics_runtime_average_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png')
    plt.show()

    # Plotting average maximum flow
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
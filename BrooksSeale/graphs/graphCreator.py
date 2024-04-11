import random
import os

# def generate_random_graph(size):
#     """Generate a random graph with given size."""
#     graph = []
#     for _ in range(size):
#         graph.append([random.randint(0, 20) for _ in range(size)])
#     return graph
def generate_random_graph(size):
    """Generate a random graph with given size, with more zeros and fewer non-zeros."""
    graph = []
    for _ in range(size):
        row = []
        for _ in range(size):
            # Generate more zeros: 80% chance of zero, 20% chance of a number between 1 and 20
            if random.random() < 0.6:  # Adjust this probability to change the sparsity
                row.append(0)
            else:
                row.append(random.randint(1, 20))
        graph.append(row)
    return graph


def save_graph_to_file(graph, filename):
    """Save the graph to a file."""
    with open(filename, 'w') as f:
        for row in graph:
            f.write(' '.join(map(str, row)) + '\n')

def main():
    # Ask user for the size of the graph
    size = int(input("Enter the size of the graph: "))
    
    # Generate a random graph
    graph = generate_random_graph(size)
    
    # Create a filename based on the size of the graph
    filename = f'size{size}.graph'
    
    # Save the graph to a file
    save_graph_to_file(graph, filename)
    
    print(f"Graph of size {size} has been saved to {filename}")

if __name__ == "__main__":
    main()

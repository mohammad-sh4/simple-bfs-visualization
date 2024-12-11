from graphviz import Digraph
from collections import deque

class Node:
    def __init__(self, name):
        self.name = name
        self.color = "White"
        self.parent = None
        self.d = float('inf')

def bfs(graph, adj_list, start):
    # Initialize all nodes
    for node in graph.values():
        node.color = "White"
        node.parent = None
        node.d = float('inf')
    
    # Start node setup
    start.color = "LightBlue"
    start.d = 0
    queue = deque([start])
    
    step = 0
    visualize(graph, adj_list, queue, f"Step_{step}", "Initial State")
    
    while queue:
        current = queue.popleft()
        for neighbor_name in adj_list[current.name]:
            neighbor = graph[neighbor_name]
            if neighbor.color == "White":
                neighbor.color = "LightBlue"
                neighbor.d = current.d + 1
                neighbor.parent = current.name
                queue.append(neighbor)
        current.color = "Gray"  
        step += 1
        visualize(graph, adj_list, queue, f"Step_{step}", f"Processing {current.name}")
        
def visualize(graph, adj_list, queue, filename, label):
    dot = Digraph(format='png')
    dot.attr(label=f"{label}\nQueue: {list(node.name for node in queue)}", labelloc="t", fontsize="12", fontname="Helvetica")
    
    for node in graph.values():
        color_map = {"White": "white", "LightBlue": "#add8e6", "Gray": "#d3d3d3"}  
        border_color = "red" if node in queue else "black"  # Highlight queue nodes
        dot.node(node.name, 
                 f"{node.name}\n(d={node.d}, p={node.parent})", 
                 style="filled", 
                 fillcolor=color_map[node.color], 
                 fontcolor="black", 
                 color=border_color, 
                 penwidth="2" if node in queue else "1")
    
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            dot.edge(node, neighbor, color="gray")
    
    
    dot.render(filename, cleanup=True)

# Example graph as adjacency list
adj_list = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Create Node objects for each graph vertex
graph_nodes = {name: Node(name) for name in adj_list.keys()}

bfs(graph_nodes, adj_list, graph_nodes['A'])

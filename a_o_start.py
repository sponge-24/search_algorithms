import heapq

class Graph:
    def __init__(self):
        self.graph = {}
        self.weights = {}
        self.heuristic = {}
        self.and_nodes = set()  # Keeps track of AND nodes
    
    def add_edge(self, u, v, cost, is_and_node=False):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, cost))
        self.weights[(u, v)] = cost
        if is_and_node:
            self.and_nodes.add(u)

    def set_heuristic(self, node, heuristic):
        self.heuristic[node] = heuristic

    def display(self):
        for node in self.graph:
            connections = " -> ".join([f"{neighbor} (cost: {cost})" for neighbor, cost in self.graph[node]])
            print(f"{node}: {connections} | Heuristic: {self.heuristic.get(node, 0)}")

def ao_star(graph, heuristic, and_nodes, start, goal):
    def calculate_cost(node, visited):
        # If node is the goal, return 0 cost and path containing only the goal
        if node == goal:
            return 0, [node]
        
        # Avoid revisiting nodes in the current path to prevent cycles
        if node in visited:
            return float('inf'), []
        
        # Mark the node as visited
        visited.add(node)

        # AND node: requires all neighbors to be visited
        if node in and_nodes:
            total_cost = 0
            total_path = [node]
            for neighbor, edge_cost in graph.get(node, []):
                cost, path = calculate_cost(neighbor, visited.copy())
                total_cost += cost + edge_cost
                total_path.extend(path)
            return total_cost, total_path

        # OR node: choose the path with the minimum cost
        else:
            min_cost = float('inf')
            best_path = []
            for neighbor, edge_cost in graph.get(node, []):
                cost, path = calculate_cost(neighbor, visited.copy())
                total_cost = cost + edge_cost
                if total_cost < min_cost:
                    min_cost = total_cost
                    best_path = [node] + path
            return min_cost, best_path

    # Start AO* from the start node
    total_cost, path = calculate_cost(start, set())
    if path:
        print("Path to goal:", " -> ".join(path))
        print("Total cost:", total_cost)
    else:
        print("Goal not reachable")

# Example usage
g = Graph()

# Define the graph with AND nodes and edge costs
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 3)
g.add_edge('C', 'E', 10, is_and_node=True)  # C is an AND node
g.add_edge('C', 'D', 7)
g.add_edge('D', 'E', 2)
g.add_edge('B', 'E', 12)
g.add_edge('B', 'F', 5)
g.add_edge('F', 'Z', 16)
g.add_edge('E', 'Z', 5)

# Set heuristics for each node
g.set_heuristic('A', 14)
g.set_heuristic('B', 12)
g.set_heuristic('C', 11)
g.set_heuristic('E', 4)
g.set_heuristic('D', 6)
g.set_heuristic('F', 11)
g.set_heuristic('Z', 0)

# Run AO* algorithm with start and goal nodes
ao_star(g.graph, g.heuristic, g.and_nodes, 'A', 'Z')

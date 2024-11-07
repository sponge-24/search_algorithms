import random

class Graph():
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    
    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph.get(node, [])}")


def goal_test(node, goal):
    return node == goal

def move_gen(graph, node):
    return graph.get(node, [])

def british_museum_search(graph, start, goal):
    goal_paths = []
    all_nodes = [(start,[start])]

    while all_nodes:
        node, path =   all_nodes.pop(random.randint(0,len(all_nodes)-1))

        print(f"Visting {node}")
        if goal_test(node, goal):
            goal_paths.append(path)

        for neighbour in move_gen(graph, node):
            all_nodes.append((neighbour, path + [neighbour]))

    if  goal_paths:
        print(f"Goal {goal} found!")
        for path in goal_paths:
            print("Path to goal: "," -> ".join(path))
    else:
        print("Goal not found in graph")

g = Graph()

g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('C','E')
g.add_edge('C','D')
g.add_edge('D','E')
g.add_edge('B','E')
g.add_edge('B','F')
g.add_edge('F','Z')
g.add_edge('E','Z')

british_museum_search(g.graph, 'A', 'Z')
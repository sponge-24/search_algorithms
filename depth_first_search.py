from collections import deque

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
    return graph.get(node, [])[::-1]

def depth_fisrt_search(graph, start, goal):
    
    stack = [(start,[start])]

    while stack:
        node, path = stack.pop()

        print(f"Visiting {node}")
        if goal_test(node, goal):
            print(f"Goal {node} found!")
            print("Path to goal: "," -> ".join(path))
            return True
        
        for neighbour in move_gen(graph, node):
            stack.append((neighbour,path+[neighbour]))
        
    print("Goal not found in graph")
    return  False

g = Graph()

list = []

g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('C','E')
g.add_edge('C','D')
g.add_edge('D','E')
g.add_edge('B','E')
g.add_edge('B','F')
g.add_edge('F','Z')
g.add_edge('E','Z')

depth_fisrt_search(g.graph,'A','Z')
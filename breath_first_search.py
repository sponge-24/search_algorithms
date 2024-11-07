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
    return graph.get(node, [])

def breath_fisrt_search(graph, start, goal):
    
    queue = deque()
    queue.append((start,[start]))

    while queue:
        node,path = queue.popleft()
        print(f"Visiting {node}")
        if goal_test(node, goal):
            print(f"Goal {node} found!")
            print("Path to goal: "," -> ".join(path))
            return True

        for neighbour in move_gen(graph, node):
            queue.append((neighbour,path+[neighbour]))
        
    print("Goal not found in graph")
    return  False

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

breath_fisrt_search(g.graph,'A','Z')
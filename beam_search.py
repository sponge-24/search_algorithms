from collections import deque

class Graph():
    def __init__(self):
        self.graph = {}
        self.heuristic = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    
    def set_heuristic(self,node,heuristic):
        self.heuristic[node] = heuristic
    
    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph.get(node, [])}")

def goal_test(node, goal):
    return node == goal

def move_gen(graph, node):
    return graph.get(node, [])

def beam_search(graph, heuristic, beam_width, start, goal):

    queue = deque()
    queue.append((start, [start]))

    while queue:

        level_nodes = []

        while queue:
            node,path = queue.popleft()
            print(f"Visiting {node}")
            
            if goal_test(node, goal):
                print(f"Goal {node} found!")
                print("Path to goal:", " -> ".join(path))
                return True
            
            for neighbour in move_gen(graph, node):
                level_nodes.append((neighbour, path + [neighbour]))

        level_nodes = sorted(level_nodes, key = lambda x : heuristic[x[0]])[:beam_width]

        queue.extend(level_nodes)

    print("Goal not found in graph")
    return False

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


g.set_heuristic('A',14)
g.set_heuristic('B',12)
g.set_heuristic('C',11)
g.set_heuristic('E',4)
g.set_heuristic('D',6)
g.set_heuristic('F',11)
g.set_heuristic('Z',0)


beam_search(g.graph, g.heuristic, 2,  'A', 'Z')

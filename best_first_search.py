import heapq

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

def best_first_search(graph, heuristic, start, goal):
    heap = []
    heapq.heappush(heap, (heuristic[start],(start,[start])))

    while heap:

        total_cost, node = heapq.heappop(heap)

        print(f"Visiting {node[0]}")

        if goal_test(node[0], goal):
            print(f"Goal {node[0]} found!")
            print("Path to goal:", " -> ".join(node[1]))
            return True
        
        for neighbour in move_gen(graph, node[0]):
                heapq.heappush(heap, (heuristic[neighbour], (neighbour, node[1] + [neighbour])))

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


best_first_search(g.graph, g.heuristic, 'A','Z')


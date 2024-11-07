import heapq

class Graph():
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v, c):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v,c))
    
    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph.get(node, [])}")

def goal_test(node, goal):
    return node == goal

def move_gen(graph, node):
    return graph.get(node, [])

def branch_and_bound_with_extented_list(graph, start, goal):
    heap = []
    total_cost = 0
    heapq.heappush(heap, (total_cost,(start,[start])))

    while heap:

        total_cost, node = heapq.heappop(heap)

        print(f"Visiting {node[0]}")

        if goal_test(node[0], goal):
            print(f"Goal {node[0]} found!")
            print("Path to goal:", " -> ".join(node[1]))
            return True
        
        for neighbour, cost in move_gen(graph, node[0]):
                cost_so_far =  total_cost + cost
                heapq.heappush(heap, (cost_so_far, (neighbour, node[1] + [neighbour])))

    print("Goal not found in graph")
    return False

g = Graph()

g.add_edge('A','B',4)
g.add_edge('A','C',3)
g.add_edge('C','E',10)
g.add_edge('C','D',7)
g.add_edge('D','E',2)
g.add_edge('B','E',12)
g.add_edge('B','F',5)
g.add_edge('F','Z',16)
g.add_edge('E','Z',5)

branch_and_bound_with_extented_list(g.graph,'A','Z')


import heapq

class Graph():
    def __init__(self):
        self.graph = {}
        self.heuristic = {}
    
    def add_edge(self, u, v, c):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v,c))

    def set_heuristic(self,node,heuristic):
        self.heuristic[node] = heuristic
    
    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph.get(node, [])}")

def goal_test(node, goal):
    return node == goal

def move_gen(graph, node):
    return graph.get(node, [])

def branch_and_bound_with_heuristic(graph, heuristic, oracle, start, goal):
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
                if oracle >= cost_so_far + heuristic[neighbour]:
                    heapq.heappush(heap, (cost_so_far, (neighbour, node[1] + [neighbour])))
    
    print("Goal not found with the given oracle")
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

g.set_heuristic('A',14)
g.set_heuristic('B',12)
g.set_heuristic('C',11)
g.set_heuristic('E',4)
g.set_heuristic('D',6)
g.set_heuristic('F',11)
g.set_heuristic('Z',0)

branch_and_bound_with_heuristic(g.graph, g.heuristic, 15, 'A', 'Z')
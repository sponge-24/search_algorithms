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

def oracle_search(graph, oracle, start, goal):
    total_cost = 0
    stack = [(total_cost,start,[start])]
    goal_paths = []

    while stack:
        total_cost, node, path = stack.pop()

        print(f"Visiting {node}")
        if goal_test(node, goal):
            goal_paths.append(path)

        for neighbour, cost in move_gen(graph, node)[::-1]:
            cost_so_far = total_cost + cost
            if oracle >= cost_so_far:
                stack.append((cost_so_far, neighbour, path + [neighbour]))

    if  goal_paths:
        print(f"Goal {goal} found!")
        for path in goal_paths:
            print("Path to goal: "," -> ".join(path))
    else:
        print("Goal not found with the given oracle")


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

oracle_search(g.graph, 17, 'A', 'Z')
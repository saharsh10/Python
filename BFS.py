graph={
    'A' : ['B', 'C', 'D', 'E'],
    'B' : ['A', 'C', 'G'],
    'C' : ['A', 'B', 'D'],
    'D' : ['A', 'C', 'E', 'H'],
    'E' : ['A', 'D', 'F'],
    'F' : ['E', 'G', 'H'],
    'G' : ['B', 'F'],
    'H' : ['D', 'F']
}

visited = []
queue = []

def bfs(graph, visited, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s)

        for neighbor in graph:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

bfs(graph, visited, 'A')
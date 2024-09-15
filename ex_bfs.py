graph = {
    'S': ['A', 'B', 'D'],
    'A': ['C'],
    'B': ['D'],
    'C': ['G', 'D'],
    'D': ['G']
    
}
def bfs(graph, start, goal):
    visited = []
    queue =[[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for node2 in adjacent_nodes:
                if node2 not in path:
                    new_path = list(path)
                    new_path.append(node2)
                    queue.append(new_path)
                    
      
                    
solution = bfs(graph, 'S', 'G')
print('Solution is ',solution)                                   
                
               
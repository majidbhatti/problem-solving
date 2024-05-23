def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Create an empty set to store visited nodes
    visited.add(start)  # Mark the current node as visited
    print(start)  # Print or process the current node

    # Visit all adjacent nodes that have not been visited yet
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # Recursively call dfs for each neighbor


# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Call dfs starting from node 'A'
dfs(graph, 'A')

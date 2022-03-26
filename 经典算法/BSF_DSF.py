graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def BFS(graph, start_vertex):
    queue = [start_vertex]
    visited = set(start_vertex)
    parent = {start_vertex: None}
    while len(queue) != 0:
        current_vertex = queue.pop(0)
        print(current_vertex)  # visit current vertex
        for vertex in graph[current_vertex]:
            if vertex not in visited:
                parent[vertex] = current_vertex
                visited.add(vertex)
                queue.append(vertex)
    return parent


def DFS(graph, start_vertex):
    stack = [start_vertex]
    visited = set(start_vertex)
    parent = {start_vertex: None}
    while len(stack) != 0:
        current_vertex = stack.pop()
        print(current_vertex)  # visit current vertex
        for vertex in graph[current_vertex]:
            if vertex not in visited:
                visited.add(vertex)
                stack.append(vertex)
                parent[vertex] = current_vertex
    return parent


if __name__ == '__main__':
    print("===========BSF===========")
    parent = BFS(graph, "A")
    print("parent: ", parent)

    print("from E --> ", end='')
    previous_vetex = parent['E']
    while previous_vetex is not None:
        print(previous_vetex, '--> ', end='')
        previous_vetex = parent[previous_vetex]

    print("\n\n===========DFS===========")
    parent = DFS(graph, "A")
    print("parent: ", parent)

import math
import heapq

graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}


def init_distance(graph):
    distance = {'A': 0}
    for vertex in graph:
        if vertex != 'A':
            distance[vertex] = math.inf
    return distance


def dijkstra():
    priority_queue = [(0, 'A')]
    visited = set()
    distance = init_distance(graph)
    parent = {}
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        visited.add(current_vertex)
        for next_vertex in graph[current_vertex]:
            if next_vertex not in visited:
                next_distance = current_distance + graph[current_vertex][next_vertex]
                if next_distance < distance[next_vertex]:
                    distance[next_vertex] = next_distance
                    parent[next_vertex] = current_vertex
                    heapq.heappush(priority_queue, (next_distance, next_vertex))
    return distance, parent


if __name__ == '__main__':
    distance, parent = dijkstra()
    print('======== distance =============')
    print(distance)
    print('========= parent ==========')
    print(parent)


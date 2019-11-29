import heapq
import numpy as np
import math


n = 9
visited = np.zeros(n)
distance = [math.inf] * n
start = 0
distance[start] = 0
x = [(0, start)]
m = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
     [4, 0, 8, 0, 0, 0, 0, 11, 0],
     [0, 8, 0, 7, 0, 4, 0, 0, 2],
     [0, 0, 7, 0, 9, 14, 0, 0, 0],
     [0, 0, 0, 9, 0, 10, 0, 0, 0],
     [0, 0, 4, 14, 10, 0, 2, 0, 0],
     [0, 0, 0, 0, 0, 2, 0, 1, 6],
     [8, 11, 0, 0, 0, 0, 1, 0, 7],
     [0, 0, 2, 0, 0, 0, 6, 7, 0]
     ]
while len(x) != 0:
    cur_dist, cur_node = heapq.heappop(x)
    # print(cur_dist)
    visited[cur_node] = 1
    if distance[cur_node] < cur_dist: continue
    for edge in range(0, n):
        # print(edge)
        if visited[edge]: continue
        if m[cur_node][edge] == 0 and edge != cur_node: continue
        new_dist = distance[cur_node] + m[cur_node][edge]
        if new_dist < distance[edge]:
            distance[edge] = new_dist
            heapq.heappush(x, (new_dist, edge))
print(distance)
'''
import heapq


def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances


example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}print(calculate_distances(example_graph, 'X'))
# => {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2}
'''
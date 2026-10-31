# algorithm.py

import heapq
from graph import city_graph


def dijkstra(start, end):

    # Initialize distances
    distances = {node: float('inf') for node in city_graph}
    distances[start] = 0

    # Store previous nodes
    previous = {}

    # Priority Queue
    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if a better distance already exists
        if current_distance > distances[current_node]:
            continue

        # Destination reached
        if current_node == end:
            break

        # Check neighbouring nodes
        for neighbour, weight in city_graph[current_node].items():

            distance = current_distance + weight

            if distance < distances[neighbour]:

                distances[neighbour] = distance
                previous[neighbour] = current_node

                heapq.heappush(
                    priority_queue,
                    (distance, neighbour)
                )

    # Reconstruct shortest path
    path = []
    current = end

    if distances[end] == float('inf'):
        return None, float('inf')

    while current in previous:
        path.append(current)
        current = previous[current]

    path.append(start)
    path.reverse()

    return path, distances[end]
def get_path(dest, predecessors):
    # Tirith",
    # {"Minas Tirith": "Isengard", "Isengard": "Gondor", "Gondor": "Rivendell"},
    # ["Rivendell", "Gondor", "Isengard", "Minas Tirith"],
    visited = []
    to_visit = dest

    while to_visit is not None:
        visited.append(to_visit)
        to_visit = predecessors.get(to_visit, None)

    # if to_visit != "":
    #     visited.append(to_visit)

    return visited[::-1]


def next_nearest_node(distances, unvisited):

    # {"Minas Tirith": 4, "Isengard": 2, "Gondor": 3, "Mirkwood": 1},
    # {"Minas Tirith", "Gondor"},
    # "Gondor",
    if len(unvisited) == 0:
        return None

    shortest = float("inf")
    shortest_place = None
    for place in unvisited:
        if place in distances:
            if distances[place] < shortest:
                shortest = distances[place]
                shortest_place = place
    return shortest_place


def dijkstra(graph, src, dest):
    # {
    #     "Minas Tirith": {"Isengard": 4, "Gondor": 1},
    #     "Isengard": {"Minas Tirith": 4, "Bree": 3, "Mirkwood": 8},
    #     "Gondor": {"Minas Tirith": 1, "Bree": 2, "Misty Mountains": 6},
    #     "Bree": {"Gondor": 2, "Isengard": 3, "Mirkwood": 4},
    #     "Mirkwood": {"Bree": 4, "Isengard": 8, "Lothlorien": 2},
    #     "Misty Mountains": {"Gondor": 6, "Lothlorien": 8},
    #     "Lothlorien": {"Misty Mountains": 8, "Mirkwood": 2},
    # },
    # "Minas Tirith",
    # "Lothlorien",
    # ["Minas Tirith", "Gondor", "Bree", "Mirkwood", "Lothlorien"],

    unvisited = set()
    predecessors = {}
    distances = {}

    for node in graph:
        unvisited.add(node)
        if node != src:
            distances[node] = float("inf")
        else:
            distances[node] = 0

    print(f"unvisited: {unvisited}")
    print(f"{src} -->")
    return dijkstras_r(graph, src, dest, unvisited, predecessors, distances)


def dijkstras_r(graph, src, dest, unvisited, predecessors, distances):
    if src == dest:
        return get_path(dest, predecessors)

    neighbors = graph[src]

    for neighbor in neighbors:
        if neighbor in unvisited:
            distance_from_src_to_next_nearest = distances[src]
            distance_from_next_nearest_to_neighbor = neighbors[neighbor]
    
            dist_src_to_neighbor = (
                distance_from_src_to_next_nearest
                + distance_from_next_nearest_to_neighbor
            )
            if dist_src_to_neighbor < distances[neighbor]:
                distances[neighbor] = dist_src_to_neighbor
                predecessors[neighbor] = src
            
    unvisited.remove(src)

    min_dist = float("inf")
    next_node = None
    for node in unvisited:
        if distances[node] < min_dist:
            min_dist = distances[node]
            next_node = node

    if next_node is None:
        return []

    return dijkstras_r(graph, next_node, dest, unvisited, predecessors, distances)

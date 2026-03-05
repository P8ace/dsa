"""
A graph is a set of vertices and edges that connect to those vertices.
All trees are graphs, but not all graphs are trees.

Graphs can have any number of vertices.
An undirected graph can have upto n(n-1)/2 edges for n vertices.
Graphs do not need a root vertex.

**Adjacency list**:
    An adjacency list stores a list of vertices for each vertex that indicates where the connections are:
        0 	connects with 	1 	4
        1 	connects with 	0 	2 	3 	4
        2 	connects with 	1 	3
        3 	connects with 	1 	2 	4
        4 	connects with 	0 	1 	3

"""


class Graph:
    """
    Here we use a matrix(list of lists to represent a graph)
    """

    def __init__(self, num_vertices):
        self.graph = [[False for n in range(num_vertices)] for n in range(num_vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = True
        self.graph[v][u] = True

    # don't touch below this line

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]


class Graph_with_adjacency_list:
    """
    Uses adjancency list to represent the graph
    """

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = set()
        if v not in self.graph:
            self.graph[v] = set()
        self.graph[u].add(v)
        self.graph[v].add(u)

    # don't touch below this line

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False

    def adjacent_nodes(self, node):
        if node in self.graph:
            return self.graph[node]
        return set()

    def add_node(self, u):
        if u not in self.graph:
            self.graph[u] = set()

    def unconnected_vertices(self):
        actual = []
        for key, value in self.graph.items():
            if value == set():
                actual.append(key)

        return actual

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result

    def breadh_first_search(self, v):
        """
        Bread First Search(BFS) is an algorithm to traverse/search a tree/graph.
        It starts at root/(some arbitrary node) and explores all nodes at present depth before going to next level.

        PseudoCode:
            add neighbors of current node to a list and then visit them also adding their neighbors and so on.

        O(V+E) V is vertices and E is Edges of a graph.
        Used for: Shortest path in a graph, web crawling
        """
        visited = []
        to_explore = []
        to_explore.append(v)
        while len(to_explore) > 0:
            to_visit = to_explore[0]
            del to_explore[0]
            visited.append(to_visit)
            neighbors = sorted(self.graph[to_visit])
            for neighbor in neighbors:
                if neighbor not in visited:
                    if neighbor not in to_explore:
                        to_explore.append(neighbor)
        return visited

    def depth_first_search(self, start_vertex):
        """
        Depth first search is an algorithm to traverse/search a tree/graph.
        It starts at root/(some arbitrary node of a graph) and explores as far as possible along each branch before backtracking and starting at next branch.

        """

        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        neighbors = sorted(self.graph[current_vertex])
        for neighbor in neighbors:
            if neighbor not in visited:
                self.depth_first_search_r(visited, neighbor)

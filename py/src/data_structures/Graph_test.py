from src.data_structures.Graph import Graph, Graph_with_adjacency_list
def test_Graph_add_edge():
    run_cases = [
        (
            3,
            [
                (0, 1),
                (2, 0),
            ],
            (
                [
                    (1, 0),
                    (1, 2),
                    (2, 0),
                ],
                [True, False, True],
            ),
        ),
        (
            6,
            [
                (0, 1),
                (1, 2),
                (2, 3),
                (3, 4),
                (4, 5),
            ],
            (
                [
                    (0, 1),
                    (1, 2),
                    (0, 4),
                    (2, 5),
                    (5, 0),
                ],
                [True, True, False, False, False],
            ),
        ),
    ]
    submit_cases = run_cases + [
        (
            6,
            [
                (0, 1),
                (2, 4),
                (2, 1),
                (3, 1),
                (4, 5),
            ],
            (
                [
                    (5, 4),
                    (1, 5),
                    (0, 4),
                    (2, 5),
                    (1, 3),
                ],
                [True, False, False, False, True],
            ),
        ),
    ]
    for test_case in submit_cases:
        num_of_vertices = test_case[0]
        graph = Graph(num_of_vertices)
        for edge in test_case[1]:
            graph.add_edge(edge[0],edge[1])
        
        actual = []
        for i,edge in enumerate(test_case[2][0]):
            exists = graph.edge_exists(edge[0],edge[1])
            actual.append(exists)
            
        assert actual == test_case[2][1]
        
def test_graph_with_adjacecy_list():
    run_cases = [
        (
            [
                (0, 1),
                (2, 0),
            ],
            (
                [
                    (1, 0),
                    (1, 2),
                    (2, 0),
                ],
                [True, False, True],
            ),
        ),
        (
            [
                (0, 1),
                (1, 2),
                (2, 3),
                (3, 4),
                (4, 5),
            ],
            (
                [
                    (0, 1),
                    (1, 2),
                    (0, 4),
                    (2, 5),
                    (5, 0),
                ],
                [True, True, False, False, False],
            ),
        ),
    ]
    submit_cases = run_cases + [
        (
            [
                (0, 1),
                (2, 4),
                (2, 1),
                (3, 1),
                (4, 5),
            ],
            (
                [
                    (5, 4),
                    (1, 5),
                    (0, 4),
                    (2, 5),
                    (1, 3),
                ],
                [True, False, False, False, True],
            ),
        ),
    ]
    for test_case in submit_cases:
        graph= Graph_with_adjacency_list()
        for edge in test_case[0]:
            graph.add_edge(edge[0],edge[1])
            
        actual=[]
        for i,edge in enumerate(test_case[1][0]):
            exists = graph.edge_exists(edge[0],edge[1])
            actual.append(exists)
        
        assert actual == test_case[1][1]
        
def test_adjacent_nodes():
    run_cases = [
        (
            [
                (0, 1),
                (1, 2),
                (2, 3),
                (3, 4),
                (4, 5),
            ],
            ([0, 1, 2, 3, 4, 5], [{1}, {0, 2}, {1, 3}, {2, 4}, {3, 5}, {4}]),
        ),
        (
            [
                (0, 1),
                (0, 2),
                (0, 3),
                (1, 2),
                (1, 3),
            ],
            ([0, 1, 2, 3], [{1, 2, 3}, {0, 2, 3}, {0, 1}, {0, 1}]),
        ),
    ]
    submit_cases = run_cases + [
        (
            [
                (0, 2),
                (2, 4),
                (2, 1),
                (3, 1),
                (4, 5),
            ],
            ([0, 2, 5], [{2}, {0, 1, 4}, {4}]),
        ),
    ]
    for test_case in submit_cases:
        graph = Graph_with_adjacency_list()
        for i,edge in enumerate(test_case[0]):
            graph.add_edge(edge[0],edge[1])
        actual = []
        for i,edge in enumerate(test_case[1][0]):
            adj_nodes = graph.adjacent_nodes(edge)
            actual.append(adj_nodes)
        
        assert actual == test_case[1][1]
        
def test_unconnected_vertices():
    run_cases = [
        (
            [
                (0, 1),
                (1, 2),
                (2, 3),
                (3, 4),
                (4, 5),
            ],
            [6, 7],
        ),
        (
            [
                (1, 2),
                (1, 3),
            ],
            [0, 4],
        ),
    ]
    submit_cases = run_cases + [
        (
            [
                (0, 5),
                (7, 0),
            ],
            [1, 2, 3, 4],
        )
    ]
    for test_case in submit_cases:
        graph = Graph_with_adjacency_list()
        for edge in test_case[0]:
            graph.add_edge(edge[0],edge[1])
        for node in test_case[1]:
            graph.add_node(node)
            
        unconnected = graph.unconnected_vertices()
        assert unconnected == test_case[1]
        
def test_breadth_fist_search():
    run_cases = [
        (
            [
                ("New York", "London"),
                ("New York", "Cairo"),
                ("New York", "Tokyo"),
                ("London", "Dubai"),
            ],
            "New York",
            ["New York", "Cairo", "London", "Tokyo", "Dubai"],
        ),
    ]
    submit_cases = run_cases + [
        (
            [
                ("New York", "London"),
                ("New York", "Cairo"),
                ("New York", "Tokyo"),
                ("London", "Dubai"),
                ("Cairo", "Kyiv"),
                ("Cairo", "Madrid"),
                ("London", "Madrid"),
                ("Buenos Aires", "New York"),
                ("Tokyo", "Buenos Aires"),
                ("Kyiv", "San Francisco"),
            ],
            "New York",
            [
                "New York",
                "Buenos Aires",
                "Cairo",
                "London",
                "Tokyo",
                "Kyiv",
                "Madrid",
                "Dubai",
                "San Francisco",
            ],
        ),
    ]
    
    for test_case in submit_cases:
        graph = Graph_with_adjacency_list()
        for edge in test_case[0]:
            graph.add_edge(edge[0],edge[1])
        
        bfs = graph.breadh_first_search(test_case[1])
        
        assert bfs == test_case[2]
        
def test_depth_first_search():
    run_cases = [
        (
            [
                ("New York", "London"),
                ("New York", "Cairo"),
                ("New York", "Tokyo"),
                ("London", "Dubai"),
            ],
            "New York",
            ["New York", "Cairo", "London", "Dubai", "Tokyo"],
        ),
    ]
    submit_cases = run_cases + [
        (
            [
                ("New York", "London"),
                ("New York", "Cairo"),
                ("New York", "Tokyo"),
                ("London", "Dubai"),
                ("Cairo", "Kyiv"),
                ("Cairo", "Madrid"),
                ("London", "Madrid"),
                ("Buenos Aires", "New York"),
                ("Tokyo", "Buenos Aires"),
                ("Kyiv", "San Francisco"),
            ],
            "New York",
            [
                "New York",
                "Buenos Aires",
                "Tokyo",
                "Cairo",
                "Kyiv",
                "San Francisco",
                "Madrid",
                "London",
                "Dubai",
            ],
        ),
    ]
    for test_case in submit_cases:
        graph = Graph_with_adjacency_list()
        for edge in test_case[0]:
            graph.add_edge(edge[0],edge[1])
        dfs = graph.depth_first_search(test_case[1])
        
        assert dfs == test_case[2]
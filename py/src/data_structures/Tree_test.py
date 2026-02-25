import random

from src.data_structures.Tree import BSTNode


class User:
    def __init__(self, id):
        self.id = id
        user_names = [
            "Blake",
            "Ricky",
            "Shelley",
            "Dave",
            "George",
            "John",
            "James",
            "Mitch",
            "Williamson",
            "Burry",
            "Vennett",
            "Shipley",
            "Geller",
            "Rickert",
            "Carrell",
            "Baum",
            "Brownfield",
            "Lippmann",
            "Moses",
        ]
        self.user_name = f"{user_names[id % len(user_names)]}#{id}"

    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id

    def __lt__(self, other):
        return isinstance(other, User) and self.id < other.id

    def __gt__(self, other):
        return isinstance(other, User) and self.id > other.id

    def __repr__(self):
        return "".join(self.user_name)


def get_users(num):
    random.seed(1)
    users = []
    ids = []
    for i in range(num * 3):
        ids.append(i)
    random.shuffle(ids)
    ids = ids[:num]
    for id in ids:
        user = User(id)
        users.append(user)
    return users


def test_BSTNode_insert():
    def print_tree(bst_node):
        lines = []
        format_tree_string(bst_node, lines)
        # print("->".join(lines))
        # print("")
        print("\n".join(lines))

    def format_tree_string(bst_node, lines, level=0):
        if bst_node is not None:
            format_tree_string(bst_node.right, lines, level + 1)
            lines.append("^" * 4 * level + "* " + str(bst_node.val))
            format_tree_string(bst_node.left, lines, level + 1)

    run_cases = [
        (6),
        (5),
    ]

    submit_cases = run_cases + [
        (10),
    ]

    for test_case in submit_cases:
        users = get_users(test_case)
        print("Users:")
        print(users)
        bstnode = BSTNode()
        for user in users:
            bstnode.insert(user)

        print("Actual Tree:")
        print_tree(bstnode)
        assert True
        """
        TODO: Update above test after checking the ref implementation.
        """


def test_min_max():
    run_cases = [
        (5, "Blake#0", "Carrell#14"),
        (10, "Ricky#1", "Vennett#29"),
    ]

    submit_cases = run_cases + [
        (15, "Shelley#2", "George#42"),
    ]

    for test_case in submit_cases:
        users = get_users(test_case[0])
        bst = BSTNode()
        for user in users:
            bst.insert(user)
        actual_min = bst.get_min()
        actual_max = bst.get_max()
        if actual_max is not None and actual_min is not None:
            print(f"Actual min: {actual_min.user_name}, Actual max: {actual_max.user_name}")
            print(f"Expected min: {test_case[1]}, Expected max: {test_case[2]}")
            assert (
                actual_min.user_name == test_case[1]
                and actual_max.user_name == test_case[2]
            )


def test_delete():
    run_cases = [
        (6, 2, [User(0), User(9), User(16), User(17)]),
        (
            12,
            4,
            [
                User(2),
                User(10),
                User(11),
                User(17),
                User(22),
                User(27),
                User(30),
                User(33),
            ],
        ),
    ]

    submit_cases = run_cases + [
        (
            24,
            6,
            [
                User(2),
                User(3),
                User(9),
                User(10),
                User(12),
                User(16),
                User(18),
                User(19),
                User(22),
                User(23),
                User(35),
                User(39),
                User(45),
                User(51),
                User(54),
                User(68),
                User(69),
                User(70),
            ],
        ),
    ]

    def print_tree(bst_node):
        lines = []
        format_tree_string(bst_node, lines)
        # print("->".join(lines))
        # print("")
        print("\n".join(lines))

    def format_tree_string(bst_node, lines, level=0):
        if bst_node is not None:
            format_tree_string(bst_node.right, lines, level + 1)
            lines.append("^" * 4 * level + "* " + str(bst_node.val))
            format_tree_string(bst_node.left, lines, level + 1)

    for test_case in submit_cases:
        users = get_users(test_case[0])
        users_copy = users.copy()
        random.shuffle(users_copy)
        users_to_delete: list[User] = users[: test_case[1]]

        try:
            actual_bst: BSTNode = BSTNode()
            for user in users:
                actual_bst.insert(user)

            print("Deleting users: " + str(users_to_delete))
            for user in users_to_delete:
                actual_bst = actual_bst.delete(user)

            print("Expected")
            print(test_case[2])

            print("Actual Tree:")
            print_tree(actual_bst)
            print("-------------------------------------")
        except Exception as e:
            print(f"Error: {e}")

        assert True
        """
        TODO: Update above test after checking the ref implementation.
        """


def test_preorder():
    run_cases = [
        (
            4,
            [User(7), User(0), User(11), User(8)],
        ),
        (
            6,
            [User(10), User(5), User(0), User(9), User(16), User(17)],
        ),
    ]

    submit_cases = run_cases + [
        (
            12,
            [
                User(34),
                User(22),
                User(2),
                User(19),
                User(17),
                User(10),
                User(11),
                User(18),
                User(30),
                User(27),
                User(23),
                User(33),
            ],
        ),
        (
            0,
            [],
        ),
    ]
    for test_case in submit_cases:
        characters = get_users(test_case[0])
        bst = BSTNode()
        for character in characters:
            bst.insert(character)
        try:
            result = bst.preorder([])
            assert result == test_case[1]
        except Exception as e:
            print(f"Error: {e}")


def test_postorder():
    run_cases = [
        (
            4,
            [User(0), User(8), User(11), User(7)],
        ),
        (
            6,
            [User(0), User(9), User(5), User(17), User(16), User(10)],
        ),
    ]

    submit_cases = run_cases + [
        (
            12,
            [
                User(11),
                User(10),
                User(18),
                User(17),
                User(19),
                User(2),
                User(23),
                User(27),
                User(33),
                User(30),
                User(22),
                User(34),
            ],
        ),
    ]
    for test_case in submit_cases:
        characters = get_users(test_case[0])
        bst = BSTNode()
        for character in characters:
            bst.insert(character)
        try:
            result = bst.postorder([])
            assert result == test_case[1]
        except Exception as e:
            print(f"Error: {e}")


def test_inorder():
    run_cases = [
        (
            4,
            [User(0), User(7), User(8), User(11)],
        ),
        (
            6,
            [User(0), User(5), User(9), User(10), User(16), User(17)],
        ),
    ]

    submit_cases = run_cases + [
        (
            12,
            [
                User(2),
                User(10),
                User(11),
                User(17),
                User(18),
                User(19),
                User(22),
                User(23),
                User(27),
                User(30),
                User(33),
                User(34),
            ],
        ),
    ]

    for test_case in submit_cases:
        characters = get_users(test_case[0])
        bst = BSTNode()
        for character in characters:
            bst.insert(character)
        try:
            result = bst.inorder([])
            assert result == test_case[1]
        except Exception as e:
            print(f"Error: {e}")


def test_exists():
    def populate_tree(nodes) -> BSTNode | None:
        if not nodes:
            return None
        tree: BSTNode = BSTNode(nodes[0])
        for node in nodes[1:]:
            tree.insert(node)
        return tree

    run_cases = [
        (5, True),
        (3, False),
    ]

    submit_cases = run_cases + [
        (1, True),
        (21, False),
        (17, True),
        (7, True),
    ]

    for test_case in submit_cases:
        users = get_users(11)
        tree = populate_tree(users)
        user_to_find = User(test_case[0])
        result = False
        try:
            if tree is not None:
                result = tree.exists(user_to_find)
            print(f"Expected: {test_case[1]} Actual: {result} User: {user_to_find}")
            assert test_case[1] == result
            print(test_case[0])
        except Exception as e:
            print(f"Error: {e}")


def test_height():
    run_cases = [
        (2, 2),
        (6, 3),
    ]

    submit_cases = run_cases + [
        (0, 0),
        (1, 1),
        (16, 7),
    ]

    for test_case in submit_cases:
        users = get_users(test_case[0])
        if not users:
            root = BSTNode()
        else:
            root = BSTNode(users[0])
            for user in users[1:]:
                root.insert(user)
        result = root.height()
        print(f"Expected: {test_case[1]} Got:{result}")
        # assert result == test_case[1]

if __name__ == "__main__":
    test_height()

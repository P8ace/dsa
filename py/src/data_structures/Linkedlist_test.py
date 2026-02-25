import random

from src.data_structures.Linkedlist import LinkedList, LLQueue, Node


def test_Linkedlist():
    def linked_list_to_list(node):
        result = []
        current = node
        while current:
            result.append(current.val)
            current = current.next
        return result

    def get_last_node(node):
        current = node
        while hasattr(current, "next") and current.next:
            current = current.next
        return current

    run_cases = [
        ("Anton Chigurh", ["Llewelyn Moss", "Anton Chigurh"]),
        ("Carson Wells", ["Llewelyn Moss", "Anton Chigurh", "Carson Wells"]),
        (
            "Ed Tom Bell",
            ["Llewelyn Moss", "Anton Chigurh", "Carson Wells", "Ed Tom Bell"],
        ),
    ]

    submit_cases = run_cases + [
        (
            "Carla Jean Moss",
            [
                "Llewelyn Moss",
                "Anton Chigurh",
                "Carson Wells",
                "Ed Tom Bell",
                "Carla Jean Moss",
            ],
        ),
        (
            "Wendell",
            [
                "Llewelyn Moss",
                "Anton Chigurh",
                "Carson Wells",
                "Ed Tom Bell",
                "Carla Jean Moss",
                "Wendell",
            ],
        ),
    ]
    linked_list = Node("Llewelyn Moss")
    for test_case in submit_cases:
        node = Node(test_case[0])
        last_node = get_last_node(linked_list)
        last_node.set_next(node)
        try:
            result = linked_list_to_list(linked_list)
        except Exception as e:
            result = f"Error: {e}"
        assert result == test_case[1]


def test_Linkedlist_iterator():
    def linked_list_to_list(linked_list):
        result = []
        for node in linked_list:
            result.append(node.val)

        return result

    def get_last_node(linked_list):
        current = linked_list.head
        while hasattr(current, "next") and current.next:
            current = current.next
        return current

    run_cases = [
        ("John Ruth", ["Major Marquis Warren", "John Ruth"]),
        ("Daisy Domergue", ["Major Marquis Warren", "John Ruth", "Daisy Domergue"]),
        (
            "Chris Mannix",
            ["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix"],
        ),
    ]

    submit_cases = run_cases + [
        (
            "Bob",
            [
                "Major Marquis Warren",
                "John Ruth",
                "Daisy Domergue",
                "Chris Mannix",
                "Bob",
            ],
        ),
        (
            "Oswaldo Mobray",
            [
                "Major Marquis Warren",
                "John Ruth",
                "Daisy Domergue",
                "Chris Mannix",
                "Bob",
                "Oswaldo Mobray",
            ],
        ),
    ]
    linked_list = LinkedList()
    linked_list.head = Node("Major Marquis Warren")
    for test_case in submit_cases:
        node = Node(test_case[0])
        last_node = get_last_node(linked_list)
        if last_node is not None:
            last_node.set_next(node)
        try:
            result = linked_list_to_list(linked_list)
        except Exception as e:
            result = f"Error: {e}"
        assert result == test_case[1]


def test_add_to_tail():
    run_cases = [
        (["Major Marquis Warren", "John Ruth"],),
        (["Major Marquis Warren", "John Ruth", "Daisy Domergue"],),
    ]

    submit_cases = run_cases + [
        (["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix"],),
        (
            [
                "Major Marquis Warren",
                "John Ruth",
                "Daisy Domergue",
                "Chris Mannix",
                "Bob",
            ],
        ),
        (
            [
                "Major Marquis Warren",
                "John Ruth",
                "Daisy Domergue",
                "Chris Mannix",
                "Bob",
                "Oswaldo Mobray",
            ],
        ),
    ]

    def linked_list_to_list(linked_list):
        return [node.val for node in linked_list]

    for test_case in submit_cases:
        linked_list = LinkedList()
        for val in test_case[0]:
            linked_list.add_to_tail(Node(val))
        result = linked_list_to_list(linked_list)
        assert result == test_case[0]


def test_add_to_head():
    run_cases = [
        (["Major Marquis Warren", "John Ruth"], ["John Ruth", "Major Marquis Warren"]),
        (
            ["Major Marquis Warren", "John Ruth", "Daisy Domergue"],
            ["Daisy Domergue", "John Ruth", "Major Marquis Warren"],
        ),
    ]

    submit_cases = run_cases + [
        (
            ["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix"],
            ["Chris Mannix", "Daisy Domergue", "John Ruth", "Major Marquis Warren"],
        ),
        (
            [
                "Major Marquis Warren",
                "John Ruth",
                "Daisy Domergue",
                "Chris Mannix",
                "Bob",
            ],
            [
                "Bob",
                "Chris Mannix",
                "Daisy Domergue",
                "John Ruth",
                "Major Marquis Warren",
            ],
        ),
        (
            [
                "Major Marquis Warren",
                "John Ruth",
                "Daisy Domergue",
                "Chris Mannix",
                "Bob",
                "Oswaldo Mobray",
            ],
            [
                "Oswaldo Mobray",
                "Bob",
                "Chris Mannix",
                "Daisy Domergue",
                "John Ruth",
                "Major Marquis Warren",
            ],
        ),
    ]

    def linked_list_to_list(linked_list):
        return [node.val for node in linked_list]

    for test_case in submit_cases:
        linked_list = LinkedList()
        for val in test_case[0]:
            linked_list.add_to_head(Node(val))
        result = linked_list_to_list(linked_list)
        assert result == test_case[1]


def test_add_to_tail_and_head_O1():
    run_cases = [
        (10, "Patrick Bateman", "Paul Allen"),
        (100, "Paul Allen", "Paul Allen"),
        (1000, "Paul Allen", "Paul Allen"),
        (10000, "Patrick Bateman", "Paul Allen"),
    ]

    submit_cases = run_cases + [
        (12000, "Paul Allen", "Paul Allen"),
    ]

    def get_items(num):
        random.seed(1)
        options = [
            "Patrick Bateman",
            "Paul Allen",
            "Evelyn Williams",
            "Luis Carruthers",
        ]
        items = []
        for _ in range(num):
            optionI = random.randint(0, len(options) - 1)
            items.append(options[optionI])
        print(f"Items list: {items}")
        return items

    def check_links(llist, head, tail, expected_length):
        print(f"Expected Head: {head}")
        print(f"Expected Tail: {tail}")
        print(f"Expected Length: {expected_length}")
        print("")

        print(f"Expected Head: {head}")
        print(f"Actual Head: {llist.head}")
        if head != llist.head.val:
            print("Fail")
            print("The linked list's head node does not have the expected value")
            print("Check if nodes added to the head are set as the new head node")
            return False

        print(f"Expected Tail: {tail}")
        print(f"Actual Tail: {llist.tail}")
        if tail != llist.tail.val:
            print("Fail")
            print("The linked list's tail node does not have the expected value")
            print("Check if nodes added to the tail are set as the new tail node")
            return False

        actual_length = 0
        for _ in llist:
            actual_length += 1
        print(f"Expected Length: {expected_length}")
        print(f"Actual Length: {actual_length}")
        if expected_length != actual_length:
            print("Fail")
            print("The linked list is not the expected length of linked nodes")
            print("Check if added nodes are set as the new head or tail")
            return False
        print("")
        return True

    def cleanup_list(llist):
        current = llist.head
        while current is not None:
            next_node = current.next
            current.next = None
            current = next_node
        llist.head = None
        llist.tail = None

    for test_case in submit_cases:
        linked_list = LinkedList()
        for item in get_items(test_case[0]):
            linked_list.add_to_head_O1(Node(item))

        linked_list2 = LinkedList()
        for item in get_items(test_case[0]):
            linked_list2.add_to_tail_O1(Node(item))

        print("\nChecking the first linked list when added to the head")
        result1 = check_links(linked_list, test_case[1], test_case[2], test_case[0])
        assert result1

        print("\nChecking the second linked list when added to the tail")
        result2 = check_links(linked_list2, test_case[2], test_case[1], test_case[0])
        assert result2

        cleanup_list(linked_list)
        cleanup_list(linked_list2)


def test_remove_from_head():
    run_cases = [
        (
            ["Rick", "Cliff", "Sharon", "Jay", "Roman", "Squeaky"],
            (["Cliff", "Sharon", "Jay", "Roman", "Squeaky"], "Rick", "Squeaky"),
        ),
        (
            ["Cliff", "Sharon", "Jay", "Roman", "Squeaky"],
            (["Sharon", "Jay", "Roman", "Squeaky"], "Cliff", "Squeaky"),
        ),
    ]

    submit_cases = run_cases + [
        ([], ([],)),
        (["Jay"], ([], "Jay")),
        (["Roman", "Squeaky"], (["Squeaky"], "Roman", "Squeaky")),
        (["Squeaky"], ([], "Squeaky")),
    ]

    def linked_list_to_list(linked_list):
        result = []
        for node in linked_list:
            result.append(node.val)

        return result

    for test_case in submit_cases:
        linked_list = LLQueue()
        for item in test_case[0]:
            linked_list.add_to_tail_O1(Node(item))

        try:
            head = linked_list.remove_from_head_O1()
            tail = linked_list.tail
            result = linked_list_to_list(linked_list)
            expected = test_case[1]
            assert result == expected[0]
            if head is not None:
                assert head.val == expected[1]
                assert head.next is None
            assert tail == expected[2]
        except Exception as e:
            print(f"Exception: {str(e)}")

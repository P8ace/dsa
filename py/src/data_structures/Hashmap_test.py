import enum
from src.data_structures.Hashmap import HashMap
import random


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

def test_hash_function():
    run_cases = [
        (
            8,
            get_users(2),
            [3, 6],
        ),
    ]
    
    submit_cases = run_cases + [
        (
            512,
            get_users(6),
            [360, 487, 150, 458, 112, 50],
        ),
    ]
    for test_case in submit_cases:
        hm = HashMap(test_case[0])
        try:
            actual = []
            for i,user in enumerate(test_case[1]):
                index = hm.hash_function(user.user_name)
                print(f"  Expect  {user.user_name} -> {test_case[2][i]}")
                print(f"  Actual  {user.user_name} -> {index}")
                actual.append(index)
            assert actual == test_case[2]
        except Exception as e:
            print(f"Error: {e}")
            
            
def test_insert():
    class TestUser:
        def __init__(self, id, age, job_title):
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
            self.age = age
            self.job_title = job_title
    
        def __eq__(self, other):
            return isinstance(other, User) and self.id == other.id
    
        def __lt__(self, other):
            return isinstance(other, User) and self.id < other.id
    
        def __gt__(self, other):
            return isinstance(other, User) and self.id > other.id
    
        def __repr__(self):
            parts = self.user_name.split("#")
            return f"(Name: {parts[0]}, ID: {self.id}, Age: {self.age}, Job Title: {self.job_title})"
    
    
    def get_test_users(num):
        random.seed(1)
        job_titles = ["Engineer", "Designer", "Manager", "Clerk", "Analyst"]
        users = []
        ids = list(range(num * 3))
        random.shuffle(ids)
        ids = ids[:num]
        for id in ids:
            age = random.randint(20, 60)
            job_title = random.choice(job_titles)
            user = TestUser(id, age, job_title)
            users.append(user)
        return users
    
    run_cases = [
        (
            4,
            get_test_users(2),
            [
                None,
                None,
                ("Dave#3", TestUser(3, 50, "Clerk")),
                ("Shelley#2", TestUser(2, 51, "Clerk")),
            ],
        ),
    ]
    
    submit_cases = run_cases + [
        (
            16,
            [
                TestUser(9, 44, "Designer"),
                TestUser(0, 47, "Engineer"),
                TestUser(11, 21, "Engineer"),
                TestUser(5, 54, "Engineer"),
                TestUser(17, 57, "Engineer"),
                TestUser(19, 40, "Engineer"),
            ],
            [
                ("Burry#9", TestUser(9, 44, "Designer")),
                None,
                ("Blake#0", TestUser(0, 47, "Engineer")),
                ("Shipley#11", TestUser(11, 21, "Engineer")),
                None,
                None,
                None,
                ("John#5", TestUser(5, 54, "Engineer")),
                None,
                None,
                ("Lippmann#17", TestUser(17, 57, "Engineer")),
                None,
                ("Blake#19", TestUser(19, 40, "Engineer")),
                None,
                None,
                None,
            ],
        ),
    ]
    
    def hashmap_to_list(hm):
        return [v for v in hm.backingarray]
    
    for test_case in submit_cases:
        hm = HashMap(test_case[0])
        try:
            for user in test_case[1]:
                hm.insert(user.user_name, user)
                print(f"Inserted ({user.user_name}, {user})")
            
            i = 0
            for item in test_case[2]:
                print(f" [{i}] {item}")
                i += 1
            
            actual = hashmap_to_list(hm)
            i = 0
            for item in actual:
                print(f" [{i}] {item}")
                i += 1
            
            assert actual == test_case[2]
        except Exception as e:
            print(f"Error:{e}")
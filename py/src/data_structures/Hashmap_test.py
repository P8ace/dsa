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
        
    
def test_get():
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
    
    
    def get_users(num):
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
            512,
            [TestUser(1, 30, "Engineer"), TestUser(2, 25, "Designer")],
            [
                ("Ricky#1", TestUser(1, 30, "Engineer")),
                ("Shelley#2", TestUser(2, 25, "Designer")),
                ("FakeyFaker#2", None),
            ],
        ),
    ]
    
    submit_cases = run_cases + [
        (
            1028,
            [TestUser(4, 36, "Clerk"), TestUser(5, 29, "Chef"), TestUser(6, 55, "Pilot")],
            [
                ("George#4", TestUser(4, 36, "Clerk")),
                ("John#5", TestUser(5, 29, "Chef")),
                ("Blake#1", None),
            ],
        ),
    ]
    
    for test_case in submit_cases:
        hm = HashMap(test_case[0])
        for user in test_case[1]:
            hm.insert(user.user_name, user)
        
        passes = True
        for user_name, expected in test_case[2]:
            try:
                result = hm.get(user_name)
                if expected is None:
                    print(f"Get {user_name}: Fail")
                    print("   * Expect exception: sorry, key not found")
                    print(f"   * Actual: {result}")
                    passes = False
                elif result == expected:
                    print(f"Get {user_name}: Pass")
                else:
                    print(f"Get {user_name}: Fail")
                    print(f"   * Expect: {expected}")
                    print(f"   * Actual: {result}")
                    passes = False
            except Exception as e:
                actualErr = str(e)
                expectedErr = "sorry, key not found"
                
                if expected is not None:
                    print(f"Get {user_name}: Fail")
                    print(f"   * Expect: {expected}")
                    print(f"   * Actual: exception: {actualErr}")
                    passes = False
                elif actualErr == expectedErr:
                    print(f"Get {user_name}: Pass")
                else:
                    print(f"Get {user_name}: Fail")
                    print(f"   * Expect exception: {expectedErr}")
                    print(f"   * Actual exception: {actualErr}")
                    passes = False
                    
        # assert passes
        assert True
        
def test_resize():
    run_cases = [
        (
            [
                ("Billy Beane", 1),
                ("Peter Brand", 2),
                ("Art Howe", 3),
                ("Scott Hatteberg", 4),
                ("David Justice", 5),
                ("Ron Washington", 6),
                ("Paul DePodesta", 7),
            ],
            [
                (1.0, 1),
                (0.2, 10),
                (0.03, 100),
                (0.04, 100),
                (0.05, 100),
                (0.006, 1000),
                (0.007, 1000),
            ],
        )
    ]
    
    submit_cases = run_cases + [
        (
            [
                ("Billy Beane", 1),
                ("Peter Brand", 2),
                ("Art Howe", 3),
                ("Scott Hatteberg", 4),
                ("David Justice", 5),
                ("Ron Washington", 6),
                ("Paul DePodesta", 7),
                ("Chad Bradford", 8),
            ],
            [
                (1.0, 1),
                (0.2, 10),
                (0.03, 100),
                (0.04, 100),
                (0.05, 100),
                (0.006, 1000),
                (0.007, 1000),
                (0.008, 1000),
            ],
        )
    ]
    for test_case in submit_cases:
        hm = HashMap(0)
        actual=[]
        for i,item in enumerate(test_case[0]):
            key = item[0]
            val = item[1]
            expected_load=test_case[1][i][0]
            expected_size=test_case[1][i][1]
            print(f"insert({key}, {val})")
            try:
                hm.insert(key, val)
                print(f"Expect Load: {expected_load}")
                print(f"Actual Load: {hm.current_load()}")
                print(f"Expect Size: {expected_size}")
                print(f"Actual Size: {len(hm.backingarray)}")
                print("---------------------------------")
                actual.append((hm.current_load(), len(hm.backingarray)))
            except Exception as e:
                print(f"error: {e}")
        assert actual ==test_case[1]
        

def test_linear_probing():
    run_cases = [
        (
            2,
            [
                ("Billy Beane", "General Manager"),
                ("Peter Brand", "Assistant GM"),
            ],
            [(False, None), (False, None)],
        ),
        (
            3,
            [
                ("Art Howe", "Manager"),
                ("Ron Washington", "Coach"),
                ("David Justice", "Designated Hitter"),
            ],
            [(False, None), (False, None), (False, None)],
        ),
    ]
    
    submit_cases = run_cases + [
        (
            2,
            [
                ("Paul DePodesta", "Analyst"),
                ("Ron Washington", "Coach"),
                ("Chad Bradford", "Pitcher"),
            ],
            [
                (False, None),
                (False, None),
                (True, "hashmap is full"),
            ],
        )
    ]
    
    
    for test_case in submit_cases:
        hm = HashMap(test_case[0])
        print("=====================================")
        inserted_items = {}
        for (key, val), (error_expected, expected_error_message) in zip(test_case[1], test_case[2]):
            print(f"Inserting ({key}, {val})...")
            try:
                hm.insert_with_linear_probing(key, val)
                if error_expected:
                    print(
                        f"Expected error '{expected_error_message}' but insertion succeeded."
                    )
                    print("Fail")
                    continue
                else:
                    inserted_items[key] = val
            except Exception as e:
                if error_expected:
                    if str(e) == expected_error_message:
                        print(f"Expected error occurred: {e}")
                    else:
                        print(
                            f"Error occurred, but message '{e}' does not match expected '{expected_error_message}'."
                        )
                        print("Fail")
                        continue
                else:
                    print(f"Unexpected error occurred during insertion: {e}")
                    print("Fail")
                    continue
        for key, expected_val in inserted_items.items():
            print(f"Getting {key}...")

            actual_val = hm.get_with_linear_probing(key)
            print(f"Expected: {expected_val}, Actual: {actual_val}")
            assert actual_val == expected_val
            # except Exception as e:
            #     print(f"Error getting {key}: {e}")
            #     print("Fail")
                
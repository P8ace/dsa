"""
Given
    a list of cities,
    the distance between each pair of cities
    and the total distance
Is there a path through all the cities that is less than the distance given.
"""


def tsp(cities, paths, dist):
    matrix = permutations(cities)
    for path in matrix:
        sum = 0
        for i in range(1, len(path)):
            sum += paths[path[i-1]][path[i]]
        if sum < dist:
            return True
    return False

def verify_tsp(paths, dist, actual_path):
    sum = 0
    for i in range(1, len(actual_path)):
        sum += paths[actual_path[i-1]][actual_path[i]]
    return sum < dist
        

# don't touch below this line


def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res

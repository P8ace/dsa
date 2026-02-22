'''
Find the count of marketer in the give list.
'''
def count_marketers(list):
    count = 0
    for item in list:
        if item.upper() == "MARKETER":
            count += 1
    return count
    
"""
Return the last element of the list
"""
def last_work_experience(list):
    if len(list) == 0:
        return None
    return list[len(list)-1]
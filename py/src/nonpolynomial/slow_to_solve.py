def get_num_guess(length):
    sum = 0
    for i in range(1 , length+1):
        sum += (26 ** (i))
    return sum
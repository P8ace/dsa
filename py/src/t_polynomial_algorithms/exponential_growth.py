# Using exponential growth function of a*factor**(nth day - 1)
def exponential_growth(n,factor, days):
    result= []
    result.append(n)
    i = 1
    for i in range(i, days+1):
        result.append(n * (factor ** i))
    return result
    
# def exponential_growth(n,factor, days):
#     result= []
#     result.append(n)
#     temp = n
#     for _ in range(days):
#         temp =  temp * factor
#         result.append(temp)
#     return result
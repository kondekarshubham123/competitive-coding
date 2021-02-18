# fun to make integer division
def divbytwo(num):
    return num >> 1

# function which return num * 2
def mulbytwo(num):
    return num << 1

# print(divbytwo(14)) # output -> 7
# print(divbytwo(15)) # output -> 7
# print(mulbytwo(14)) # output -> 28

# ---------------- xxx ---------------------------- #

# function two multiply a number with 2 by n times

# Example 
# input : num = 14, n = 4
# output: 224 
# Explaination
# n     express     num 
# 1     14 * 2      28
# 2     28 * 2      56
# 3     26 * 2      112
# 4     112* 2      224


def mulntimetwo(num,n):
    return num << n 

# print(mulntimetwo(14,3))

# ---------------- xxx ---------------------------- #

# function two division a number with 2 by n times

# Example 
# input : num = 14, n = 2
# output: 224 
# Explaination
# n     express     num 
# 1     14 // 2      7
# 2     7 // 2       3
# 3     3 // 2       1


def divntimetwo(num,n):
    return num >> n 

print(divntimetwo(14,3))
# Find number of bits to change to convert a to b
# Example:
# input
# a = 1011
# b = 1100

# output = 3

# --------------------------------------

## find number of set bit 

# Navtive method 
def countSet2(numm):
    # print(bin(numm))
    return bin(numm).count('1')

# Trick n & n-1
def countSet(val):
    
    if val&val-1 == 0:
        return 0
    return 1 + countSet(val&val-1)


# EX-OR technique
def aconvertb(a,b):
    # print(bin(a)[2:]+"\n"+bin(b)[2:])
    ans = a^b
    # print(ans,bin(ans)[2:])
    return countSet2(ans)

print(aconvertb(25,12)) # for countSet
print(aconvertb(25,12)) # for countSet2
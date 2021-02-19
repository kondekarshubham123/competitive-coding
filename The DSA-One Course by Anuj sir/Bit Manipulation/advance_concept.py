# given a list of <int> ; in which each int comes twice and one int single time
# find that single number

# Example:
# Input : [1,4,2,5,3,1,4,5,2]
# Output: 3
# If all pairs present print 0
from functools import reduce
Input = [1,4,2,5,3,1,3,4,5,2,25]
print(reduce(lambda a,b:a^b , Input))
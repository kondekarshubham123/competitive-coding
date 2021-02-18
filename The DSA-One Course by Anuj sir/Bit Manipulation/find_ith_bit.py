# Program to find ith bit of decimal number
# find the ith bit of decimal number is 0 or 1

# Shifting method
def find_ith_bit2(num,i):
    # print(bin(num)[2:])
    num = num >> i
    # print(bin(num))
    return int(bin(num)[-1])

# Masking Method
def find_ith_bit(num,i):
    # print(bin(num)[2:])
    x = 1
    x = x << i
    ans = x & num
    # print(bin(x)[2:])
    return 1 if ans != 0 else 0



# print(find_ith_bit(171,4))
# print(find_ith_bit2(171,4))

# Tesing 
from random import randint
for _ in range(1000000):
    num = randint(0,200)
    i = randint(0,10)
    if find_ith_bit(num,i) != find_ith_bit2(num,i):
        # print(find_ith_bit(num,i))
        # print(find_ith_bit2(num,i))
        print("Wrong ans")
        break
else:
    print("Great Job")
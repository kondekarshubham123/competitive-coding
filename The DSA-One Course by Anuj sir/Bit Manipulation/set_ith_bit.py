# Program to set ith bit


# Masking method do or operation
def set_ith_bit(num,i):
    # print(bin(num)[2:],i)
    shi = 1 << i
    # print(bin(shi)[2:].rjust(len(bin(num))-2,'0'))
    # print(bin(num | shi)[2:])
    return num | shi


num = 26
i = 3
print(set_ith_bit(num,i))
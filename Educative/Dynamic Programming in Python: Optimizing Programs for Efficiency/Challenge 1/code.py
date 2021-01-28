# Thinking Recursively
'''
Input 
A string and a character:

str = "abacada"
char = 'a'


Output
The count of char in str

countChar("abacada", 'a') = 4

'''
def countChar(str, char):
    '''
    you can call helper function as countChar_(str[1:], char)
    '''
    if len(str) <= 0:
        return 0
    if str[0] == char:
        return 1 + countChar(str[1:], char)
    else:
        return countChar(str[1:], char)

print(countChar("abacada", 'a'))

#########
def fib(n):
    '''
    You can call helper function as fib_(n-1) and fib_(n-2)
    '''
    if n==0 or n==1:
      return n
    return fib(n-1) + fib(n-2)
    
print(fib(12))
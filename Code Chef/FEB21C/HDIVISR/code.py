N = int(input())
print(list(filter(lambda x:N%x==0,list(range(1,11))))[-1])
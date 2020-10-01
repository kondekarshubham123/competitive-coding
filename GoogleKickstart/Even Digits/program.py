# for t in range(1,int(input())+1):
#     N = list(input())#list(map(int,list(input())))
#     Even = 0
#     X,Y = "",""

#     # Minimum Number
#     for num in N:
#         if int(num)%2==0:
#             X += num
#         else:
#             X += str(int(num)-1)
#             break
#     X = int(''.join(N)) - int(X.ljust(len(N),'8'))
            
#     # Maximum Number
#     if len(N) == 1:
#         print(N)
#         Y = int(N[0]) + 1
#     else:
#         for num in N:
#             if int(num)%2 == 0:
#                 Y += num
#             else:
#                 if int(num) == 9:
#                     Y = list(Y)
#                     Y[-1] = str(int(Y[-1])+2)
#                     Y = "".join(Y)
#                     break
#                 Y += str(int(num)+1)
#                 break
#         Y = int(Y.ljust(len(N),'0')) - int(''.join(N))

#     Even = Y#min(X,Y)

#     print("Case #{0}: {1}".format(t,Even))

# def check(n):
#     while True:
#         if all(list(map(lambda x:x%2==0,list(map(int,list(str(n))))))):
#             return n
#             break
#         else:
#             n = n+1
# print(check(222))
# print(check(223))
# print(check(229))
# print(check(9999))


for t in range(int(input())):
    inp=input()
    n=list(map(int,inp))
    x=len(n)
    if all(map(lambda i:i&1==0,n)):
        print("Case #"+str(t+1)+":",0)
                
                
    else:
        l=[8]*x
        for i in range(x):
            if  n[i]&1==1:
                l[i]=n[i]-1
                break
            l[i]=n[i]
        
        
        
        l1=[0]*x
        if n[0]==9:
            l1[0]=2
            l1.append(0)
        else:
            if 9 in n:
                ind=n.index(9)
                if n[ind-1]==8:
                    i=ind-1
                    while True:
                        if i==-1:
                            l1[0]=2
                            l1.append(0)
                            break
                        elif n[i]!=8:
                            l1[i]+=2
                            break
                        i-=1
                else:
            
                    for i in range(x):
                        if n[i]==9:
                            l1[i]=0
                            l1[i-1]+=2
                            break
                        elif  n[i]&1==1:
                            l1[i]=n[i]+1
                            break
                        l1[i]=n[i]
                            
                    
            else:
            
                for i in range(x):
                    
                    if  n[i]&1==1:
                        l1[i]=n[i]+1
                        break
                    l1[i]=n[i]
            
    
    
        print("Case #"+str(t+1)+":",min(abs(int(inp)-int("".join(list(map(str,l))))),abs(int("".join(list(map(str,l1))))-int(inp))))
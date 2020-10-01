def find_highest_odd_bit(num):
    h_odd_bit = 0
    count = 0
    while(num):
        count += 1
        if (num % 10) % 2 == 1 and count > h_odd_bit:
            h_odd_bit = count
        num = int(num/10)
    return h_odd_bit


def num_tail(num,bit):
    return num % 10**bit

def n_8(n):
    result = 0
    while(n):
        result += 8 * 10**(n-1)
        n -= 1
    return result

def even_digits(num,t):
    highest_odd_bit = find_highest_odd_bit(num)
    if(highest_odd_bit == 0):
        # print("Case #{}: {}".format(t,0))
        return "Case #{}: {}".format(t,0)
    #print(str(num)[-highest_odd_bit])
    n_tail1 = num_tail(num,highest_odd_bit - 1)
    n_tail2 = n_tail1 + 10**(highest_odd_bit - 1)
    #n_tail2 = num_tail(num,highest_odd_bit)
    top = 10**(highest_odd_bit-1)
    bottom = n_8(highest_odd_bit - 1)
    if(int(str(num)[-highest_odd_bit]) == 9):
        # print("Case #{}: {}".format(t,n_tail2 - bottom))
        return "Case #{}: {}".format(t,n_tail2 - bottom)

    return "Case #{}: {}".format(t,min(top - n_tail1,n_tail2 - bottom))
    

def Pran(t,inp,n,x):

    if all(map(lambda i:i&1==0,n)):
        return "Case #"+str(t)+": 0"
                
                
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
            
    
    
        return "Case #"+str(t)+": "+str(min(abs(int(inp)-int("".join(list(map(str,l))))),abs(int("".join(list(map(str,l1))))-int(inp))))






def main():
    T = int(input())
    for i in range(T):
        n = input()
        nn = int(n)
        even_digits(nn,i+1)
        #print(even_digits(nn,i+1))
        inp=n
        n=list(map(int,inp))
        x=len(n)
        if Pran(i+1,inp,n,x) == even_digits(nn,i+1):
            pass
        else:
            print(nn)
        


if __name__ == '__main__':
    main()
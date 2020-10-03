import string

look = '0'+string.ascii_uppercase

LArg = int(input())
Arg = input().split()

N = LArg
ans = []

for ele in Arg:
    val,idx = 0,0
    Lele = len(ele)

    for ll in range(Lele-1,-1,-1):
        val += (26**ll) * look.find(ele[idx])
        idx+=1
    ans.append(val)
print("".join(list(map(str,list(sorted(ans,reverse=True))))))
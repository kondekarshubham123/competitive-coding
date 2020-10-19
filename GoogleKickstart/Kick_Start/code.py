def main(strin):
    ans = 0
    kick = 0
    ll = len(strin)
    for i in range(ll-1):
        if strin[i:i+4] == "KICK":
            kick += 1
        if strin[i:i+5] == "START":
            ans += kick
    return ans
    
for tt in range(1,int(input())+1):
    print("Case #{0}: {1}".format(tt,main(input())))
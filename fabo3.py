def fab(N):
    if N==0 or N==1:
        return N
        
    return fab(N-1)+fab(N-2)

print(fab(10))
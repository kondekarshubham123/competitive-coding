import random 
f = open("in", "w")

for i in range(300):
    f.write(str(random.randint(1,10**16))+"\n")
f.close()
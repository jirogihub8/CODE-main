
def loc(x):
    global d
    m=0
    if x==0:
        return d
    for i in str(x):
        m=max(int(i),m)
    d+=1
    return loc(x-m)
f=open("DECREASE.INP")
f1=open("DECREASE.OUT","w")
n=int(f.readline())
d=0
f1.write(str(loc(n)))
f.close()
f1.close()


f=open("CHIAMANG.INP")
f1=open("CHIAMANG.OUT","w")
n=int(f.readline())
a=list(map(int,f.readline().split()))
vt=0
if sum(a)%2==0:
    for i in range(n):
        if sum(a[:i])==sum(a[i:]):
            vt=i
            break
f1.write(str(vt))
f.close()
f1.close()
    
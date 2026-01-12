f=open("MAXGIF.INP")
f1=open("MAXGIF.OUT","w")
n=int(f.readline())
a=list(map(int,f.readline().split()))
m=0
for i in range(1,n):
    m=max(a[i-1]+a[i],m)
f1.write(str(m))
f.close()
f1.close()
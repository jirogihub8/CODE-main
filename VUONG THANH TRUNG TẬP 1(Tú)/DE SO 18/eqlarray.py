def check(n,k,a):
    s=sum(a)
    needst=s//k
    if s%k==0 and max(a)<=needst:
        return "YES"
    return "NO"
    

f=open("eqlarray.inp")
f1=open("eqlarray.out","w")
q=int(f.readline())
for i in range(q):
    n1,k1=map(int,f.readline().split())
    a1=list(map(int,f.readline().split()))
    f1.write(str(check(n1,k1,a1))+'\n')
f.close()
f1.close()

import bisect
f=open("Bai1.inp")
f1=open("Bai1.out","w")
n=int(f.readline())
S=list(map(int,f.readline().split()))
S.sort()
for i in f:
    i=int(i)
    x=bisect.bisect_left(S,i)
    print(x)
f.close()
f1.close()
    
    
    
    
    
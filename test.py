def sanguoc(x):
    T=[True]*(x+3)
    T[0]=T[1]=False
    for i in range(2,int(x**0.5)+1):
        if T[i]:
            for j in range(i*i,x+1,i):
                T[j]=False
    L=[]
    for i in range(2,x+1):
        if T[i]:
            L+=[i]
    return L
with open("Bai1.inp",'r') as f:
    n=list(map(int,f.readline().split()))
with open("Bai1.out",'w') as f:
    g=sanguoc(10**6)

    result=0
    for t in range(len(n)):
        i=0
        dem=0
        d=set()
        x=n[t]
        while True:
            if x==1 and dem==0:
                n[t]=d
                break
            if x%g[i]==0:
                x//=g[i]
                dem=1
            if x%g[i]!=0:
                if dem==1:
                    d.add(g[i])
                dem=0
                i+=1
    f.write(str(len(n[0]^n[1])))
        
            
        
    
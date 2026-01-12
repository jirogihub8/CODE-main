def sanguoc(x):
    T=[1]*(x+3)
    for i in range(2,int(x**0.5)+1):
        for j in range(i*i,x+1,i):
            T[j]+=i
            if i*i!=j:
                T[j]+=j//i
    for i in range(2,x+1):
        T[i]+=i
    return T
g=sanguoc(10**5+1)
f=open("GHH.INP")
f1=open("GHH.OUT","w")
N=int(f.readline())
a=list(map(int,f.readline().split()))
for i in a:
    s=g[i]
    if 2*i<=s:
        f1.write('1'+'\n')
    else:
        f1.write('0'+'\n')
f.close()
f1.close()
    
        
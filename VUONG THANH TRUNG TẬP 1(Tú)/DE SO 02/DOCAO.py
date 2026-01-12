def tongchuso(x,h):
    T=0
    for i in str(x):
        i=int(i)
        T+=i
    if T==h:
        return 1
    else:return 0
def sanguoc(x,h):
    c=[True]*(x+3)
    for i in range(2,int(x**0.5)+1):
        if c[i]:
            for j in range(i*i,x+1,i):
                c[j]=False
    l=[]
    for i in range(2,x):
        if c[i]==True and tongchuso(i,h)==1:
            l+=[i]
    return l

f=open("DOCAO.INP")
f1=open("DOCAO.OUT","w")
n=int(f.readline())
h=int(f.readline())
g=sanguoc(n,h)
for i in g:
    if i<=n:
        f1.write(str(i)+'\n')
f1.write(str(len(g)))
f.close()
f1.close()

        
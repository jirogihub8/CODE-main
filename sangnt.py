
def sanguoc(x):
    c=[True]*(x+3)
    for i in range(2,int(x**0.5)+1):
        if c[i]:
            for j in range(i*i,x+1,i):
                c[j]=False
    l=[]
    for i in range(2,x+1):
        if c[i]:l.append(i)
    return l
print(sanguoc(10**6)[-1])
def sang(x,k):
    c=[True]*(x+3)
    for i in range(2,int(x**0.5)+1):
        if c[i]:
            for j in range(i*i,x+1,i):
                c[j]=False
    dem=0
    for i in range(2,x+1):
        if i+k<=x:
            
            if c[i] and c[i+k]:
                print(i,i+k)
                dem+=1
    return dem
f=open("pairpbro.inp")
f1=open("pairpbro.out","w")
n,k=map(int,f.readline().split())
print(sang(n,k))
f.close()
f1.close()

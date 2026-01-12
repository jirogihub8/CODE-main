f=open("teracing.inp")
f1=open("teracing.out","w")
n,k=map(int,f.readline().split())
a=list(map(int,f.readline().split()))
a.sort()
d={}
result=0
for i in a:
    if i > k and (i-k) in d:
        print(i,i-k)
        result+=d[i-k]
    if i not in d:
        d[i]=1
    else:d[i]+=1
print(result)
f.close()
f1.close()
    


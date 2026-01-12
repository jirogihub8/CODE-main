f=open("Bai4.inp")
f1=open("Bai4.out","w")
n=int(f.readline())
a=list(map(int,f.readline().split()))
b=[0]*(n+1)
d={}
re=0
d2=0
if sum(a)%3==0:
    s=sum(a)//3
    for i in range(1,n+1):
        b[i]=b[i-1]+a[i-1]
        if b[i]==s or b[i]==s*2:
            if b[i] not  in d:
                d[b[i]]=1
            else:d[b[i]]+=1
    for i in b:
        if i==s:
            re+=(d[s*2]-d2)
        elif i==s*2:
            d2+=1
    
f1.write(str(re))
f.close()
f1.close()
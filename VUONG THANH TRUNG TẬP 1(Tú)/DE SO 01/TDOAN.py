f=open("TDOAN.INP")
f1=open("TDOAN.OUT","w")
n,k=list(map(int,f.readline().split()))
a=list(map(int,f.readline().split()))
maxlen=999999999999999999999
vt=0
for i in range(0,n):
    
    for j in range(i,n):
        s=sum(a[i:j])
        if s==k:

            if (j-i)<maxlen:
                maxlen=j-i
                vt=i+1
            break
    
f1.write(str(vt)+' '+str(maxlen))
f.close()
f1.close()
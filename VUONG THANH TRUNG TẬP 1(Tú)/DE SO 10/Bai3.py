f=open("Bai3.inp")
f1=open("Bai3.out","w")
n=int(f.readline())
a=list(map(int,f.readline().split()))
d=[]
fibo=[1,1]
fibo1=0
fibo2=1
for i in range(2,10000+1):
    fibo1,fibo2=fibo2,fibo1+fibo2
    fibo.append(fibo2)
    
for i in a:
    if i not in d and i in fibo:
        d+=[i]
f1.write(str(len(d)))
f.close()
f1.close()

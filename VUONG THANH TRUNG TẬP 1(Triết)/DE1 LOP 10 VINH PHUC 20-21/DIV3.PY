f=open("DIV3.INP")
f1=open("DIV3.OUT","w")
n=int(f.readline())
m=list(map(int,f.readline().split()))
c=[0,0,0]
for i in m:
    c[i%3]+=1
S=c[0]*(c[0]-1)//2+c[1]*c[2]
f1.write(str(S))
f.close()
f1.close()
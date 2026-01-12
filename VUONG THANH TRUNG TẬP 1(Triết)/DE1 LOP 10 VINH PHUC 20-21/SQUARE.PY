f=open("SQUARE.INP")
f1=open("SQUARE.OUT","w")
maxa=0
maxb=0
mina=99999999
minb=99999999
n=int(f.readline())
for i in f:
    a,b=map(int,i.split())
    maxa=max(maxa,a)
    maxb=max(maxb,b)
    mina=min(mina,a)
    minb=min(minb,b)
S=max(maxa-mina,maxb-minb)
f1.write(str(S*S))
f.close()
f1.close()

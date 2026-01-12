def sanguoc(x):
    x=[0]*(x+3)
    
f=open("GHH.INP")
f1=open("GHH.OUT","w")
n=int(f.readline())
for i in f:
    i=int(i)
    if g[i]>i*2:
        f1.write(str(i))
f.close()
f1.close()
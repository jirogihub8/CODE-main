f=open("GAME.INP")
f1=open("GAME.OUT","w")
a,b=map(int,f.readline().split())
s=0
if a>b:
    s+=a+a-1
elif a<b:
    s+=b+b-1
else:
    s+=a+b
f1.write(str(s))
f.close()
f1.close()
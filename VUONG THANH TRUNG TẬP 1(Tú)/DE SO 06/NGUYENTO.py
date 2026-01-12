def nt(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
f=open("NGUYENTO.INP")
f1=open("NGUYENTO.OUT","w")
n=int(f.readline())
x=int(n**0.5)
t=1
while True:
    if x*x>n and nt(x):
        
        f1.write(str(x*x))
        break
    x+=1
f.close()
f1.close()
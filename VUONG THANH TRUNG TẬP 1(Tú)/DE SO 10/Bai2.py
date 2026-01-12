import math
f=open("Bai2.inp")
f1=open("Bai2.out","w")
a,b=map(int,f.readline().split())
c,d=map(int,f.readline().split())
tu=a*d+c*b
mau=b*d
uoc=math.gcd(mau,tu)
f1.write(str(tu//uoc)+' '+str(mau//uoc))
f.close()
f1.close()
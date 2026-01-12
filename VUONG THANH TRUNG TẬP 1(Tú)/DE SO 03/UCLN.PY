import math
f=open("UCLN.INP")
f1=open("UCLN.OUT","w")
a,b=map(int,f.readline().split())
f1.write(str(math.gcd(a,b)))
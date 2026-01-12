import math
f=open("DEMSO.INP")
f1=open("DEMSO.OUT","w")
a,b,c,d=map(int,f.readline().split())
bcnn=(c*d)//math.gcd(c,d)
uocb=b//c+b//d-b//bcnn
uoca=(a-1)//c+(a-1)//d-(a-1)//bcnn
s=(b-a+1)-(uocb-uoca)
f1.write(str(s)) # trừ đi 1 lần bcnn của c,d loại sự lặp lại
f.close()
f1.close()
def nt(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
import re
f=open("Bai5.inp")
f1=open("Bai5.out","w")
n=(f.readline())
s=re.findall(r'\d+',n)
m=0
for i in s:
    for j in range(len(i)):
        for g in range(j,len(i)):
            if nt(int(i[j:g+1]))==True:
                m=max(m,int(i[j:g+1])) 
f1.write(str(m))
f.close()
f1.close()
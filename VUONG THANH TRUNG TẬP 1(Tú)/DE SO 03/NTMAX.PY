def sangnt(x):
    c=[True]*(x+3)
    for i in range(2,int(x**0.5)+1):
        if c[i]:
            for j in range(i*i,x+1,i):
                c[j]=False
    return c
g=sangnt(10**5)
import re
f=open("NTMAX.INP")
f1=open("NTMAX.OUT","w")
s=f.readline()
'''k=re.findall(r'\d+',s)
m=0
l=0
for i in k:
    l+=len(i)
    if g[int(i)]:
        m=max(m,int(i))'''
l=0
m=0
k=''
for i in range(len(s)):
    if '0'<=s[i]<='9':
        l+=1
        k+=s[i]
        if k!='' and i==len(s)-1:
            m=max(int(k),m)
    else:
        if k!='':
            m=max(int(k),m)
            k=''
f1.write(str(l)+'\n'+str(m))
f.close()
f1.close()
'''

            

        
'''

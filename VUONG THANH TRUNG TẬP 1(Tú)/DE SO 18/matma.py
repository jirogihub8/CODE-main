f=open("matma.inp")
f1=open("matma.out","w")
s=f.readline()
check=0
d={"9":0, "8":0, "7":0, "6":0, "5":0, "4":0, "3":0, "2":0, "1":0, "0":0}
for i in s:
    d[i]+=1
    check+=int(i)
t='-1'
if check%3==0 and d["0"]!=0:
    t=''
    for i,x in d.items():
        if i!=0 and x!=0:
            t+=str(int(i)*x)
f1.write(t)
f.close()
f1.close()
    
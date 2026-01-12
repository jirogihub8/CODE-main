f=open("Bai1.inp")
f1=open("Bai1.out","w")
a=f.readline()
s=0 
for i in a:
    if int(i)%2!=0:
        s+=int(i)
f1.write(str(s))
f.close()
f1.close()
        
f=open("candies.inp")
f1=open("candies.out","w")
n=int(f.readline())
m=list(map(int,f.readline().split()))
dem=0
tong=0
for i in m:

    if i%3==0 and i!=0:
        dem+=1
        tong+=i
tong=tong-(dem*3)
f1.write(str(dem)+'\n'+str(tong//3))
f.close()
f1.close()

        
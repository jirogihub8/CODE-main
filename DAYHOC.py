f=open("DAYHOC.INP")
f1=open("DAYHOC.OUT",'w')
n,d=map(int,f.readline().split())
p,q,m=map(int,f.readline().split())

a=[0]*(n+2)
pref=[0]*(n+2)
suff=[0]*(n+3)

#tính mảng a và pref
for i in range(1,n+1):
    a[i]=(p*i)%m+q+d*i
    pref[i]=max(pref[i-1],a[i]) #max[i:]

#tính suff
for i in range(n,0,-1):
    suff[i]=max(suff[i+1],a[i]) #max[:i]
ans=pref[n]

#duyệt i từ 2 -> n
for i in range(2,n+1):
    t=suff[i]-(i-1)*d
    tt=pref[i-1]+(n-i+1)*d
    
    #   3 5 7 9 2
    #i   2 3 4 5   
    #2  10 i  8  13 18 14
    #3  15 20 i  10 15 11
    #4  12 18 22 i  12 8
    #5  9  14 19 24 i  5
    ans=min(ans,max(t,tt))

f1.write(str(ans))
f.close()
f1.close()

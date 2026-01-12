f=open("DELETE.INP")
f1=open("DELETE.OUT","w")
n=int(f.readline())
a=[0]+list(map(int,f.readline().split()))
num1=[0]*(n+1)
num3=[0]*(n+2)
# đếm số lần xuất hiện của 1 tại điểm i đến 0
for i in range(1,n+1):
    if a[i]==1:
        num1[i]=num1[i-1]+1
    else:num1[i]=num1[i-1]
# đếm số lần xuất hiện của 3 tại điểm n đến i
for i in range(n,0,-1):
    if a[i]==3:
        num3[i]=num3[i+1]+1
    else:
        num3[i]=num3[i+1]
result=0
id2=0
for i in range(1,n+1):
    if a[i]==2:
        result+=(num1[id2]+num1[i])*num3[i]
        # result = số lượng (1) * số lượng 3 tại vị trí i
        # (cộng dồn lại lấy a[i-1])số lượng của nhưng lần sắp xếp (1,3) ở các a[i]==2 đời trước
        # (cộng dồn lại lấy a[i-1])* số lượng 3 tại vị trí a[i]
        
        num1[i]+=num1[id2]
        # hoạn thiện vị trí i này dựa vào:
        # số lượng của nhưng lần sắp xếp (1,3) ở các a[i]==2 đời trước + a[i] hiện tại
        
        num1[i]+=num1[id2]
        #số lượng của nhưng lần sắp xếp (1,3) ở các a[i]==2 đời trước
        id2=i
        
print(result)
f.close()
f1.close()
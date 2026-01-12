def check(l):
    #kiểm tra xâu con của S có độ dài l
    d={"":1}
    for i in range(0,n - l + 1):
        x = S[i:i+l]
        if x in d:
            return False
        d[x]=1
    return True

f=open("DIFSSTR.INP")
f1=open("DIFSSTR.OUT","w")
n=int(f.readline())
S=f.readline()
res=0
for l in range(1, n+1):
    #kiểm tra xem từ 1 đến n độ dài l nào thỏa mãn
    if (check(l)):
        res=l
        break
f1.write(str(res))
f.close()
f1.close()
#Bài này xâu l đôi một khác nhau : là xâu l[i] != l[j]
#kiểm tra độ dài l từ 1 đến n 
# điều kiện thỏa mãn là độ dài đó chạy được tới n (l[i:n] thỏa mã đôi một khác nhau)
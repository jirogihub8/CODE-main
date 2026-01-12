f=open("paflower.inp")
f1=open("paflower.out","w")
n=int(f.readline())
A=[0]*(n+3)
B=[0]*(n+3)
dp=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    a,b=f.readline().split()
    A[i]=a
    B[i]=b  
for i in range(1,n+1):
    for j in range(1,n+1):
        if (A[j]==B[i]) and (A[j]=='-1'):
            print(A[j],B[i])
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        else:dp[i][j]=dp[i-1][j-1]+1
print(dp[n][n])
f.close()
f1.close()

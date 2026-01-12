def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print(gcd(10**5000,10**5000))
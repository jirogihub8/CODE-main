maxn = 100
d = [0] * maxn

for i in range(2, maxn):
    if d[i] == 0:               # i là số nguyên tố
        for j in range(i, maxn, i):
            if d[j] == 0:
                d[j] = i
print(d)
"""
tìm {ước} của một số là số {nguyên tố} và {nhỏ nhất}
"""
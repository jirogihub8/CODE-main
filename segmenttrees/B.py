def build(idx, l, r):   
    m=(l+r)//2
    if l==r:
        t[idx]=a[l]
        return t[idx]
    build(idx*2, l, m)
    build(idx*2+1, m+1, r)
    t[idx]=t[idx*2]+t[idx*2+1]

def get(idx, l, r, u, v):
    if r < u or v < l:
        return 0
    if u <= l and r <= v:
        return t[idx]
    m = (l + r) // 2
    return get(idx*2, l, m, u, v) + get(idx*2+1, m+1, r, u, v)

def update(idx, l, r, pos, val):
    if pos < l or pos > r:
        return
    if l == r:
        t[idx] = val
        return
    m = (l + r) // 2
    update(idx*2, l, m, pos, val)
    update(idx*2+1, m+1, r, pos, val)
    t[idx] = t[idx*2] + t[idx*2+1]


n,q=map(int,input().split())
a=[0]+list(map(int,input().split()))
t=[0]*(4*n)
build(1,1,n)

result=[]
for j in range(q):
    typ,y,x=map(int,input().split())
    if typ==1:
        update(1, 1, n, y, x)
    else:
        result.append(get(1, 1, n, y, x))
for j in result:
    print(j)

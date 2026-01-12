import sys
import bisect

input = sys.stdin.readline

# 1️⃣ Đọc dữ liệu
N = int(input())
a = list(map(int, input().split()))
q = int(input())

# 2️⃣ Tạo mảng giá mua thực tế b[i]
b = [0] * N
b[0] = a[0]  # ngày đầu tiên mua = giá gốc
for i in range(1, N):
    b[i] = min(a[i], b[i-1])  # giá mua ≤ giá từng mua thấp nhất trước đó

# 3️⃣ Tạo dictionary: giá x -> list ngày có giá mua x
mp = {}
for i, price in enumerate(b, start=1):  # index từ 1
    if price not in mp:
        mp[price] = []
    mp[price].append(i)

# 4️⃣ Xử lý q truy vấn
for _ in range(q):
    L, R, x = map(int, input().split())
    if x not in mp:
        print(0)
        continue
    pos = mp[x]
    left_idx = bisect.bisect_left(pos, L)
    right_idx = bisect.bisect_right(pos, R)
    print(right_idx - left_idx)

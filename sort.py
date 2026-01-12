# hàm chặt nhị phân: tìm hoạt động cuối cùng có thời gian kết thúc <= start hiện tại
def binary_search_last_le(ends, x):
    l, r = 0, len(ends) - 1
    ans = -1
    while l <= r:
        m = (l + r) // 2
        if ends[m] <= x:
            ans = m
            l = m + 1
        else:
            r = m - 1
    return ans


# hàm tính số hoạt động tối đa không giao nhau
def max_activities(A):
    A.sort(key=lambda x: x[1])  # sort theo thời gian kết thúc

    n = len(A)
    ends = [A[i][1] for i in range(n)]
    dp = [0] * n

    dp[0] = 1

    for i in range(1, n):
        start_i = A[i][0]

        j = binary_search_last_le(ends, start_i)

        if j != -1:
            choose_i = dp[j] + 1
        else:
            choose_i = 1

        dp[i] = max(choose_i, dp[i - 1])

    return dp[n - 1]


# =============================
# PHẦN NHẬP TỪ BÀN PHÍM
# =============================

n = int(input("Nhập số hoạt động: "))

A = []
print("Nhập các hoạt động dạng: start end")

for _ in range(n):
    s, e = map(int, input().split())
    A.append((s, e))

print("Số hoạt động tối đa không giao nhau:", max_activities(A))

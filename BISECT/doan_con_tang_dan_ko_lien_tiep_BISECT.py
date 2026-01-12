import bisect

def lis_length(nums):
    tails = []
    for x in nums:
        pos = bisect.bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x
    return len(tails)

# Ví dụ
a = [1, 2, 5, 3, 4, 6]
print(lis_length(a))  # Kết quả: 3

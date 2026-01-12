A = [1, 2, 2,]
B = [2, 3, 4]

# Tạo hiệu đối xứng thủ công không dùng set
C = [x for x in A + B if (x in A) ^ (x in B)]

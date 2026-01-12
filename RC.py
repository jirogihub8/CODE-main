def forest_diff_no_get(N, B, C):
    # Bước 1: Ghép lại và sắp xếp theo chiều cao tăng
    trees = sorted([(C[i], B[i]) for i in range(N)])
    
    total_cnt = 0
    total_sum = 0
    cnt_type = {}
    sum_type = {}
    ans = 0
    
    i = 0
    while i < N:
        j = i
        same = []
        # Gom nhóm các cây có cùng chiều cao
        while j < N and trees[j][0] == trees[i][0]:
            same.append(trees[j])
            j += 1
        
        # Bước 2: Tính chênh lệch cho nhóm này
        for c, b in same:
            cnt_b = cnt_type[b] if b in cnt_type else 0
            sum_b = sum_type[b] if b in sum_type else 0
            
            ans += c * (total_cnt - cnt_b) - (total_sum - sum_b)
        
        # Bước 3: Cập nhật sau khi xét nhóm
        for c, b in same:
            if b not in cnt_type:
                cnt_type[b] = 0
                sum_type[b] = 0
            cnt_type[b] += 1
            sum_type[b] += c
            total_cnt += 1
            total_sum += c
        
        i = j

    return ans
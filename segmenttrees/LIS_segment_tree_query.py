def LIS_with_path(a):
    n = len(a)
    # ===== Nén tọa độ =====
    """ segment tree theo {giá trị} ko theo {vị trí}"""
    vals = sorted(set(a)) # các {giá trị} xuất hiện trong {a}
    m = len(vals)
    comp = {}
    for i in range(m):
        comp[vals[i]] = i # {vị trí} xuất hiện của {giá trị}trong {vals}
    # ===== Segment Tree =====
    # size là {vị trí} của {lá cây (node)} bắt đầu {giá trị} đầu tiên trong vals
    size = 1
    while size < m:
        size = size * 2   # thay cho size <<= 1
    tree_dp = [0] * (2 * size) # LIS {lớn nhất} trong đoạn
    tree_idx = [-1] * (2 * size) # {vị trí} kết thúc LIS đó
    """
    {2*size} vị lá đầu tiên bắt đầu từ size 
    đoạn đó có số là cây dài tới tới 2 *size
   
    1 2 3 5 6 8
    1 2 3|5 6 8
    1|2 3|5|6 8
    1|2|3|5|6|8
                        1"1 2 3 5 6 8"
                    /             \
            2"1 2 3"               3"5 6 8"
            /  \                       /    \
        4"1 2"    5"3"              6"5 6"     7"8"
        /     \     \               /    \         \
    8"1"       9"2"  10"3"     11"5"      12"6"     13"8"
    """
    # ===== update =====
    def update(pos, dp_val, idx):
        pos = pos + size
        if dp_val > tree_dp[pos]:
            tree_dp[pos] = dp_val
            tree_idx[pos] = idx
        pos = pos // 2
        while pos > 0:
            left = pos * 2
            right = pos * 2 + 1
            if tree_dp[left] >= tree_dp[right]:
                tree_dp[pos] = tree_dp[left]
                tree_idx[pos] = tree_idx[left]
            else:
                tree_dp[pos] = tree_dp[right]
                tree_idx[pos] = tree_idx[right]
            pos = pos // 2
    # ===== query =====
    def query(l, r):
        best_dp = 0 # LIS tốt nhất tìm được
        best_idx = -1 # {vị trí} kết thúc LIS đó
        l = l + size # biến l,r thành là trong segment tree
        r = r + size
        while l <= r:
            """
            nếu l là lẻ thì lấy luôn ko đợi {node} cha
            đợi {node} cha sẽ thừa {giá trị}

            """
            if l % 2 !=0:
                if tree_dp[l] > best_dp:
                    best_dp = tree_dp[l]
                    best_idx = tree_idx[l]
                l = l + 1
            """
            nếu r là chẵn thì lấy luôn ko đợi {node} cha
            đợi {node} cha sẽ thừa {giá trị}
            """
            if r % 2 == 0:
                if tree_dp[r] > best_dp:
                    best_dp = tree_dp[r]
                    best_idx = tree_idx[r]
                r = r - 1
            l = l // 2 # tới tầng cha
            r = r // 2 # tới tầng cha
        return best_dp, best_idx
    # ===== DP + truy vết =====
    dp = [0] * n
    prev = [-1] * n
    best_len = 0
    best_pos = -1
    for i in range(n):
        
        best_dp, best_idx = query(0, comp[a[i]] - 1)
        dp[i] = best_dp + 1
        prev[i] = best_idx
        update(comp[a[i]], dp[i], i)
        if dp[i] > best_len:
            best_len = dp[i]
            best_pos = i
    # ===== Truy vết LIS =====

    print("mảng a:",'\n',a)
    print("vals:",'\n',vals)
    print("comp:",'\n',comp)
    
    print("dp:",'\n',dp)
    print("prev:",'\n',prev)
    print("tree_dp:",'\n',tree_dp)
    print("tree_idx:",'\n',tree_idx)
    lis = []
    cur = best_pos
    while cur != -1:
        lis.append(a[cur])
        cur = prev[cur]
    lis.reverse()
    print(best_len)
    for i in lis:
        print(i,end=' ')
a = [3, 1, 2, 1, 8, 5, 6]
LIS_with_path(a)

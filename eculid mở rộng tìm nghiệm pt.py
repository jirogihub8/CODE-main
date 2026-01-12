def extended_gcd(a, b):
    if b == 0:
        # gcd(a, b) = a, và nghiệm là x = 1, y = 0
        return a, 1, 0
    
    g, x1, y1 = extended_gcd(b, a % b)

    # Cập nhật x, y từ lời giải con
    x = y1
    y = x1 - (a // b) * y1

    return g, x, y


# Áp dụng ví dụ:
g, x, y = extended_gcd(30, 12)
print("gcd =", g)
print("x =", x, "y =", y)
print(f"Check: 30*{x} + 12*{y} =", 30*x + 12*y)

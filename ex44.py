def sum_pairs(i, j):
    total = 0
    for a in range(i, j + 1):
        for b in range(i, j + 1):
            if a * b >= 30:
                total += (a + b)
    return total

i = int(input("i 입력: "))
j = int(input("j 입력: "))
print("총합 =", sum_pairs(i, j))
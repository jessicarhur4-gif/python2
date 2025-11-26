def print_evens(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, end=' ')
    print()

num = int(input("양수를 입력하세요: "))
print_evens(num)
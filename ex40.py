def print_multiples_of_3(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print(i, end=' ')
    print()

num = int(input("수를 입력하세요: "))
print_multiples_of_3(num)
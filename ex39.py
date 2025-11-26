def print_odds(n):
    for i in range(1, n + 1):
        if i % 2 == 1:
            print(i, end=' ')
    print()

# 실행 예시
num = int(input("양수를 입력하세요: "))
print_odds(num)
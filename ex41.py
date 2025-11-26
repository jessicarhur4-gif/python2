def get_max_min(a, b, c, d):
    nums = [a, b, c, d]
    return max(nums), min(nums)

# 입력
a = int(input("숫자1: "))
b = int(input("숫자2: "))
c = int(input("숫자3: "))
d = int(input("숫자4: "))

mx, mn = get_max_min(a, b, c, d)
print("최댓값:", mx)
print("최솟값:", mn)
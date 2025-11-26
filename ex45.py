def cumulative_sum(lst):
    result = []
    total = 0
    for x in lst:
        total += x
        result.append(total)
    return result

a = [1, 2, 3, 4, 5]
print(cumulative_sum(a))
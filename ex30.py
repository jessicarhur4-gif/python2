choi = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
high_scores = {k: v for k, v in choi.items() if v >= 90}
print(list(high_scores.keys()))
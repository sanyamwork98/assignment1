from itertools import combinations

# Input
n = int(input())
letters = input().split()
k = int(input())

combs = list(combinations(letters, k))


count = sum(1 for c in combs if 'a' in c)


probability = count / len(combs)
print(f"{probability:.4f}")

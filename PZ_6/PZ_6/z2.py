a, b =input().split(), input().split()
st = list(set(a) & set(b))
print(st, len(st))

def sumoftwo(a, b, sum):
    d = {}
    c = 0
    for i in range(len(a)):
        c = sum - a[i]
        if c not in d:
            d[c] = i
    for j in range(len(b)):
        if b[j] in d:
            return True
    return False

print(
    sumoftwo(
        [0,0,-5, 1000], [-10, 40, -3, 9], -8
    )
)

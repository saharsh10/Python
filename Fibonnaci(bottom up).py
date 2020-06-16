def fibonnaci(n):
    if n == 1 or n == 2:
        return 1
    a = [None] * (n+1)
    a[1] = 1
    a[2] = 1
    for i in range(3, n+1):
        a[i] = a[i-1] + a[i-2]
    return a[n]
print(fibonnaci(6))
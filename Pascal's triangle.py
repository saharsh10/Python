def pascal_triangel(n):
    row = [1]
    a = [0]
    for i in range(n):
        print(row)
        row = [l+r for l, r in zip(row+a, a+row)]
pascal_triangel(6)
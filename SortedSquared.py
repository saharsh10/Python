def sortsquare(array):
    a = []
    n = len(array)
    left = 0
    right = n-1
    for i in range(0, n):
        if abs(array[left]) > array[right]:
            a.append((array[left] * array[left]))
            left += 1
        else:
            a.append((array[right] * array[right]))
            right -= 1
    return a[::-1]

print(sortsquare([-6, -4, 1, 2, 3]))
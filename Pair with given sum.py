def test(array, sum):
    d = {}
    #for i, j in enumerate(array):
    for i in range(0, len(array)):
        #c = sum - j
        c = sum - array[i]
        if c in d:
            return c, array[i]
        #d[j] = i
        d[array[i]] = i
    return False

a = [2,1,4,3]
print(test(a, 4))

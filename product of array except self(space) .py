#space complexity O(n)
#time complexity O(n)
def productofarrayexceptself(array):
    output = [0] * len(array)
    output[0] = 1
    temp = 1
    for i in range(1, len(array)):
        output[i] = output[i-1] * array[i-1]
    for i in range(len(array)-1, -1, -1):
        output[i] = output[i] * temp
        temp = temp * array[i]
    return output
print(productofarrayexceptself([1,2,3,4]))
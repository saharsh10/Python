def first_index(array, low, high, n, target):
    if high >= low:
        middle = low + (high-low)/2
        if array[middle] == target and (middle == 0 or target > array[middle - 1]):
            return middle
        elif target>array[middle]:
            return first_index(a, middle + 1, high, n, target)
        else:
            return first_index(a, low, middle - 1, n, target)

def last_index(array, low, high, n, target):
    if high >= low:
        middle = low + (high - low)/2
        if array[middle] == target and (middle == n-1 or target < array[middle + 1]):
            return middle
        elif target < array[middle]:
            return last_index(a, low, middle - 1, n, target)
        else:
            return last_index(a, middle + 1, high, n, target)


a = [1,2,2,2,3,4,5,6,7,7,8,9]
print(first_index(a, 0, len(a) - 1, len(a), 2))
print(last_index(a, 0, len(a) - 1, len(a), 2))
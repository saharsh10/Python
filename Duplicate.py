# 0 < array[i] <= lenght of array
#solve without extra space and O(n) time
def duplicate(array):
    a = []
    for i in range(0, len(array)):
        index = abs(array[i]) - 1
        if array[index] < 0:
            a.append(index+1)
        array[index] = -array[index]
    return a 
print(duplicate(
    [4,3,2,7,8,2,3,1]
)) 
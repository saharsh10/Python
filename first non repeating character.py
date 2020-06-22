def duplicate(str):
    array = []
    dictionary = {}
    for i in str:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
        array.append(i)
    for i in array:
        if dictionary[i] == 1:
            return i
    return False

print(duplicate('aaabcccdeeef'))
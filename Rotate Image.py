def rotate(matrix):
    n = len(matrix)
    for i in range(0,n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for i in range(0,n):
        for j in range(0, n/2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = temp
    return matrix

print(rotate(
    [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
))
#output
#[13,9,5,1]
#[14,10,6,2]
#[15,11,7,3]
#[16,12,8,4]
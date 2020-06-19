#Get the result without using division 
def productofarray(array):
    n = len(array) #[1,2,3,4] so n = 4
    left = [0]*n
    right = [0]*n
    product = [0]*n
    left[0] = 1 #[1,0,0,0]
    right[n-1] = 1 #[0,0,0,1]
    for i in range(1, n):
        left[i] = array[i-1] * left[i-1]
    
    for i in range(n-2, -1, -1):
        right[i] = array[i+1] * right[i+1]

    for i in range(0,n):
        product[i] = left[i] * right[i]
    return product
print(
    productofarray(
        [1,2,3,4]
    )
)
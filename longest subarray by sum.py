def longestSubArrayBySum(array, sum):
    n = len(array)
    s = 0
    maxlength = 0
    d = {}

    for i in range(0, n):
        s = s + array[i]
        if s == sum:
            maxlength = i + 1
        elif s-sum in d:
            maxlength = max(maxlength, i-d[s-sum])
        if s not in d:
            d[s] = i
    return maxlength

print(
    longestSubArrayBySum(
        [1,2,3,4,5,0,0,0,6,7,8,9,10], 15
    )
)
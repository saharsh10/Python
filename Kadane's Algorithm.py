def kadane(array):
    max_ending_here = 0
    max_now = 0

    for i in range(0, len(array)):
        max_ending_here = max_ending_here + array[i]
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_ending_here > max_now:
            max_now = max_ending_here
    return max_now

print(kadane(
    [-2, 2, 5, -11, 6]
))
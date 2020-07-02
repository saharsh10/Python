def knapsack(MaxWeight, ValueofItem, WeightofItem):
    n  = len(ValueofItem)
    KnapsackArray = [[0 for i in range(MaxWeight+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(MaxWeight+1):
            if i == 0 or j == 0:
                KnapsackArray[i][j] = 0
            elif WeightofItem[i-1] <= j:
                KnapsackArray[i][j] = max(ValueofItem[i-1] + KnapsackArray[i-1][j - WeightofItem[i-1]], KnapsackArray[i-1][j])
            else:
                KnapsackArray[i][j] = KnapsackArray[i-1][j]
    return KnapsackArray[i][j]

print(knapsack(
    5, [60,50,70,30], [5,3,4,2]
))
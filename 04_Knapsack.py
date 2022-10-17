def knapsack(W, wt, val):
    n = min(len(wt), len(val))
    s_a = [(wt[i], val[i]) for i in range(n)]
    s_a.sort(key=lambda item:item[1], reverse=True)

    max_value = 0
    result_knapsack = []

    for item in s_a:
        if item[0] <= W:
            max_value += item[1]
            W -= item[0]
            result_knapsack.append(item)
             
    return max_value


value = [50, 100, 120]
weight = [10, 20, 30]
allowed_weight = 50

print(knapsack(allowed_weight, weight, value))
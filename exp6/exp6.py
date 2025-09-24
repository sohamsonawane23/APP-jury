print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
# Top-Down approach with memoization
def knapsack_top_down(values, weights, W, n, memo):
    # Base case: no items or no capacity
    if n == 0 or W == 0:
        return 0

    # Return cached result if available
    if (n, W) in memo:
        return memo[(n, W)]

    if weights[n - 1] <= W:
        # Include the item
        include = values[n - 1] + knapsack_top_down(values, weights, W - weights[n - 1], n - 1, memo)
        # Exclude the item
        exclude = knapsack_top_down(values, weights, W, n - 1, memo)
        memo[(n, W)] = max(include, exclude)
    else:
        # Item too heavy, exclude it
        memo[(n, W)] = knapsack_top_down(values, weights, W, n - 1, memo)

    return memo[(n, W)]


# Bottom-Up approach with tabulation
def knapsack_bottom_up(values, weights, W):
    n = len(values)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50
    n = len(values)

    memo = {}
    result_top_down = knapsack_top_down(values, weights, W, n, memo)
    print(f"Top-Down Result: Maximum value in knapsack = {result_top_down}")

    result_bottom_up = knapsack_bottom_up(values, weights, W)
    print(f"Bottom-Up Result: Maximum value in knapsack = {result_bottom_up}")

print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
def unique_paths(m, n):
    # Create a 2D DP table initialized with 1 for first row and column
    dp = [[1] * n for _ in range(m)]

    # Fill the dp table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]

# Example usage:
rows = 3
cols = 7
print(f"Number of unique paths in a {rows}x{cols} grid: {unique_paths(rows, cols)}")

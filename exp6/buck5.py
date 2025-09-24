print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
def tile_2xn(n):
    if n == 0 or n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# Example usage:
n = 5
print(f"Number of ways to tile a 2x{n} board: {tile_2xn(n)}")

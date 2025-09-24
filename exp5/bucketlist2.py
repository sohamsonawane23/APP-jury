print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
def is_subset_sum(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][target]

# Example usage:
nums = list(map(int, input("Enter the set elements separated by space: ").split()))
target = int(input("Enter the target sum: "))
if is_subset_sum(nums, target):
    print("A subset with the given sum exists.")
else:
    print("No subset with the given sum exists.")

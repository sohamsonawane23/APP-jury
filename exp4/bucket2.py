print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i  # delete all chars from str1
    for j in range(n + 1):
        dp[0][j] = j  # insert all chars to str1

    # Fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # characters match
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # Deletion
                    dp[i][j - 1],    # Insertion
                    dp[i - 1][j - 1] # Substitution
                )

    return dp[m][n]

# Example usage:
s1 = "kitten"
s2 = "sitting"
result = edit_distance(s1, s2)
print(f"Minimum edit operations to convert '{s1}' to '{s2}': {result}")

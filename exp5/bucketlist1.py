print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
def lcs_length(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if str1[i] == str2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[m][n]

def shortest_common_supersequence_length(str1, str2):
    lcs_len = lcs_length(str1, str2)
    return len(str1) + len(str2) - lcs_len

# Example usage:
X = input("Enter first string: ")
Y = input("Enter second string: ")
print("Length of Shortest Common Supersequence:", shortest_common_supersequence_length(X, Y))


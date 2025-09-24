print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
def shortest_common_supersequence(str1, str2):
    m, n = len(str1), len(str2)

    # Compute Longest Common Subsequence (LCS) matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the shortest common supersequence from dp table
    i, j = m, n
    scs = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            scs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            scs.append(str1[i - 1])
            i -= 1
        else:
            scs.append(str2[j - 1])
            j -= 1

    # Add remaining characters from str1 or str2
    while i > 0:
        scs.append(str1[i - 1])
        i -= 1
    while j > 0:
        scs.append(str2[j - 1])
        j -= 1

    # Reverse list since we built it backwards
    scs.reverse()

    return ''.join(scs)

# Example usage
s1 = "abac"
s2 = "cab"
result = shortest_common_supersequence(s1, s2)
print(f"Shortest common supersequence of '{s1}' and '{s2}': '{result}'")

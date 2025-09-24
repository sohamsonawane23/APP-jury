print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
def longest_repeating_subsequence(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Build the dp table
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # If characters match and indexes are not same
            if s[i - 1] == s[j - 1] and i != j:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the subsequence from the dp table
    i, j = n, n
    subseq = []
    while i > 0 and j > 0:
        if s[i - 1] == s[j - 1] and i != j:
            subseq.append(s[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(subseq))

# Example usage:
input_str = "aabb"
result = longest_repeating_subsequence(input_str)
print(f"Longest repeating subsequence in '{input_str}': '{result}'")

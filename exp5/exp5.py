print("Soham Sonawane")
def lcs(seq1, seq2):
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if seq1[i] == seq2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    # To reconstruct LCS string
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if seq1[i-1] == seq2[j-1]:
            lcs_str.append(seq1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(lcs_str))


s1 = input("Enter first sequence: ")
s2 = input("Enter second sequence: ")
result = lcs(s1, s2)
print("Longest Common Subsequence:", result)

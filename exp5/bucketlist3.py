print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):  # length of substring
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])


    return dp[0][n - 1]


string = input("Enter a string: ")
print("Length of the Longest Palindromic Subsequence:", longest_palindromic_subsequence(string))

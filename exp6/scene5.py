print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
def calculate_edit_distance(student, correct):
    m, n = len(student), len(correct)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i  # delete all from student
    for j in range(n + 1):
        dp[0][j] = j  # insert all to student

    # Fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if student[i - 1] == correct[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # deletion
                    dp[i][j - 1],    # insertion
                    dp[i - 1][j - 1] # substitution
                )

    return dp, dp[m][n]

# Generate student and correct answers
student_answers = ["cat", "hat", "dog", "fog"]
correct_answers = ["bat", "hat", "dog", "log"]

# Calculate edit distance matrix and minimum distance
dp_matrix, min_distance = calculate_edit_distance(student_answers, correct_answers)

print("Student answers:", student_answers)
print("Correct answers:", correct_answers)
print(f"Minimum edit distance: {min_distance}\n")

print("DP Matrix:")
for row in dp_matrix:
    print(row)

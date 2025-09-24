print("soham sonawane")
import random

# Generate traffic counts for 60 minutes (random between 20 and 80 cars)
traffic_counts = [random.randint(20, 80) for _ in range(60)]

# Stable flow range
min_stable = 40
max_stable = 60

# DP array to track longest stable streak ending at each minute
dp = [0] * len(traffic_counts)

max_length = 0

for i in range(len(traffic_counts)):
    if min_stable <= traffic_counts[i] <= max_stable:
        dp[i] = 1 if i == 0 else dp[i - 1] + 1
    else:
        dp[i] = 0
    max_length = max(max_length, dp[i])

print("Minute-wise traffic counts:", traffic_counts)
print(f"Longest stable flow length in range [{min_stable}, {max_stable}]:", max_length)

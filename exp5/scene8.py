import random

# Generate random cost and area for 50 sections
n = 50
costs = [random.randint(1, 10) for _ in range(n)]  # energy cost between 1 and 10
areas = [random.randint(5, 20) for _ in range(n)]  # area covered between 5 and 20

battery_limit = 100  # total battery energy limit

# dp[i][j] represents max area using first i sections with battery limit j
dp = [[0] * (battery_limit + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    cost = costs[i - 1]
    area = areas[i - 1]
    for j in range(1, battery_limit + 1):
        if cost <= j:
            dp[i][j] = max(dp[i - 1][j], area + dp[i - 1][j - cost])
        else:
            dp[i][j] = dp[i - 1][j]

print("Costs (energy):", costs)
print("Areas:", areas)
print("Battery limit:", battery_limit)
print("Maximum area cleaned:", dp[n][battery_limit])

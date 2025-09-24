print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
def matrix_chain_order(costs):
    n = len(costs) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]

    # m[i][j] holds the minimum cost to multiply chain from i to j

    for length in range(2, n + 1):  # length of the chain
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                # Cost = cost of left + cost of right + cost of merging
                cost = m[i][k] + m[k + 1][j] + costs[i - 1] * costs[k] * costs[j]
                if cost < m[i][j]:
                    m[i][j] = cost

    return m[1][n]

# Generate video segments' render costs (dimensions)
# Suppose each effect's output dimension (cost) is represented as an integer
segments = [10, 20, 30, 40, 30]

min_cost = matrix_chain_order(segments)
print(f"Minimum processing time (cost) for optimal merging order: {min_cost}")

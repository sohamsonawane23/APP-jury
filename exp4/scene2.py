print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
def climb_stairs(n, memo=None):
    if memo is None:
        memo = {}

    if n == 0 or n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
    return memo[n]

# Example usage:
stairs = 10
print(f"Number of unique ways to climb {stairs} stairs:", climb_stairs(stairs))

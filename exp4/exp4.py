def fibonacci_iterative(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1

    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b

if __name__ == "__main__":
    test_values = [0, 1, 2, 5, 10, 20, 50]

    for n in test_values:
        result = fibonacci_iterative(n)
        print(f"The {n}th Fibonacci number is: {result}")

    large_n = 100
    large_result = fibonacci_iterative(large_n)
    print(f"\nThe {large_n}th Fibonacci number is: {large_result}")
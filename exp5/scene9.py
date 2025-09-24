print("Soham Sonawane")
import random

# Generate hourly price changes for 24 hours (-5 to 5 range)
price_changes = [random.randint(-5, 5) for _ in range(24)]

# Base prices for the first two hours (assumed)
base_price_0 = 100
base_price_1 = base_price_0 + price_changes[0]

# Memo dictionary to store computed prices
memo = {0: base_price_0, 1: base_price_1}

def predicted_price(hour):
    # Base cases already stored
    if hour in memo:
        return memo[hour]

    # Fibonacci-style recurrence using previous two hours and current hour change
    price = predicted_price(hour - 1) + predicted_price(hour - 2) + price_changes[hour - 1]
    memo[hour] = price
    return priceṣ

# Predict price for next hour (hour 24)
next_hour = 24
next_price = predicted_price(next_hour)

print("Hourly price changes:", price_changes)
print(f"Predicted price at hour {next_hour}:", next_price)

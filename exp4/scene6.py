print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
import random

# Generate random daily expenses for 30 days (0 to 100 units)
expenses = [random.randint(0, 100) for _ in range(30)]

def summarize_week(expenses_slice):
    total = sum(expenses_slice)
    average = total / len(expenses_slice)
    no_spend_days = sum(1 for x in expenses_slice if x == 0)

    # Identify longest no-spend streak in the slice
    max_streak = 0
    current_streak = 0
    for amount in expenses_slice:
        if amount == 0:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0

    return total, average, no_spend_days, max_streak

# Slice week 1 and week 4 (days 1-7 and 22-28, 0-based indexing)
week_1 = expenses[0:7]
week_4 = expenses[21:28]

# Summarize weeks
total_w1, avg_w1, no_spend_w1, streak_w1 = summarize_week(week_1)
total_w4, avg_w4, no_spend_w4, streak_w4 = summarize_week(week_4)

# Print results
print(f"Expenses for 30 days: {expenses}\n")

print("Week 1 Summary:")
print(f" Total: {total_w1}")
print(f" Average: {avg_w1:.2f}")
print(f" No-spend days: {no_spend_w1}")
print(f" Longest no-spend streak: {streak_w1}\n")

print("Week 4 Summary:")
print(f" Total: {total_w4}")
print(f" Average: {avg_w4:.2f}")
print(f" No-spend days: {no_spend_w4}")
print(f" Longest no-spend streak: {streak_w4}")


print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
import random

# Generate random heart rate data for 10 minutes (range 60 to 150 bpm)
heart_rates = [random.randint(60, 150) for _ in range(10)]

# Index the first 5 minutes
first_5 = heart_rates[:5]

# Compute minimum, maximum, and average heart rates for entire data and for first 5 minutes
min_hr = min(heart_rates)
max_hr = max(heart_rates)
avg_hr = sum(heart_rates) / len(heart_rates)

min_hr_5 = min(first_5)
max_hr_5 = max(first_5)
avg_hr_5 = sum(first_5) / len(first_5)

# Filter high heart rates (>120 bpm)
high_hr = [hr for hr in heart_rates if hr > 120]

print("Heart rate data (10 min):", heart_rates)
print("First 5 minutes:", first_5)
print(f"Overall Min: {min_hr}, Max: {max_hr}, Average: {avg_hr:.2f}")
print(f"First 5 Min Min: {min_hr_5}, Max: {max_hr_5}, Average: {avg_hr_5:.2f}")
print("High heart rates (>120 bpm):", high_hr)

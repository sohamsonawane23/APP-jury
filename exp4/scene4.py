print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
import random

# Generate random distance data for 45 minutes (in meters), e.g., between 0.5m and 2.5m per minute
distance_data = [round(random.uniform(0.5, 2.5), 2) for _ in range(45)]

# Calculate total distance covered
total_distance = sum(distance_data)

# Calculate average distance per minute
avg_distance = total_distance / 45

# Identify minutes of no movement (distance = 0)
no_movement_minutes = sum(1 for dist in distance_data if dist == 0)

print("Distance covered each minute (meters):")
print(distance_data)

print("\nEfficiency Summary:")
print(f" Total distance covered: {total_distance:.2f} meters")
print(f" Average distance per minute: {avg_distance:.2f} meters")
print(f" Number of minutes without movement: {no_movement_minutes}")

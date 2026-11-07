
import random
import time

# Generate 365 daily rainfall readings
random.seed(10)
readings = [random.randint(0, 20) for i in range(365)]

# Weekly rainfall totals using slicing
weekly_totals = []

for i in range(0, len(readings), 7):
    week = readings[i:i+7]
    weekly_totals.append(sum(week))

print("Weekly totals:", weekly_totals)
print("Wettest week:", weekly_totals.index(max(weekly_totals)) + 1)
print("Driest week:", weekly_totals.index(min(weekly_totals)) + 1)

# Maximum and minimum readings
print("Maximum rainfall:", max(readings))
print("Maximum position:", readings.index(max(readings)) + 1)

print("Minimum rainfall:", min(readings))
print("Minimum position:", readings.index(min(readings)) + 1)

# Dry days
dry_days = [i+1 for i in range(len(readings)) if readings[i] == 0]
print("Dry days:", dry_days)

# Naive moving average
def naive_average(data):
    averages = []
    for i in range(len(data) - 6):
        averages.append(sum(data[i:i+7]) / 7)
    return averages

# Running sum moving average
def running_average(data):
    if len(data) < 7:
        return []

    averages = []
    total = sum(data[:7])
    averages.append(total / 7)

    for i in range(7, len(data)):
        total = total - data[i-7] + data[i]
        averages.append(total / 7)

    return averages

print("First 5 naive averages:", naive_average(readings)[:5])
print("First 5 running averages:", running_average(readings)[:5])

# Test empty and short lists
print("Empty list:", running_average([]))
print("Short list:", running_average([2, 4, 5]))

# Time comparison
for n in [365, 36500, 365000]:
    data = [random.randint(0, 20) for i in range(n)]

    start = time.perf_counter()
    naive_average(data)
    naive_time = time.perf_counter() - start

    start = time.perf_counter()
    running_average(data)
    running_time = time.perf_counter() - start

    print("\nReadings:", n)
    print("Naive time:", naive_time)
    print("Running sum time:", running_time)

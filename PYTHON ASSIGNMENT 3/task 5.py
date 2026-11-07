
readings = [-55, 1, 4, 9, 52, 6, 3, 10]

# Method 1: For loop with append()
valid = []

for temp in readings:
    if -50 <= temp <= 50:
        valid.append(temp)

fahrenheit = []

for temp in valid:
    fahrenheit.append((temp * 9/5) + 32)

print("Using for loop:")
print("Valid readings:", valid)
print("Fahrenheit:", fahrenheit)

# Method 2: List comprehension
valid2 = [temp for temp in readings if -50 <= temp <= 50]
fahrenheit2 = [(temp * 9/5) + 32 for temp in valid2]

print("\nUsing list comprehension:")
print("Valid readings:", valid2)
print("Fahrenheit:", fahrenheit2)

# Method 3: map() and filter()
valid3 = list(filter(lambda x: -50 <= x <= 50, readings))
fahrenheit3 = list(map(lambda x: (x * 9/5) + 32, valid3))

print("\nUsing map and filter:")
print("Valid readings:", valid3)
print("Fahrenheit:", fahrenheit3)

# Alarm minutes using enumerate()
alarms = [
    minute
    for minute, temp in enumerate(readings, start=1)
    if -50 <= temp <= 50 and (temp < 2 or temp > 8)
]

print("\nAlarm minutes:", alarms)

# Dictionary comprehension
celsius_fahrenheit = {
    temp: (temp * 9/5) + 32 for temp in valid
}
print("Temperature dictionary:", celsius_fahrenheit)

# Set comprehension
alarm_temperatures = {
    temp for temp in valid if temp < 2 or temp > 8
}
print("Alarm temperatures:", alarm_temperatures)

# Check identical results
print("\nAll methods give same result:",
      valid == valid2 == valid3 and
      fahrenheit == fahrenheit2 == fahrenheit3)

# Generator expression
generator = (temp for temp in readings if -50 <= temp <= 50)
print("Generator values:", list(generator))

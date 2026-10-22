
import math

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def calculate_rate(fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return round(rate, 2)

fat = 4.2
snf = 8.7
litres = 10

print("Fat steps:", round((fat - 3.5) / 0.1))
print("SNF steps:", round((snf - 8.5) / 0.1))
print("Rate:", calculate_rate(fat, snf))
print("Amount:", round(litres * calculate_rate(fat, snf), 2))

print("Unexpected result:", (4.2 - 3.5) / 0.1)
print("Using round:", round((4.2 - 3.5) / 0.1))
print("round(-2.7):", round(-2.7))
print("int(-2.7):", int(-2.7))
print("floor(-2.7):", math.floor(-2.7))

print("Chained comparison:", 2.0 <= fat <= 7.0)
print("Boolean AND:", fat >= 2.0 and fat <= 7.0)

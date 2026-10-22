
BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def rate_per_litre(fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(BASE_RATE + fat_steps * FAT_STEP_VALUE
                 + snf_steps * SNF_STEP_VALUE, 2)

def payout(litres, fat, snf):
    if litres < 0:
        raise ValueError("Litres cannot be negative")
    if not 2.0 <= fat <= 7.0:
        raise ValueError("Fat must be between 2.0 and 7.0")
    if snf <= 0:
        raise ValueError("SNF must be positive")
    return round(litres * rate_per_litre(fat, snf), 2)

# Test cases
tests = [
    (10, 3.5, 8.5, 300.00),
    (8.5, 4.2, 8.7, 283.90),
    (12, 3.1, 8.3, 333.60),
    (10, 2.0, 8.5, 240.00),
    (10, 7.0, 8.5, 440.00),
]

print("Expected       Actual         Result")
for litres, fat, snf, expected in tests:
    actual = payout(litres, fat, snf)
    result = "PASS" if actual == expected else "FAIL"
    print(f"{expected:10.2f} {actual:12.2f} {result}")
    assert actual == expected

# Invalid input tests
invalid_tests = [
    (-1, 3.5, 8.5),
    (10, 1.5, 8.5),
    (10, 7.5, 8.5),
    (10, 3.5, 0)
]

for case in invalid_tests:
    try:
        payout(*case)
    except ValueError:
        print("Invalid input correctly rejected:", case)
    else:
        print("FAIL:", case)

print("All tests completed.")

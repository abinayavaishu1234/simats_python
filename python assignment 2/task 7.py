
# Q7 - String Concatenation Redesign

import time

items = [f"Item{i}" for i in range(100000)]


# Original method
def original_method(items):
    result = ""

    for item in items:
        result += item + ";"

    return result


# Redesigned method
def redesigned_method(items):
    return ";".join(items) + ";"


# Measure original method
start = time.perf_counter()
old_result = original_method(items)
old_time = time.perf_counter() - start


# Measure redesigned method
start = time.perf_counter()
new_result = redesigned_method(items)
new_time = time.perf_counter() - start


print("Original method time:", round(old_time, 4))
print("Redesigned method time:", round(new_time, 4))

print("Same output:", old_result == new_result)

if new_time < old_time:
    print("Redesigned method is faster")
else:
    print("Original method was faster in this test")


import time
import logging
import cProfile
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

def calculate_average(numbers):
    try:
        if len(numbers) == 0:
            raise ValueError("List cannot be empty")

        total = sum(numbers)
        average = total / len(numbers)

        return average

    except ValueError as error:
        logging.error(error)
        return None

print("DEBUGGING PROGRAM")

data = [10, 20, 30, 40, 50]

result = calculate_average(data)
print("Numbers:", data)
print("Average:", result)
print("\nTESTING EMPTY LIST")
empty_result = calculate_average([])
print("Result:", empty_result)
print("\nPERFORMANCE PROFILING")

start = time.perf_counter()

for i in range(100000):
    calculate_average([10, 20, 30, 40, 50])

end = time.perf_counter()

execution_time = end - start

print("Execution time:", round(execution_time, 5), "seconds")
print("\nPROFILING DETAILS")
cProfile.run(
    "calculate_average([10, 20, 30, 40, 50])"
)
print("\nTASK 4 COMPLETED")

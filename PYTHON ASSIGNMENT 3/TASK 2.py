
import copy
import sys
import time

# Bus stop coordinates using tuples
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}

print("Bus stops:")
for (latitude, longitude), name in stops.items():
    print(name, latitude, longitude)

# Incorrect grid
rows, cols = 3, 4
bad = [[0] * cols] * rows
bad[0][1] = 7

# Correct grid using list comprehension
good = [[0 for j in range(cols)] for i in range(rows)]
good[0][1] = 7

print("\nbad :", bad)
print("good:", good)
print(bad[0] is bad[1], good[0] is good[1])

# Aliasing
a = [10, 20, 30]
b = a
b[0] = 99
print("\nAliasing:", a)

# Shallow copy
original = [[1, 2], [3, 4]]
shallow1 = copy.copy(original)
shallow2 = original[:]

shallow1[0][0] = 100
print("Original after shallow copy:", original)

# Deep copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 500

print("Original after deep copy:", original)
print("Deep copy:", deep)

# Tuple as dictionary key
print("\nBus stop:", stops[(13.0418, 80.2341)])

# List as dictionary key causes error
try:
    sample = {[13.0418, 80.2341]: "T. Nagar"}
except TypeError as e:
    print("Error:", e)

# Memory comparison
values = list(range(1000000))
tuple_values = tuple(values)

print("\nList memory:", sys.getsizeof(values))
print("Tuple memory:", sys.getsizeof(tuple_values))

# Creating and indexing
start = time.perf_counter()
my_list = list(range(1000000))
print("List creation time:", time.perf_counter() - start)

start = time.perf_counter()
my_tuple = tuple(range(1000000))
print("Tuple creation time:", time.perf_counter() - start)

start = time.perf_counter()
x = my_list[500000]
print("List indexing time:", time.perf_counter() - start)

start = time.perf_counter()
y = my_tuple[500000]
print("Tuple indexing time:", time.perf_counter() - start)

# List inside a tuple
data = ([10, 20], 30)
data[0].append(40)
print("Tuple with list:", data)

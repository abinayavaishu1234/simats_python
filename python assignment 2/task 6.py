
# Q6 - Recursion and Memoisation

from functools import lru_cache

calls = 0


def ways_naive(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


n = 25

calls = 0
print("Naive result:", ways_naive(n))
print("Naive calls:", calls)

calls = 0
print("Memoised result:", ways_memo(n))
print("Memoised calls:", calls)


# Iterative method
def ways_loop(n):
    if n <= 1:
        return 1

    a, b = 1, 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


print("Loop result:", ways_loop(25))
print("Ways for 6 stairs:", ways_memo(6))


from decimal import Decimal
import time

sizes = [300, 6000, 150000]

for n in sizes:
    payments = ["33.40"] * n + ["0.10"] * 3

    start = time.perf_counter()
    float_total = sum(float(x) for x in payments)
    float_time = time.perf_counter() - start

    start = time.perf_counter()
    decimal_total = sum((Decimal(x) for x in payments),
                        Decimal("0.00"))
    decimal_time = time.perf_counter() - start

    print("Payments:", n)
    print("Float total:", round(float_total, 2))
    print("Decimal total:", decimal_total)
    print("Difference:", abs(Decimal(str(float_total)) - decimal_total))
    print("Float time:", round(float_time, 6), "seconds")
    print("Decimal time:", round(decimal_time, 6), "seconds")
    print()


def calculate_payment(litres, fat, snf):
    """Calculate milk payment."""
    if litres < 0 or not 2.0 <= fat <= 7.0 or snf <= 0:
        return None

    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = 30 + fat_steps * 0.40 + snf_steps * 0.30
    return round(litres * rate, 2)

entries = [
    (10, 3.5, 8.5),
    (8.5, 4.2, 8.7),
    (12, 3.1, 8.3)
]

total = 0

for litres, fat, snf in entries:
    amount = calculate_payment(litres, fat, snf)
    if amount is not None:
        print("Payment: Rs.", amount)
        total += amount
    else:
        print("Invalid entry")

print("Total payment: Rs.", round(total, 2))
print("Ten-day total: Rs.", round(total * 10, 2))

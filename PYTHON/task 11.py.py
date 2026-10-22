
from decimal import Decimal

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

def rate_per_litre(fat, snf):
    """Calculate the rate per litre."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = BASE_RATE
    rate += Decimal(fat_steps) * FAT_STEP_VALUE
    rate += Decimal(snf_steps) * SNF_STEP_VALUE
    return rate.quantize(Decimal("0.01"))

def payout(litres, fat, snf):
    """Calculate payment using exact decimal money."""
    rate = rate_per_litre(fat, snf)
    amount = Decimal(str(litres)) * rate
    return amount.quantize(Decimal("0.01"))

entries = [
    (10, 3.5, 8.5),
    (8.5, 4.2, 8.7),
    (12, 3.1, 8.3)
]

total = Decimal("0.00")

for litres, fat, snf in entries:
    amount = payout(litres, fat, snf)
    total += amount
    print("Payment: Rs.", amount)

print("Final total: Rs.", total)

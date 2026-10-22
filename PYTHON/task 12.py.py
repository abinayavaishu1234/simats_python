
from decimal import Decimal
BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
SEASONAL_BASE_RATE = Decimal("32.00")
SEASONAL_FAT_STEP_VALUE = Decimal("0.45")

BONUS_LIMIT = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")


def rate_per_litre(fat, snf, month):
    """Calculate milk rate based on the month."""
    if month in ["April", "May", "June"]:
        base = SEASONAL_BASE_RATE
        fat_value = SEASONAL_FAT_STEP_VALUE
    else:
        base = BASE_RATE
        fat_value = FAT_STEP_VALUE

    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = base
    rate += Decimal(fat_steps) * fat_value
    rate += Decimal(snf_steps) * SNF_STEP_VALUE

    return rate.quantize(Decimal("0.01"))


def payout(litres, fat, snf, month):
    """Calculate payment for one milk entry."""
    rate = rate_per_litre(fat, snf, month)
    amount = Decimal(str(litres)) * rate
    return amount.quantize(Decimal("0.01"))


def ten_day_total(entries, month):
    """Calculate total payment and eligible volume bonus."""
    total_litres = sum(
        (Decimal(str(entry[0])) for entry in entries),
        Decimal("0")
    )

    total_payment = Decimal("0.00")

    for litres, fat, snf in entries:
        total_payment += payout(litres, fat, snf, month)

    if total_litres > BONUS_LIMIT:
        bonus = total_litres * BONUS_PER_LITRE
    else:
        bonus = Decimal("0.00")

    bonus = bonus.quantize(Decimal("0.01"))
    total_payment += bonus

    return total_litres, bonus, total_payment
print("April rate:", rate_per_litre(4.2, 8.7, "April"))
print("July rate:", rate_per_litre(4.2, 8.7, "July"))
entries = [
    (200, 3.5, 8.5),
    (180, 4.2, 8.7),
    (150, 3.5, 8.5)
]

litres, bonus, total = ten_day_total(entries, "April")

print("Ten-day litres:", litres)
print("Bonus: Rs.", bonus)
print("Total payment including bonus: Rs.", total)
entries_500 = [(500, 3.5, 8.5)]
litres, bonus, total = ten_day_total(entries_500, "April")

print("Exactly 500 litres bonus: Rs.", bonus)

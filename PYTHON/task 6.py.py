
BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def rate_per_litre(fat, snf):
    """Calculate the rate per litre."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE
    rate += snf_steps * SNF_STEP_VALUE
    return round(rate, 2)

def payout(litres, fat, snf):
    """Calculate the payment for the milk supplied."""
    return round(litres * rate_per_litre(fat, snf), 2)

def ten_day_total(daily_amounts):
    """Calculate the total payment for ten days."""
    return round(sum(daily_amounts), 2)

rate = rate_per_litre(4.2, 8.7)
amount = payout(10, 4.2, 8.7)
total = ten_day_total([amount] * 10)

print(f"Rate per litre: Rs. {rate:.2f}")
print(f"Daily payout: Rs. {amount:.2f}")
print(f"Ten-day total: Rs. {total:.2f}")

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
DAYS = 10

farmer_id = 101
litres = 10.5
fat = 4.2
snf = 8.7
shift = "Morning"

fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)

rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
amount = round(litres * rate, 2)
ten_day_total = round(amount * DAYS, 2)

print("Farmer ID:", farmer_id)
print("Litres:", litres)
print("Fat %:", fat)
print("SNF %:", snf)
print("Shift:", shift)
print("Rate per litre: Rs.", round(rate, 2))
print("Amount: Rs.", amount)
print("Ten-day total: Rs.", ten_day_total)
print("Fat valid:", 2.0 <= fat <= 7.0)
print("Litres valid:", litres >= 0)


BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
MIN_FAT = 2.0
MAX_FAT = 7.0

farmer_id = 101
litres = 10
fat = 4.2
snf = 8.7

print("Base rate:", BASE_RATE)
print("Fat step value:", FAT_STEP_VALUE)
print("SNF step value:", SNF_STEP_VALUE)
print("Fat limits:", MIN_FAT, "to", MAX_FAT)

value = 10
print("Before:", value, type(value))
value = "ten"
print("After:", value, type(value))

a = 5
b = 10
a, b = b, a
print("After swapping:", a, b)

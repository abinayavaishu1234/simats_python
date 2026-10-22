
def read_number(message):
    while True:
        text = input(message).strip()
        try:
            value = float(text)
            if value < 0:
                print("Enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Enter a valid number.")

farmer_id = input("Enter farmer ID: ").strip()
litres = read_number("Enter litres: ")
fat = read_number("Enter fat percentage: ")
snf = read_number("Enter SNF percentage: ")

if not farmer_id:
    print("Invalid farmer ID")
elif not 2.0 <= fat <= 7.0:
    print("Invalid fat percentage")
elif snf <= 0:
    print("Invalid SNF percentage")
else:
    rate = 30 + round((fat - 3.5) / 0.1) * 0.40
    rate += round((snf - 8.5) / 0.1) * 0.30
    amount = round(litres * rate, 2)

    print(f"Farmer ID: {farmer_id}")
    print(f"Rate per litre: Rs. {rate:.2f}")
    print(f"Amount: Rs. {amount:.2f}")

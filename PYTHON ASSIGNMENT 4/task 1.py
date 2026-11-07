
def process_mess_bill(filename):
    total = 0.0
    report = []
    rejected = []

    try:
        with open(filename, "r") as file:

            for line_number, line in enumerate(file, start=1):

                if not line.strip():
                    continue

                try:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Invalid number of fields")

                    reg_no, name, amount = parts
                    amount = float(amount)

                    report.append(name + " " + str(amount))
                    total += amount

                except ValueError as error:
                    rejected.append((line_number, line.strip(), str(error)))

    except FileNotFoundError:
        print("File not found")
        return

    except PermissionError:
        print("Permission denied")
        return

    print("Mess Bill Report")

    for item in report:
        print(item)

    print("Total:", round(total, 2))

    print("\nRejected Records:")

    for item in rejected:
        print(item)


# Creating sample input file
with open("mess_oct.txt", "w") as file:
    file.write("192311001,Arun,1250.50\n")
    file.write("192311002,Priya,1500\n")
    file.write("192311003,Ravi,wrong\n")
    file.write("192311004,Meena,1200\n")

process_mess_bill("mess_oct.txt")

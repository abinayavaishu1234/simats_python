
# TASK 5 - ORGANISATION A
# Attendance processing using one single script

def read_attendance(filename):
    records = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            records.append(parts)

    return records


def calculate_statistics(records):
    print("\nATTENDANCE REPORT")

    for record in records:
        reg_no = record[0]
        days = record[1:]

        present = days.count("P")
        percentage = (present / len(days)) * 100

        print(reg_no, "-", percentage, "%")


def absent_three_days(records):
    print("\nSTUDENTS ABSENT FOR THREE CONSECUTIVE DAYS")

    for record in records:
        reg_no = record[0]
        days = record[1:]

        for i in range(len(days) - 2):
            if days[i:i+3] == ["A", "A", "A"]:
                print(reg_no)
                break


def write_report(records):
    with open("attendance_report.txt", "w") as file:
        for record in records:
            reg_no = record[0]
            days = record[1:]

            present = days.count("P")
            percentage = (present / len(days)) * 100

            file.write(reg_no + " - " + str(percentage) + "%\n")

    with open("absent_report.txt", "w") as file:
        for record in records:
            days = record[1:]

            for i in range(len(days) - 2):
                if days[i:i+3] == ["A", "A", "A"]:
                    file.write(record[0] + "\n")
                    break

    print("\nReports saved successfully.")


# Main program
if __name__ == "__main__":
    records = read_attendance("attendance.txt")
    calculate_statistics(records)
    absent_three_days(records)
    write_report(records)

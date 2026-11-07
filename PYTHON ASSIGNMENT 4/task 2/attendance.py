import os

folder = "attendance_files"

attendance = {}
processed = 0
damaged = 0

for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        path = os.path.join(folder, filename)

        try:
            with open(path, "r") as file:
                for line in file:
                    try:
                        reg_no, status = line.strip().split(",")

                        if status not in ["P", "A"]:
                            raise ValueError("Invalid status")

                        if reg_no not in attendance:
                            attendance[reg_no] = {"P": 0, "A": 0}

                        attendance[reg_no][status] += 1

                    except ValueError:
                        damaged += 1

            processed += 1

        except FileNotFoundError:
            damaged += 1

with open("attendance_report.txt", "w") as report:
    for reg_no, data in attendance.items():
        total = data["P"] + data["A"]
        percentage = (data["P"] / total) * 100

        report.write(
            f"{reg_no} - Attendance: {percentage:.2f}%\n"
        )

with open("below_75.txt", "w") as report:
    for reg_no, data in attendance.items():
        total = data["P"] + data["A"]
        percentage = (data["P"] / total) * 100

        if percentage < 75:
            report.write(f"{reg_no} - {percentage:.2f}%\n")

with open("error_log.txt", "w") as report:
    report.write(f"Processed files: {processed}\n")
    report.write(f"Damaged records: {damaged}\n")

print("Attendance processing completed!")
print("Processed files:", processed)
print("Damaged records:", damaged)
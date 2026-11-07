
import os
import tempfile


# Custom exception
class InvalidRecord(Exception):
    pass


# Function to check each line
def parse_line(line):
    parts = line.strip().split(",")

    if len(parts) != 3:
        raise InvalidRecord(
            f"expected 3 fields, found {len(parts)}"
        )

    if parts[2] not in ["P", "A"]:
        raise InvalidRecord(
            f"invalid status '{parts[2]}'"
        )

    return tuple(parts)


# Function to process attendance file
def summarise(path):
    present = 0
    absent = 0
    errors = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    reg_no, date, status = parse_line(line)

                except InvalidRecord as error:
                    errors.append((line_number, str(error)))

                else:
                    if status == "P":
                        present += 1
                    else:
                        absent += 1

    except FileNotFoundError as error:
        raise RuntimeError("Attendance file not found") from error

    except PermissionError as error:
        raise RuntimeError("Permission denied") from error

    except UnicodeDecodeError as error:
        raise RuntimeError("Wrong file encoding") from error

    else:
        print("File processed successfully.")

    finally:
        print("File processing attempt finished.")

    return present, absent, errors


# Sample attendance data
data = (
    "192311001,2026-10-08,P\n"
    "192311002,2026-10-08,A\n"
    "192311003,2026-10-08\n"
    "192311004,2026-10-08,L\n"
)

# Create a temporary file
with tempfile.NamedTemporaryFile(
    "w", suffix=".csv", delete=False, encoding="utf-8"
) as tmp:
    tmp.write(data)
    filename = tmp.name

# Process the file
try:
    print(summarise(filename))

except RuntimeError as error:
    print(error)

finally:
    os.remove(filename)

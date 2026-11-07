
# TASK 6 - COLLEGE FEST REGISTRATION DESK

import os

DEPARTMENTS = ["CSE", "AIDS", "ECE", "EEE", "MECH"]

INPUT_FOLDER = "department_files"
OUTPUT_FOLDER = "reports"


def validate_email(email):
    return "@" in email and "." in email.split("@")[-1]


def process_registrations():
    master_records = []
    registered_ids = set()
    event_participants = {}
    error_messages = []

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Read files from all five departments
    for department in DEPARTMENTS:
        filename = os.path.join(INPUT_FOLDER, department + ".txt")

        try:
            with open(filename, "r", encoding="utf-8") as file:

                for line_number, line in enumerate(file, start=1):

                    try:
                        parts = line.strip().split(",", 4)

                        if len(parts) != 5:
                            raise ValueError("Damaged record: expected 5 fields")

                        reg_no, name, dept, email, events = parts

                        reg_no = reg_no.strip()
                        name = name.strip()
                        dept = dept.strip()
                        email = email.strip()
                        events = events.strip()

                        if not all([reg_no, name, dept, email, events]):
                            raise ValueError("One or more fields are empty")

                        if not validate_email(email):
                            raise ValueError("Invalid email address")

                        if reg_no in registered_ids:
                            raise ValueError("Duplicate registration number")

                        event_list = [
                            event.strip()
                            for event in events.split(";")
                            if event.strip()
                        ]

                        if not event_list:
                            raise ValueError("No valid events entered")

                        # Save valid registration
                        registered_ids.add(reg_no)

                        record = {
                            "reg_no": reg_no,
                            "name": name,
                            "department": dept,
                            "email": email,
                            "events": event_list
                        }

                        master_records.append(record)

                        # Add student to each selected event
                        for event in event_list:
                            event_participants.setdefault(event, []).append(record)

                    except ValueError as error:
                        error_messages.append(
                            f"{department}.txt - Line {line_number}: {error}"
                        )

        except FileNotFoundError:
            error_messages.append(
                f"{department}.txt - File not found"
            )

        except PermissionError:
            error_messages.append(
                f"{department}.txt - Permission denied"
            )

        except UnicodeDecodeError:
            error_messages.append(
                f"{department}.txt - Invalid file encoding"
            )

        except OSError as error:
            error_messages.append(
                f"{department}.txt - File error: {error}"
            )

    # Create clean master list
    with open(os.path.join(OUTPUT_FOLDER, "master_list.txt"),
              "w", encoding="utf-8") as file:

        for record in master_records:
            file.write(
                f"{record['reg_no']}, {record['name']}, "
                f"{record['department']}, {record['email']}, "
                f"{'; '.join(record['events'])}\n"
            )

    # Create separate participant list for every event
    event_folder = os.path.join(OUTPUT_FOLDER, "event_participants")
    os.makedirs(event_folder, exist_ok=True)

    for event, participants in event_participants.items():
        safe_name = "".join(
            character for character in event
            if character.isalnum() or character in "_-"
        )

        event_file = os.path.join(event_folder, safe_name + ".txt")

        with open(event_file, "w", encoding="utf-8") as file:
            file.write(f"PARTICIPANTS - {event}\n\n")

            for record in participants:
                file.write(
                    f"{record['reg_no']} - {record['name']} "
                    f"({record['department']})\n"
                )

    # Create summary report
    with open(os.path.join(OUTPUT_FOLDER, "summary_report.txt"),
              "w", encoding="utf-8") as file:

        file.write("COLLEGE FEST REGISTRATION SUMMARY\n")
        file.write("---------------------------------\n")
        file.write(f"Total valid registrations: {len(master_records)}\n")

        for event, participants in sorted(event_participants.items()):
            file.write(
                f"{event}: {len(participants)} participants\n"
            )

        file.write(f"Total errors found: {len(error_messages)}\n")

    # Create error log
    with open(os.path.join(OUTPUT_FOLDER, "error_log.txt"),
              "w", encoding="utf-8") as file:

        if error_messages:
            for message in error_messages:
                file.write(message + "\n")
        else:
            file.write("No errors found.\n")

    # Display final result
    print("\nCOLLEGE FEST REGISTRATION PROCESS")
    print("---------------------------------")
    print("Valid registrations:", len(master_records))
    print("Errors found:", len(error_messages))
    print("Reports saved in the reports folder.")

    print("\nEVENT PARTICIPANT COUNTS")

    for event, participants in sorted(event_participants.items()):
        print(event, ":", len(participants))

    print("\nProcessing completed successfully.")


if __name__ == "__main__":
    process_registrations()

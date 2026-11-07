
# TASK 4 - FILE AND EXCEPTION FORENSICS

# Create three sample daily files
with open("day1.txt", "w") as f:
    f.write("Python Book\nData Science Book\n")

with open("day2.txt", "w") as f:
    f.write("AI Book\nMachine Learning Book\n")

with open("day3.txt", "w") as f:
    f.write("Networking Book\nCyber Security Book\n")


# ORIGINAL PROGRAM - SHOWING THE DEFECTS

def save_returns(books):
    log = open("returns_old.log", "w")
    for b in books:
        log.write(b)
    log.close()


def process(day_file):
    try:
        books = open(day_file).read().split("\n")
        save_returns(books)
    except FileNotFoundError:
        print("missing")


print("ORIGINAL PROGRAM OUTPUT")

for day in ["day1.txt", "day2.txt", "day3.txt"]:
    process(day)

with open("returns_old.log", "r") as f:
    print("Old log contents:")
    print(f.read())


# REPAIRED PROGRAM

def save_returns(books):
    with open("returns.log", "a") as log:
        for book in books:
            if book.strip():
                log.write(book + "\n")


def process(day_file):
    try:
        with open(day_file, "r") as f:
            books = f.read().splitlines()

        save_returns(books)

    except FileNotFoundError as error:
        with open("error_log.txt", "a") as log:
            log.write(str(error) + "\n")
        print("Missing file:", day_file)


print("\nREPAIRED PROGRAM OUTPUT")

# Clear old reports before testing
open("returns.log", "w").close()
open("error_log.txt", "w").close()

for day in ["day1.txt", "day2.txt", "day3.txt", "day4.txt"]:
    process(day)

with open("returns.log", "r") as f:
    print("\nFinal returns log:")
    print(f.read())

with open("error_log.txt", "r") as f:
    print("Error log:")
    print(f.read())

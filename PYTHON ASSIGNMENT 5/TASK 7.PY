
import sqlite3

# AIM: Adversarial Data and SQL Injection Testing

# Step 1: Create database
con = sqlite3.connect("task7.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS air_quality")

cur.execute("""
CREATE TABLE air_quality (
    station TEXT,
    date TEXT,
    pm25 REAL
)
""")

# Step 2: Insert sample records safely
readings = [
    ("Adyar", "2026-10-01", 48.0),
    ("Guindy", "2026-10-01", 95.0),
    ("Guindy", "2026-10-03", 121.0),
    ("Adyar", "2026-10-04", 60.0)
]

cur.executemany(
    "INSERT INTO air_quality VALUES (?, ?, ?)",
    readings
)

con.commit()

print("RECORDS INSERTED SUCCESSFULLY")

# Step 3: Display all records
print("\nAIR QUALITY RECORDS")

cur.execute("SELECT * FROM air_quality")

for row in cur.fetchall():
    print(row)

# Step 4: Create parameterised query function
def station_average(name):
    cur.execute(
        "SELECT AVG(pm25) FROM air_quality WHERE station = ?",
        (name,)
    )

    result = cur.fetchone()[0]
    return round(result, 2) if result is not None else None

# Step 5: Find station averages
print("\nSTATION AVERAGES")

print("Adyar:", station_average("Adyar"))
print("Guindy:", station_average("Guindy"))

# Step 6: Test unusual input safely
print("\nSECURITY TEST")

test_input = "Adyar' OR '1'='1"

print("Test Input:", test_input)
print("Query Result:", station_average(test_input))

print("The parameterised query treats the input as data.")

# Step 7: Test invalid data
print("\nINVALID DATA TEST")

test_values = ["100", "-20", "NA", "abc", "1500"]

for value in test_values:
    try:
        number = float(value)

        if 0 <= number <= 999:
            print(value, "-> Valid")
        else:
            print(value, "-> Invalid range")

    except ValueError:
        print(value, "-> Invalid numeric value")

con.close()

print("\nTASK 7 COMPLETED")

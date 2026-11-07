
import csv
import sqlite3
import os

# AIM: Data Cleaning Pipeline

folder = os.path.dirname(os.path.abspath(__file__))

# Step 1: Create sample CSV data
raw_data = """station,date,pm25
Adyar,2026-10-01,48
Adyar,2026-10-02,NA
Adyar,2026-10-03,
Guindy,2026-10-01,95
Guindy,2026-10-02,-5
Guindy,2026-10-03,121
"""

raw_file = os.path.join(folder, "raw_air_quality.csv")

with open(raw_file, "w") as file:
    file.write(raw_data)

print("RAW CSV FILE CREATED")

# Step 2: Read and clean the CSV data
cleaned_rows = []

with open(raw_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        value = row["pm25"].strip()

        if value == "" or value.upper() == "NA":
            continue

        try:
            pm25 = float(value)

            if pm25 < 0 or pm25 > 999:
                continue

            cleaned_rows.append(
                (row["station"], row["date"], pm25)
            )

        except ValueError:
            continue

print("\nCLEANED DATA")
for row in cleaned_rows:
    print(row)

# Step 3: Min-Max Normalisation
values = [row[2] for row in cleaned_rows]

minimum = min(values)
maximum = max(values)

if maximum != minimum:
    normalised = [
        round((value - minimum) / (maximum - minimum), 3)
        for value in values
    ]
else:
    normalised = [0 for value in values]

print("\nNORMALISED VALUES")
print(normalised)

# Step 4: Save cleaned CSV
clean_file = os.path.join(folder, "cleaned_task6.csv")

with open(clean_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["station", "date", "pm25", "normalised_pm25"])

    for row, norm in zip(cleaned_rows, normalised):
        writer.writerow(list(row) + [norm])

# Step 5: Create SQLite database
db_file = os.path.join(folder, "air_quality_task6.db")
con = sqlite3.connect(db_file)
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS readings")

cur.execute("""
CREATE TABLE readings (
    station TEXT,
    date TEXT,
    pm25 REAL,
    normalised_pm25 REAL
)
""")

records = [
    (row[0], row[1], row[2], norm)
    for row, norm in zip(cleaned_rows, normalised)
]

cur.executemany(
    "INSERT INTO readings VALUES (?, ?, ?, ?)",
    records
)

con.commit()

# Step 6: Display station-wise averages
print("\nSTATION-WISE AVERAGE PM2.5")

cur.execute("""
SELECT station, AVG(pm25)
FROM readings
GROUP BY station
""")

for row in cur.fetchall():
    print(row[0], ":", round(row[1], 2))

con.close()

# Step 7: Create chart
try:
    import matplotlib.pyplot as plt

    stations = [row[0] for row in cleaned_rows]
    pm_values = [row[2] for row in cleaned_rows]

    plt.bar(stations, pm_values)
    plt.title("Air Quality PM2.5 Readings")
    plt.xlabel("Station")
    plt.ylabel("PM2.5")
    plt.savefig(os.path.join(folder, "task6_chart.png"))
    plt.show()

    print("\nCHART SAVED SUCCESSFULLY")

except ImportError:
    print("\nMatplotlib is not installed. Chart skipped.")

print("\nCLEANED CSV AND DATABASE SAVED")
print("TASK 6 COMPLETED")

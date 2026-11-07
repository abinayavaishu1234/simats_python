
import csv
import sqlite3

# AIM: To acquire air quality data from CSV
# and create SQLite database tables.

# Step 1: Sample CSV data
data = [
    ["station", "date", "hour", "pm25", "pm10", "no2", "temperature"],
    ["Adyar", "2026-10-01", 10, 48, 80, 25, 30],
    ["Guindy", "2026-10-01", 11, 95, 120, 40, 32],
    ["Adyar", "2026-10-02", 10, "", 75, 20, 29],
    ["Guindy", "2026-10-02", 11, -5, 90, 35, 31],
    ["Adyar", "2026-10-03", 10, 5000, 100, 30, 86]
]

# Step 2: Create CSV file
with open("air_quality.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV FILE CREATED SUCCESSFULLY")

# Step 3: Read and inspect CSV file
with open("air_quality.csv", "r") as file:
    reader = csv.DictReader(file)

    print("\nAIR QUALITY DATA")

    for row in reader:
        print(row)

        if row["pm25"] == "":
            print("Problem: Missing PM2.5 value")

        elif float(row["pm25"]) < 0:
            print("Problem: Negative PM2.5 value")

        elif float(row["pm25"]) > 1000:
            print("Problem: Abnormally high PM2.5 value")

# Step 4: Create SQLite database
con = sqlite3.connect("air_quality.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Stations (
    station_id INTEGER PRIMARY KEY,
    station_name TEXT UNIQUE
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Readings (
    reading_id INTEGER PRIMARY KEY,
    station_id INTEGER,
    date TEXT,
    hour INTEGER,
    pm25 REAL,
    pm10 REAL,
    no2 REAL,
    temperature REAL,
    FOREIGN KEY (station_id) REFERENCES Stations(station_id)
)
""")

# Step 5: Insert station names
stations = ["Adyar", "Guindy"]

for station in stations:
    cur.execute(
        "INSERT OR IGNORE INTO Stations (station_name) VALUES (?)",
        (station,)
    )

con.commit()

# Step 6: Display station details
print("\nSTATION DETAILS")

cur.execute("SELECT * FROM Stations")

for row in cur.fetchall():
    print(row)

print("\nDATABASE TABLES CREATED SUCCESSFULLY")

con.close()

print("\nTASK 1 COMPLETED")

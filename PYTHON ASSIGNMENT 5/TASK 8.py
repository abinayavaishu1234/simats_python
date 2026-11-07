
import random
import time
import sqlite3
import pandas as pd
import cProfile

# AIM: Compare Loops, Pandas and SQL performance

random.seed(42)

# Function 1: Python loop method
def loop_analysis(records):
    totals = {}
    counts = {}

    for station, day, pm25 in records:
        key = (station, day)

        totals[key] = totals.get(key, 0) + pm25
        counts[key] = counts.get(key, 0) + 1

    averages = {
        key: totals[key] / counts[key]
        for key in totals
    }

    return averages


# Test datasets with different station counts
for station_count in [1, 12, 120]:

    print("\n================================")
    print("NUMBER OF STATIONS:", station_count)
    print("================================")

    # Step 1: Generate one year of hourly data
    records = []

    for station_number in range(1, station_count + 1):
        station = "Station_" + str(station_number)

        for hour_number in range(8760):
            day = (hour_number // 24) + 1
            pm25 = round(random.uniform(10, 150), 2)

            records.append((station, day, pm25))

    print("Total records:", len(records))

    # Step 2: Python loop timing
    start = time.perf_counter()

    loop_result = loop_analysis(records)

    loop_time = time.perf_counter() - start

    # Step 3: Pandas timing
    df = pd.DataFrame(
        records,
        columns=["station", "day", "pm25"]
    )

    start = time.perf_counter()

    pandas_result = df.groupby(
        ["station", "day"]
    )["pm25"].mean()

    pandas_time = time.perf_counter() - start

    # Step 4: SQL database
    con = sqlite3.connect(":memory:")
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE readings (
            station TEXT,
            day INTEGER,
            pm25 REAL
        )
    """)

    cur.executemany(
        "INSERT INTO readings VALUES (?, ?, ?)",
        records
    )

    con.commit()

    start = time.perf_counter()

    cur.execute("""
        SELECT station, day, AVG(pm25)
        FROM readings
        GROUP BY station, day
    """)

    sql_result = cur.fetchall()

    sql_time = time.perf_counter() - start

    # Step 5: Display comparison
    print("\nPERFORMANCE COMPARISON")

    print("Python Loop:", round(loop_time, 5), "seconds")
    print("Pandas:", round(pandas_time, 5), "seconds")
    print("SQL:", round(sql_time, 5), "seconds")

    print("\nDaily groups generated:")
    print("Python:", len(loop_result))
    print("Pandas:", len(pandas_result))
    print("SQL:", len(sql_result))

    con.close()


# Step 6: Profile Python loop
print("\nPYTHON PROFILING DETAILS")

profile_records = records[:8760]

profiler = cProfile.Profile()
profiler.enable()

loop_analysis(profile_records)

profiler.disable()
profiler.print_stats(sort="cumtime")

print("\nTASK 8 COMPLETED")

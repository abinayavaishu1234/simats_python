
# Railway timetable
trains = {
    "12601": {
        "name": "Chennai Express",
        "stops": [
            ("Chennai", "06:00", "06:10"),
            ("Katpadi", "08:00", "08:05"),
            ("Bangalore", "11:00", "11:10")
        ],
        "days": {"Monday", "Wednesday", "Friday"}
    },

    "12602": {
        "name": "Coimbatore Express",
        "stops": [
            ("Chennai", "07:00", "07:10"),
            ("Salem", "10:00", "10:05"),
            ("Coimbatore", "12:00", "12:10")
        ],
        "days": {"Tuesday", "Thursday", "Saturday"}
    },

    "12603": {
        "name": "Madurai Express",
        "stops": [
            ("Chennai", "08:00", "08:10"),
            ("Trichy", "12:00", "12:05"),
            ("Madurai", "14:00", "14:10")
        ],
        "days": {"Monday", "Tuesday", "Friday"}
    },

    "12604": {
        "name": "Bangalore Express",
        "stops": [
            ("Chennai", "05:00", "05:10"),
            ("Katpadi", "07:00", "07:05"),
            ("Bangalore", "10:00", "10:10")
        ],
        "days": {"Monday", "Wednesday", "Sunday"}
    },

    "12605": {
        "name": "Salem Express",
        "stops": [
            ("Chennai", "09:00", "09:10"),
            ("Salem", "12:00", "12:05"),
            ("Erode", "13:00", "13:10")
        ],
        "days": {"Monday", "Thursday", "Saturday"}
    }
}

station = input("Enter station: ")
day = input("Enter day: ")

results = []

for number, details in trains.items():
    if day in details["days"]:
        for stop in details["stops"]:
            if stop[0].lower() == station.lower():
                results.append(
                    (number, details["name"], stop[1], stop[2])
                )

# Sort using departure time
results = sorted(results, key=lambda x: x[3])

print("\nTrains stopping at", station, "on", day)

if results:
    for number, name, arrival, departure in results:
        print(number, name, "Arrival:", arrival,
              "Departure:", departure)
else:
    print("No trains found")

# Print complete timetable
print("\nComplete Timetable:")
for number, details in trains.items():
    print("\nTrain:", number, details["name"])
    print("Running days:", sorted(details["days"]))

    for station_name, arrival, departure in details["stops"]:
        print(station_name, arrival, departure)

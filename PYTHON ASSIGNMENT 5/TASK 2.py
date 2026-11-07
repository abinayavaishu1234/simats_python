
import pandas as pd

data = {
    "Station": ["Adyar", "Guindy", "Adyar", "Guindy",
                "Adyar", "Guindy", "Adyar"],
    "Date": ["2026-10-01", "2026-10-01", "2026-10-02",
             "2026-10-02", "2026-10-03", "2026-10-03",
             "2026-10-01"],
    "PM25": [48, 95, None, -5, 60, 121, 48],
    "Temperature": [30, 32, 29, 31, 86, 33, 30]
}

df = pd.DataFrame(data)

print("ORIGINAL DATASET")
print(df)

df = df.drop_duplicates()

df["PM25"] = df["PM25"].fillna(df["PM25"].median())

df = df[(df["PM25"] >= 0) & (df["PM25"] <= 1000)]

df.loc[df["Temperature"] > 50, "Temperature"] = (
    df.loc[df["Temperature"] > 50, "Temperature"] - 32
) * 5 / 9

minimum = df["PM25"].min()
maximum = df["PM25"].max()

if maximum != minimum:
    df["PM25_Normalised"] = (
        (df["PM25"] - minimum) / (maximum - minimum)
    ).round(3)
else:
    df["PM25_Normalised"] = 0

print("\nCLEANED AND NORMALISED DATASET")
print(df.to_string(index=False))

df.to_csv("cleaned_air_quality.csv", index=False)

print("\nCleaned data saved successfully!")
print("TASK 2 COMPLETED")

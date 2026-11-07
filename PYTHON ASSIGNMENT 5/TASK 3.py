
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_air_quality.csv")

print("AIR QUALITY DATASET")
print(df.to_string(index=False))

print("\nSTATISTICAL ANALYSIS")

print("Average PM2.5:", round(df["PM25"].mean(), 2))
print("Maximum PM2.5:", df["PM25"].max())
print("Minimum PM2.5:", df["PM25"].min())
station_avg = df.groupby("Station")["PM25"].mean()

print("\nSTATION-WISE AVERAGE PM2.5")
print(station_avg)
daily_avg = df.groupby("Date")["PM25"].mean()

print("\nDAILY AVERAGE PM2.5")
print(daily_avg)
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
daily_avg.plot(kind="line", marker="o", ax=axes[0, 0])
axes[0, 0].set_title("Daily PM2.5 Trend")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("PM2.5")
station_avg.plot(kind="bar", ax=axes[0, 1])
axes[0, 1].set_title("Station-wise PM2.5 Average")
axes[0, 1].set_xlabel("Station")
axes[0, 1].set_ylabel("Average PM2.5")
axes[1, 0].scatter(df["Temperature"], df["PM25"])
axes[1, 0].set_title("Temperature vs PM2.5")
axes[1, 0].set_xlabel("Temperature")
axes[1, 0].set_ylabel("PM2.5")
axes[1, 1].hist(df["PM25"], bins=5)
axes[1, 1].set_title("PM2.5 Distribution")
axes[1, 1].set_xlabel("PM2.5")
axes[1, 1].set_ylabel("Frequency")
plt.tight_layout()
plt.savefig("task3_charts.png")
plt.show()

print("\nCharts saved successfully!")
print("TASK 3 COMPLETED")

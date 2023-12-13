import csv
import matplotlib.pyplot as plt
from datetime import datetime

timestamps = []
temperatures = []

with open('weather.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        temperature  = float(row['Temperature'])
        timestamp_str = row['Timestamp']
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
        temperatures.append(temperature)
        timestamps.append(timestamp)

plt.figure(figsize=(18, 10))

plt.plot(timestamps, temperatures)

plt.xlabel('Time')
plt.ylabel('Temperature (C)')
plt.title('Temperature Over Time')
plt.ylim([0, 30])

plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d %H:%M'))

plt.xticks(rotation=45)

plt.show()

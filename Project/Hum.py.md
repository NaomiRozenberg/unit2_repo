```py 
import csv
import matplotlib.pyplot as plt
from datetime import datetime

timestamps = []
humidity = []

with open('weather.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        Humidity = float(row['Humidity'])
        timestamp_str = row['Timestamp']
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
        humidity.append(Humidity)
        timestamps.append(timestamp)

plt.figure(figsize=(10, 10))

plt.plot(timestamps, humidity)

plt.xlabel('Time')
plt.ylabel('Humidity (%)')
plt.title('Humidity Over Time')
plt.ylim([0, 50])

plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d %H:%M'))

plt.xticks(rotation=45)

plt.show()
```

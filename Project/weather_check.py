from datetime import datetime, timedelta
import csv
import serial
import time

arduino = serial.Serial(port='/dev/cu.usbserial-10', baudrate=9600, timeout=.1)


def read():
    data = ""
    while len(data) < 1:
        data = arduino.readline()
    return data


csv_file_path = 'weather.csv'
end_time = datetime.now() + timedelta(hours=48)

with open(csv_file_path, mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Temperature', 'Humidity', 'Timestamp'])

while datetime.now() < end_time:
    time.sleep(300)
    value = read()
    msg = value.decode('utf-8')

    if "Hello" not in msg:
        print(msg)
        hum, temp = msg.split(" ")
        temp = temp.split(":")[1][0:-3]
        hum = hum.split(":")[1][0:-1]

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(csv_file_path, mode='a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([temp, hum, timestamp])

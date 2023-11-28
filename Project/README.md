![11e470e9022f4fc5b367429bcbb285bc](https://github.com/comsci-uwc-isak/unit2_2023/assets/53995212/1d14b1d3-ae39-4ef3-8ec9-3329630eacae)

# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning

## Problem definition ##

Miu and Valery, two UWC ISAK students found a squirrel in the forest that is severely injured and sick. They kindly decided to take them home and monitor the situation. It's important to put the squirrel to a place where they are protected from danger. Also, they need a place with ideal temperature and humidity level for the squirrel to have a higher chance of survival. They decided to put the squirrel either in Miu's room (R1-11B) or Valery's room (R2-14A) as the rooms have heaters and air conditioning which improve the humidity and temperature. However, they still need to decide which exact room they'll put the squirrel in because even the tiny difference can deteriorate the squirrel's symptoms. Despite having a thermometer, Valery and Miu don't have a thorough understanding of the living conditions in their respective rooms: they can only check the temperature a few times a day, as the temperature is completely unknown to them while they sleep. Moreover, the lack of a tool that shows the graphical representation of the humidity and temperature makes them unsure about which room to put the squirrel. In order to make the right decision to save the squirrel's life, they need a tool that shows the humidity and temperature of the two rooms with graphs, in which other useful data such as mean, median, and mode are also being represented, with a comparison between two rooms to come to a conclusion on which room is better for the squirrel's recovery. With this tool, Valery and Miu are able to make the crucial decision to maximize the squirrel's chance of survival. 


## Proposed Solution ##
Considering the client requirements an adequate solution includes a low cost sensing device for humidity and temperature and a custom data script that process and anaysis the samples acquired. For a low cost sensing device an adequate alternative is the DHT11 sensor[^1] which is offered online for less than 5 USD and provides adequare precision and range for the client requirements (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). Similar devices such as the DHT22, AHT20 or the AM2301B [^2] have higher specifications, however the DHT11 uses a simple serial communication (SPI) rather than more eleborated protocols such as the I2C used by the alternatives. For the range, precision and accuracy required in this applicaiton the DHT11 provides the best compromise. Connecting the DHT11 sensor to a computer requires a device that provides a Serial Port communication. A cheap and often used alternative for prototyping is the Arduino UNO microcontroller [^3]. "Arduino is an open-source electronics platform based on easy-to-use hardware and software"[^4]. In additon to the low cost of the Arduino (< 6USD), this devide is programable and expandable[^1]. Other alternatives include diffeerent versions of the original Arduino but their size and price make them a less adequate solution.

Considering the budgetary constrains of the client and the hardware requirements, the software tool that I proposed for this solution is Python. Python's open-source nature and platform independence contribute to the long-term viability of the system. The use of Python simplifies potential future enhancements or modifications, allowing for seamless scalability without the need for extensive redevelopment [^5][^6]. In comparison to the alternative C or C++, which share similar features, Python is a High level programming language (HLL) with high abstraction [^7]. For example, memory management is automatic in Python whereas it is responsability of the C/C++ developer to allocate and free up memory [^7], this could result in faster applications but also memory problems. In addition a HLL language will allow me and future developers extend the solution or solve issues proptly.  

**Design statement**

We, Naomi and Dylan, will design and make a program that provides information of the temperature and huidity of two rooms, R1-11B and R2-14 represented in graphs along with other useful information such as standard deviation, mean, median, and mode. The information will be summarized and synthesized and a specific suggestion based on such information will be given in order to solve the problem defined above. DHT 11 sensor is used in this program in order to keep track of information on temperature and humidity. This progran is constructed with the software python, Arduino, and DHT 11 and will be evaluated by criteria A, B, and C. It takes around three weeks to be completed. 

## Success Criteria

[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 
[^2]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.   
[^3]:“How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  
[^4]:Team, The Arduino. “What Is Arduino?: Arduino Documentation.” Arduino Documentation | Arduino Documentation, https://docs.arduino.cc/learn/starting-guide/whats-arduino.  
[^5]:Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability Query Is Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. 
[^6]:Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. 
[^7]: Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management. 

1. The solution provides a visual representation of the Humidity and Temperature values inside a dormitory (Local) and outside the house (Remote) for a period of minimum 48 hours. 
1. ```[HL]``` The local variables will be measure using a set of 3 sensors around the dormitory.
2. The solution provides a mathematical modelling for the Humidity and Temperature levels for each Local and Remote locations. ```(SL: linear model)```, ```(HL: non-lineal model)```
3. The solution provides a comparative analysis for the Humidity and Temperature levels for each Local and Remote locations including mean, standad deviation, minimum, maximum, and median.
4. ```(SL)```The Local samples are stored in a csv file and ```(HL)``` posted to the remote server as a backup.
5. The solution provides a prediction for the subsequent 12 hours for both temperature and humidity.
6. The solution includes a poster summarizing the visual representations, model and analysis created. The poster includes a recommendation about healthy levels for Temperature and Humidity.

_TOK Connection: To what extent does ```the use of data science``` in climate research influence our understanding of environmental issues, and what knowledge questions arise regarding the ```reliability, interpretation, and ethical implications``` of data-driven approaches in addressing climate change_

1. How does our use of technology shape our understanding of the environment
2. What responsibilities do we have as technologists when it comes to handling personal data related to our living spaces?
3. What cultural and contextual factors might impact our interpretation of the results, especially when comparing our local readings with those from the campus? 

# Criteria B: Design

## System Diagram **SL**

![SL](https://github.com/comsci-uwc-isak/unit2_2023/assets/53995212/6161f2f6-67c5-4742-9961-e46475376370)

**Fig.1** shows the system diagram for the proposed solution (**SL**). The indoor variables will be measured using an Arduino microprocessor and one sensor DHT11 conencted to the local computer (Laptop) located inside a room. The outdoor variables will be requested to the remote server using a GET request to the API of the server at ```192.168.6.153/readings```. The local values are stored in a CSV database locally.



## Record of Tasks
| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
1|Write the Problem context|Problem definition|10min|Nov 25|A
2|Read proposed solution|Have a better understanding of what we have to do and write our design statement|10min|Nov 25|A
3|Begin coding to fullfill the needs of our clients|A code that will read the data collected by the arduino and the DHT11|15min|Nov 26|C
4|Make the code create and then append the data into two sepparate csv files|A file titled "weathear.csv" that store data in new lines|20min|Nov 26|C
5| Run our program in R1-11B | Measuring Humidity and temperature in R1-11B | 48H | Nov 26-27 |C| 
6|write the Design statement| Make the Design statement infotmetive| 10min| Nov 28| A 


## Test Plan

# Criteria C: Development

## List of techniques used

## Development
DHT11 sensor data collection from arduino

```py
import csv
import serial
import time

arduino = serial.Serial(port='/dev/cu.usbserial-10', baudrate=9600, timeout=.1)

def read():
    data = ""
    while len(data) < 1:
        data = arduino.readline()
    return data

Temperature = []
Humidity = []
Count = []

count = 0

while True:
    time.sleep(300)
    value = read()
    msg = value.decode('utf-8')

    if "Hello" not in msg:
        humidity_temp = msg.split(" ")
        h = humidity_temp[0]

        v_h = h.split(":")
        hum_value = float(v_h[1].strip("%"))

        t = humidity_temp[1]
        v_t = t.split(":")
        temp_value = float(v_t[1].strip("C\r\n"))

        Temperature.append(temp_value)
        Humidity.append(hum_value)
        count += 1
        Count.append(count)
        print(Temperature, Humidity, Count)

        if count == 144:
            csv_file_path = 'weather.csv'
            with open(csv_file_path, mode='w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(['Temperature', 'Humidity', 'Count'])
                csv_writer.writerows(zip(Temperature, Humidity, Count))

            print(f'Data has been written to {csv_file_path}')
            break
```

# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration

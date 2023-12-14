![11e470e9022f4fc5b367429bcbb285bc](https://github.com/comsci-uwc-isak/unit2_2023/assets/53995212/1d14b1d3-ae39-4ef3-8ec9-3329630eacae)

# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning

## Problem definition ##

John is a student at UWC ISAK Japan who is interested in growing plants. He recently found out that devil's ivy (epipremnum aureum) is a natural purifier, and he is in need of an inexpensive air purifier for the smelly room. However, this plant is very sensitive to its surroundings: the leaves will turn yellow and it will eventually die if the moisture, temperature or sunligh level is not appropriate for its growth. John doesn't know where to grow it. He has two options: the room or outside[the place where the api sensor is]. He is very indecisive as he doesn't know the difference in temperature or humidity of these two places. He has a thermometer, but it only gives him a glimpse of the temperature in the locations, while he can't see the comparison of the two places or the changing pattern in a few days, and the data is completely unknown to him while he sleeps. To make a decision, John needs a comprehensive set of data, including temperature, humidity, and other useful information such as standard deviation, mode, median, mean, etc. He desperately craves a tool that provides him with these information, with the comparison between the two places and graphs that visualize the humidity, temperature and the changing pattern. 


## Proposed Solution ##
Considering the client requirements an adequate solution includes a low cost sensing device for humidity and temperature and a custom data script that process and anaysis the samples acquired. For a low cost sensing device an adequate alternative is the DHT11 sensor[^1] which is offered online for less than 5 USD and provides adequare precision and range for the client requirements (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). Similar devices such as the DHT22, AHT20 or the AM2301B [^2] have higher specifications, however the DHT11 uses a simple serial communication (SPI) rather than more eleborated protocols such as the I2C used by the alternatives. For the range, precision and accuracy required in this applicaiton the DHT11 provides the best compromise. Connecting the DHT11 sensor to a computer requires a device that provides a Serial Port communication. A cheap and often used alternative for prototyping is the Arduino UNO microcontroller [^3]. "Arduino is an open-source electronics platform based on easy-to-use hardware and software"[^4]. In additon to the low cost of the Arduino (< 6USD), this devide is programable and expandable[^1]. Other alternatives include diffeerent versions of the original Arduino but their size and price make them a less adequate solution.

Considering the budgetary constrains of the client and the hardware requirements, the software tool that I proposed for this solution is Python. Python's open-source nature and platform independence contribute to the long-term viability of the system. The use of Python simplifies potential future enhancements or modifications, allowing for seamless scalability without the need for extensive redevelopment [^5][^6]. In comparison to the alternative C or C++, which share similar features, Python is a High level programming language (HLL) with high abstraction [^7]. For example, memory management is automatic in Python whereas it is responsability of the C/C++ developer to allocate and free up memory [^7], this could result in faster applications but also memory problems. In addition a HLL language will allow me and future developers extend the solution or solve issues proptly.  

**Design statement**

We, Naomi and Dylan, will design and make a program that provides information of the temperature and huidity of the specimen room, R1-11B represented in graphs along with other useful information such as standard deviation, mean, median, mode, minimum, and maximum. The information will be summarized and synthesized and a specific suggestion based on such information will be given in order to solve the problem defined above. DHT 11 sensor is used in this program in order to keep track of information on temperature and humidity. The data is recorded every 5 minutes in 48 hours, and will be saved in a local file. After that, we will compare the two sets of data: indoor and outdoor, to give a suggestion on where John should grow devil's ivy based on the information illustrated by graphs. A prediction of the patterns of temperature and humidity in the future will be given as well. This progran is constructed with the software python, Arduino, and DHT 11 and will be evaluated by criteria A, B, and C. It takes around three weeks to be completed. 

## Success Criteria

[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 
[^2]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.   
[^3]:“How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  
[^4]:Team, The Arduino. “What Is Arduino?: Arduino Documentation.” Arduino Documentation | Arduino Documentation, https://docs.arduino.cc/learn/starting-guide/whats-arduino.  
[^5]:Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability Query Is Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. 
[^6]:Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. 
[^7]: Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management.
[^8]: Taken from stack overflow https://stackoverflow.com/questions/42504295/python-datetime-over-one-day
[^9]: Taken from python programming https://www.programiz.com/python-programming/datetime/strftime

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

# Criteria B: Design #

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
5|write the Design statement| Make the Design statement infotmetive| 10min| Nov 28| A 
6| Run our program in R1-11B | Measuring Humidity and temperature in R1-11B |48H | Nov 30 - Dec 2 |C| 
7| Make a program to extract the temperature information from weather.csv (Temp.py)|The information will be used for Graphing| 20min|Dec 9|C|
8| Make a program to extract the humidity information from weather.csv (Hum.py)|The information will be used for Graphing |20min|Dec 9 |C|
9| Make a program to get sensor ID numbers from the Api (libApi.py)|This will help know which API outdoor sensors we are using|30min|Dec 10|C|
10| Make a program which makes a list per each sensor, with all its values and unit (weather_reader.py)|The information will be used for Graphing |30min|Dec 11|C|
11| Make 3 flow diagrams to represent 3 diffrent algorithms in the project|Present what the code dose in a simple way so the customer understands how the code works|2H|Dec 11|B|
12| Make a test plan for the project| Outline how we would test the code to make sure it works|2H|Dec 12 |B|



## Test Plan

| Test No. | Test type           | Input                                                    | Process                                                                                                                      | Expected output                                                                                                                         |
|----------|---------------------|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| 1        | Unit testing        | Arduino connected to the computer,  weather_check code.  | 1, open weather_check.py 2, run the code                                                                                     | 'Hello' should be printed as the program starts running to indicate that the sensor is  successfully connected.                         |
| 2        | Performance testing | weather_check code.                                      | 1, connect arduino and sensor 2, run the code                                                                                | The temperature and humidity  should be recorded every 5  minutes and stored in weather.csv The sensor should respond without lagging.  |
| 3        | Integration testing | weather.csv                                              | 1, open weather.csv 2, check if all data are recorded in the correct format                                                  | Data is recorded in the correct format (temperature, humidity, timestamp) and is complete (there should be 48*12 lines of data).        |
| 4        | Unit testing        | All codes for graphs                                     | 1, run the codes                                                                                                             | Diagrams that are correctly labelled, with the correct titles and curves. All curves are smoothed.                                      |
| 5        | Integration testing | http://192.168.6.153/readings                            | 1, visit http://192.168.6.153/readings                                                                                       | The readings contain all the data from all sensors that we need for graphing.                                                           |
| 6        | Unit testing        | The code for indoor temperature                          | 1, run the code                                                                                                              | Correct diagram is showed.                                                                                                              |
| 7        | Unit testing        | The code for outdoor temperature                         | 1, run the code                                                                                                              | Correct diagram is showed.                                                                                                              |
| 8        | Unit testing        | The code for indoor humidity                             | 1, run the code                                                                                                              | Correct diagram is showed.                                                                                                              |
| 9        | Unit testing        | The code for outdoor humidity                            | 1, run the code                                                                                                              | Correct diagram is showed.                                                                                                              |
| 10       | Code review         | All Code                                                       | 1, check if the code has  adequate comments, variables  are correctly named, and the  code runs smoothly without any error.  | The code includes comments explaining what is happening. All variables are  correctly named to help understand what they represent.     |
| 11       |                     |                                                          |                                                                                                                              |                                                                                                                                         |



## FlowCharts
<img width="390" alt="Screenshot 2023-12-13 at 15 06 26" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/c52a7faf-5805-4ec3-8484-b9a7d54bc4a3">

**Fig.2** Shows the algorithm of Hum.py. Which extracts Humidity information from weather.csv, and Graphs the information with formatted X-ticks timestamps.

<img width="465" alt="Screenshot 2023-12-13 at 15 02 09" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/4f968cf9-7fa7-45eb-baf5-c1522f6a7729">

**Fig.3** Shows the algorithm of libApi.py. Which filters out sensors with any owner_id that is not 1. and removs sensor 3 due to the fact that it is broken.

<img width="378" alt="Screenshot 2023-12-13 at 15 02 42" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/9bf41696-8948-461c-b4ac-8e60b19fa034">

**Fig.4** Shows the algorithm of weather_check.py. Which measures the temperature and the humidity every 5 minutis for 48 hours and writes the clues in a csv in addition to a time stamp to follow up on the timing. 

## How data is stored ##

We store temperature and humidity data recorded from the sensor to a local csv file called "weather.csv".

In the python file "weather_check.py" the file was first opened, and we used the writerow method to write a new row whenever there's new data recorded. They all follow the format (temperature, humidity, time).

```.py

with open(csv_file_path, mode='a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([temp, hum, timestamp])

```

# Criteria C: Development

## List of techniques used

1. Functions
2. For loop
3. While loop
4. if statement
5. Generating grpahs with matplotlib
6. API Requests
7. Timing
8. writing rows in a csv file
9. read data from a csv file
10. calculate the mean, median, and standard deviation of a set of data
11. smoothing a graph using smoothing function

## Existing tools used

| Software tool  | Coding structure tools | Libraries  |
|----------------|------------------------|------------|
| Python/Pycharm | For loop               | matplotlib |
|                | While loop             | datetime   |
|                | API requests           | requests   |
|                |                        | numpy      |
|                |                        |            |   




## Development


Below are what we developed to fulfil the client's success criteria.


## 1. The solution provides a visual representation of the Humidity and Temperature values inside a dormitory (Local) and outside the house (Remote) for a period of minimum 48 hours. 

To fulfil this requirement, we need both indoor and outdoor data recorded every five minutes in 48 hours, which include values of humidity and temperature, as well as time. For outdoor (remote) data, there are three sensors (id 0, id 1, id 2) for temperature and two (id 4, id 5) for humidity. In order to compare these data, we calculated the mean for three temperature sensors and two humidity sensors, and respectively compared these two curves to the indoor temperature stored in the local csv file. 

To achieve this, we defined a function called get_readings which extracts the readings from the api server which has the recordings of the outdoor data of humidity and termperature. 

```.py

def get_readings(ip: str = '192.168.6.153'):
    data = requests.get(f'http://{ip}/readings')
    data = data.json()
    x = data['readings'][0]
    return x

```




Considering that different sensors represent different kinds of data (temperature and humidity), we realized that we need a function to get a set of data specifically from one sensor in order to calculate the mean and compare with the indoor data. 

```.py

def get_sensors(ids: list() = [1, 2]):
    recordings = get_readings()
    my_sensors = {}
    for i in ids:
        my_sensors[i] = []
    for rec in recordings:
        id_sensor = rec['sensor_id']
        if id_sensor in ids:
            value = rec['value']
            my_sensors[id_sensor].append(value)
    return my_sensors

```



Additionally, the client needs a clear graphical representation of data that helps him visualize the data. To achieve this, we designed a code that makes a curve smooth in a graph. 
First, we defined a function name "smoothing" with the two parameters, values which is a list and size_window which has the default value of 5. After initializing two empty lists, x and y, we used a for loop to calculate the mean of the current value of size_window and i, and append them to x and y respectively. After the loop ends, x and y are returned as smoothed values. With this function, the client is able to better understand a curve in a graph. 

```.py

def smoothing(values: [], size_window: int = 5):
    x = []
    y = []
    for i in range(0, len(values), size_window):
        window_mean = sum(values[i:i + size_window])/size_window
        y.append(window_mean)
        x.append(i)
    return x, y

```





<img width="570" alt="Screenshot 2023-12-14 at 4 01 30" src="https://github.com/NaomiRozenberg/unit2_repo/assets/144768397/ba3a21e5-ed4f-49fa-8791-cec8a6b161d1">

This graph is an example of how we calculate the average value from multiple sensors using the functions above. It's also worth noting that the curves are smoothed using the smoothing function. 




```.py

for reading_hum in p:
    if reading_hum['sensor_id'] in hum:
        print(reading_hum)
        print(reading_hum['value'])

        if 12760 <= int(reading_hum['id']) <= 21089:
            if int(reading_hum['sensor_id']) == 4:
                hum_48hrs_data_id4.append(reading_hum['value'])
                datetime_string = reading_hum['datetime']
            else:
                hum_48hrs_data_id5.append(reading_hum['value'])
```
We designed this code to specify the timespan that we need for humidity. We chose the same timespan as the indoor data for a more precise and meaningful comparison. 





With the assistance of these functions that we defined, we can now compare all data and provide the client with a clear graphical representation of the humidity and temperature indoor and outdoor. 

<img width="601" alt="Screenshot 2023-12-14 at 11 23 44" src="https://github.com/NaomiRozenberg/unit2_repo/assets/144768397/187965a0-5441-489b-8527-f89dd17c7158">
This is the comparison between indoor and outdoor humidity





Similarly, we compared the average outdoor temperature with the indoor temperature. 


<img width="585" alt="Screenshot 2023-12-14 at 11 30 31" src="https://github.com/NaomiRozenberg/unit2_repo/assets/144768397/64a4c26f-ff10-4f62-9d64-53834e10147b">



Note that all data have been recorded in the same time period, 2023-11-30 20:00 to 2023-12-2 20:00. 48 hours in total. 

## 2. The solution provides a mathematical modelling for the Humidity and Temperature levels for each Local and Remote locations. ```(SL: linear model)```, ```(HL: non-lineal model)```and The solution provides a prediction for the subsequent 12 hours for both temperature and humidity.
## The solution provides a comparative analysis for the Humidity and Temperature levels for each Local and Remote locations including mean, standad deviation, minimum, maximum, and median.
##  ```(SL)```The Local samples are stored in a csv file and ```(HL)``` posted to the remote server as a backup.

#### check_weather.py

The next 2 pieces of code are taken from weather_check.py which collects data from DHT11 sensor connected to the arduino. We connected the sensor on the arduino and used it to record the temperature and humidity. 

This part defines when to end the program, using datetime and tinedelte methodes[^8]. We used writeline function to store the data and time (every 5 minutes) into a local csv file named "weather.csv". 

```.py
end_time = datetime.now() + timedelta(hours=48)
while datetime.now() < end_time:
    time.sleep(300)
    value = read()
    msg = value.decode('utf-8')
```

This part defines the timestamp, which helps track when the measurement was taken [^9]. 
```.py
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```
This image proves the collation of data to the csv file was successful 
<img width="1470" alt="Screenshot 2023-12-13 at 20 06 15" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/ec1a8122-1525-4111-9e9c-d6bbe10aa071">



### Computational thinking

# Criteria D: Functionality
## The solution includes a poster summarizing the visual representations, model and analysis created. The poster includes a recommendation about healthy levels for Temperature and Humidity.

<img width="800" alt="Screenshot 2023-12-14 at 12 46 42" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/3a092b67-e428-466a-8d07-2b29f0baa55d">

A 7 min video demonstrating the proposed solution with narration

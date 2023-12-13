import requests

api_endpoint = 'http://192.168.6.153/sensors'
response = requests.get(api_endpoint)
data = response.json()
owner_id_1_sensors = [sensor for sensor_list in data['readings']
                      for sensor in sensor_list if sensor['owner_id'] == 1]
print(data)
unit_list = []
sensor_ids = []
for sensor in owner_id_1_sensors:
    if not sensor['name'] == 'sensor_3':
        sensor_ids.append(sensor['name'])
        unit_list.append(sensor['unit'])
sensor_ids = [int(sensor.split('_')[1]) for sensor in sensor_ids]
if 3 in sensor_ids:
    sensor_ids.remove(3)

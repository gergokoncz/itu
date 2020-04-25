from influxdb import InfluxDBClient

client = InfluxDBClient(host = 'influxus.itu.dk', port = 8086, username = 'lsda', password = 'icanonlyread')
client.switch_database('orkney')

measurements = client.get_list_measurements()

print('Measurements:\n', measurements)

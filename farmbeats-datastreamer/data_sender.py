import paho.mqtt.publish as pub



def send_data(data_string):
    pub.single("test",data_string,hostname = "172.22.32.140:1880")

def format_to_json(data_string):
    data = data_string.split(',')
    json_string = "{"
    json_string += "data_from:Chris,"
    json_string += "date_time:" + data[0] + ","
    json_string += "soil_temperature:" + data[1] + ","
    json_string += "soil_moisture:" + data[2] + ","
    json_string += "air_temperature:" + data[3] + ","
    json_string += "air_humidity:" + data[4] + ","
    json_string += "sunlight_visible:" + data[5] + ","
    json_string += "sunlight_uv:" + data[6] + ","
    json_string += "sunlight_ir:" + data[7] + ","
    json_string += "relay:" + data[7] + ","
    json_string += "button:" + data[8] + "}"
    
    return json_string

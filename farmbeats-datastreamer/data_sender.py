from paho.mqtt import client, publish as client, publish
import time

#fil = open("serverIP.txt",'r')
server_ip = "172.22.32.140"
topic = "test"
payload = "Test from Chris's pi"
def send_data(data):
    #print(server_ip)
    publish.single(topic, payload=data, hostname=server_ip)

def format_csv_string(dataString):
    data = dataString.split(',')
    json_data = "{"
    json_data+="date_time:"+str(time.time())+","
    json_data+="soil_temp:"+str(data[1])+","
    json_data+="soil_moisture:"+str(data[2])+","
    json_data+="air_temp:"+str(data[3])+","
    json_data+="air_humidity:"+str(data[4])+","
    json_data+="sunligh_visible:"+str(data[5])+","
    json_data+="sunlight_uv:"+str(data[6])+"}"
        #'sunlight_ir':data[7]
        #'relay':
        #'button':
        #'logger_status':
        #'agent_configuration_set':
        #'agent_state':

    return json_data

def main():
    while True:
        send_data()
        time.sleep(5)

if __name__=="__main__":
    main()
# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
import json
# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("myClientID3")
# For Websocket connection
# myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
# Configurations
# For TLS mutual authentication
myMQTTClient.configureEndpoint("a1iq12e8p3g3m2-ats.iot.eu-west-1.amazonaws.com", 8883)
# For Websocket
# myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
# For TLS mutual authentication with TLS ALPN extension
# myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
myMQTTClient.configureCredentials("AmazonRootCA1.pem", "06efe1629b-private.pem.key", "06efe1629b-certificate.pem.crt")
# For Websocket, we only need to configure the root CA
# myMQTTClient.configureCredentials("YOUR/ROOT/CA/PATH")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
part_num=[]
list_p=[]
def json_list(list):
    lst = []
    for pn in list:
        d = {}
        d['mpn']=pn
        lst.append(d)
    return json.dumps(lst)

def customCallback(client, userdata, message):
    print(message)
    print(message.payload)
    print("start")
    file=open("data.txt",'w')
    file.write(message.payload)
#    file.write("\n")
    file.close()
    #print (json_list(part_nums))

myMQTTClient.connect()
# myMQTTClient.publish("trial", "{temperature:20, cpu:30}", 0)
while(1):
 myMQTTClient.subscribe("trial", 1, customCallback)
 time.sleep(2)

# myMQTTClient.unsubscribe("trial")
# myMQTTClient.disconnect()

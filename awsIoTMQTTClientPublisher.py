# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import random
import time
# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("myClientID1")
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
# def customCallback(client, userdata, message):
#     print(message)
#     print(message.payload)
#     file = open("data.txt", 'a')
#     file.write(message.payload)
#     file.write("\n")
#     file.close()

myMQTTClient.connect()
while(1):
 val = random.randrange(30, 60)
 myMQTTClient.publish("trial", "{device1:{temperature:"+str(val)+"}}", 0)
 time.sleep(5)
# while(1):
#  myMQTTClient.subscribe("trial", 1, customCallback)
#  time.sleep(2)

# myMQTTClient.unsubscribe("trial")
myMQTTClient.disconnect()

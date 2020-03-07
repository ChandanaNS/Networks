#author: chandana
#Topic: End to end IoT network system using AWS

To publish a topic from any device like a PC to an AWS IoT broker, a script has been written using the AWSIoTMQTTClient package.

The package is available in https://github.com/aws/aws-iot-device-sdk-python

In the script MQTTClient instance has been created and an endpoint has been configured (Endpoint is available in AWS IoT, setting) with standard MQTT port number 8883. 

The corresponding certificates are attached to the configureCredentials method in the script. 
The MQTT client has been connected with a topic, and the JSON has been published and then the client has to be disconnected.

For the above use case the subscriber and publisher script has been attached in this repository.

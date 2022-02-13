from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder

class MQTTConnectionProvider:
    _ENDPOINT = "a2ew9sszuocgvp-ats.iot.eu-central-1.amazonaws.com"
    _CLIENT_ID = "RaspberryPi"
    _PATH_TO_CERTIFICATE = "/home/pi/AWSIoT/certificate.pem.crt"
    _PATH_TO_PRIVATE_KEY = "/home/pi/AWSIoT/private.pem.key"
    _PATH_TO_AMAZON_ROOT_CA_1 = "/home/pi/AWSIoT/AmazonRootCA1.pem"

    def __init__(self):
        self.event_loop_group = io.EventLoopGroup(1)
        self.host_resolver = io.DefaultHostResolver(self.event_loop_group)
        self.client_bootstrap = io.ClientBootstrap(self.event_loop_group, self.host_resolver)
        self.mqtt_connection = mqtt_connection_builder.mtls_from_path(
                    endpoint=self._ENDPOINT,
                    cert_filepath=self._PATH_TO_CERTIFICATE,
                    pri_key_filepath=self._PATH_TO_PRIVATE_KEY,
                    client_bootstrap=self.client_bootstrap,
                    ca_filepath=self._PATH_TO_AMAZON_ROOT_CA_1,
                    client_id=self._CLIENT_ID,
                    clean_session=True,
                    keep_alive_secs=5
                    )
        print("Connecting to endpoint {} with clientId '{}'".format(
                self._ENDPOINT, self._CLIENT_ID))

        connect_future = self.mqtt_connection.connect()
        connect_future.result()

    def cleanup(self):
        disconnect_future = self.mqtt_connection.disconnect()
        disconnect_future.result()
    
    def publish(self, _topic, message):
        self.mqtt_connection.publish(topic=_topic, payload=message, qos=mqtt.QoS.AT_LEAST_ONCE)
        print(_topic + ": " + message)
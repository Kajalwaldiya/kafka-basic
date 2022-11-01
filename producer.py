from kafka import KafkaProducer
import json

class MessageProducer:
    broker = ""
    topic = ""
    producer = None

    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=self.broker,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        acks='all',
        retries = 3)


    def send_msg(self, msg):
        print("sending message...")
        try:
            future = self.producer.send(self.topic,msg)
            self.producer.flush()
            future.get(timeout=60)
            print("message sent successfully...")
            return {'status_code':200, 'error':None}
        except Exception as ex:
            return ex


broker = 'localhost:9092'
topic = 'first_topic.'
message_producer = MessageProducer(broker,topic)


import json
import base64

data = {'name':'name1.jpeg'}
with open('test101.png', mode='rb') as file:
    img = file.read()
data['img'] = base64.encodebytes(img).decode('utf-8')

resp = message_producer.send_msg(data)
print(resp)
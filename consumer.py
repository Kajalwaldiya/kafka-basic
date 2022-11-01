# Import KafkaConsumer from Kafka library
from kafka import KafkaConsumer
import json
# Import sys module
import sys
import base64
import os
# Define server with port
bootstrap_servers = ['localhost:9092']

# Define topic name from where the message will recieve
topicName = 'first_topic.'

# Initialize consumer variable
consumer = KafkaConsumer (topicName, group_id ='group1',bootstrap_servers =
   bootstrap_servers, value_deserializer=lambda m: json.loads(m.decode('utf-8')))

data_dir = os.path.join(os.getcwd(), "data")
# data_dir = r"C:\Users\Kajal\Documents\KJ\A\kafka_try\data"

# Read and print message from consumer
for msg in consumer:
    with open(data_dir+"\\"+msg.value['name'], mode='wb') as file:
        file.write(base64.b64decode(msg.value['img']))
    print('{} File saved'.format(msg.value['name']))

# Terminate the script
sys.exit()
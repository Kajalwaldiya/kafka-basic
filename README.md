# kafka-basic
Sends a image payload from producer to consumer
Convert image files as JSON payload and then save it to another folder in the system.

The images are stored in data folder in current working directory.


Steps:
1. Install kafka https://kafka.apache.org/downloads
2. Extract to the contents
3. open server.properties inside kafka_xx/config,
 - add these listeners=PLAINTEXT://:9092
           - listeners=PLAINTEXT://:9092
           - log.dirs=xxx\kafka_logs\server_logs
  - and save the file
4. open zookeeper.properties inside kafka_xx/config
- and add dataDir=xxx\kafka_logs\zookeeper
5. start zookeeper: bin\windows\zookeeper-server-start.bat config\zookeeper.properties
6. start kafka server: bin\windows\kafka-server-start.sh config\server.properties
7. create topic : kafka_xx\bin\window\kafka-topics.bat --bootstrap-server localhost:9092 --topic first_topic --create --partitions 3 --replication-factor 1
8. pip3 install kafka-python
9. Producer.py : publishes message/data to topic
   - file_path = "image path"
   - topic = "first_topic "
10. consumer.py: consumes message from topic 
    - topicName = 'first_topic.'
11. create folder data in the working directory.
12. Run both producer.py and consumer.py


  

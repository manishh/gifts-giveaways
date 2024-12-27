from kafka import KafkaProducer  

# Kafka configuration  
bootstrap_servers = ["localhost:9092"]  
topic = "orders"  

# Initialize the Kafka producer  
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)  

# Send 10 messages to the topic  
for i in range(10):  
    ack = producer.send(topic, f'Order #{i+1}'.encode())
    metadata = ack.get()  # Get metadata for confirmation  
    # Optionally, you can access metadata.topic and metadata.partition here  

print("Produced 10 orders.")  

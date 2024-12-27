from kafka import KafkaConsumer  
import sys  

# Kafka configuration  
bootstrap_servers = ["localhost:9092"]  
topic = "orders"  

# Initialize the Kafka consumer  
consumer = KafkaConsumer(  
    topic,  
    group_id="group1",  
    bootstrap_servers=bootstrap_servers,  
    auto_offset_reset="earliest"  # Start reading from the earliest available message  
)  

try:  
    print("Consumer reading messages...")  
    for message in consumer:  
        print(f"\t{message.topic}: {message.partition}:{message.offset}: key={message.key} value={message.value}")
        
except KeyboardInterrupt:  
    print("Consumer exit.")  
    sys.exit()  

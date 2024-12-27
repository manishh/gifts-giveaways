from kafka import KafkaConsumer, KafkaProducer
import sys

# Kafka configuration
bootstrap_servers = ["localhost:9092"]
input_topic = "input_orders"
output_topic = "processed_orders"

def stream_processing():
    # Initialize Consumer to read from the input topic
    consumer = KafkaConsumer(
        input_topic,
        bootstrap_servers=bootstrap_servers,
        group_id="streaming_app_group",
        auto_offset_reset="earliest",
    )

    # Initialize Producer to write to the output topic
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    print("\nStreaming application started...")

    try:
        for message in consumer:
            transformed_value = f"{message.value.decode()} - processed"
            # Send the transformed message to the output topic
            producer.send(output_topic, transformed_value.encode())
            print(f"Processed: {message.value.decode()} -> {transformed_value}")
    except KeyboardInterrupt:  
        print("nStreaming application exit.")  
        sys.exit()  

if __name__ == "__main__":
    stream_processing()
from kafka import KafkaProducer
import time

# Kafka configuration
bootstrap_servers = ["localhost:9092"]
input_topic = "input_orders"

def produce_orders():
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    print("Creating sample input orders...")
    # Use higher number to observe streaming application demo better
    for i in range(1, 11):
        message = f"Order #{i}"
        producer.send(input_topic, message.encode())
        print(f"Produced: {message}")
        time.sleep(0.5)  # Simulate delay between messages
    print("Order creation completed.")

if __name__ == "__main__":
    produce_orders()

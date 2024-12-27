# Introduction to Apache Kafka Messaging System

- This code is provided _"as-is"_ to accompany to the tutorial: Introduction to Apache Kafka Messaging System. You must be familiar with Docker, Kafka, and Python to run this demo code.
- The Python code assumes that you are running Kafka+Zookeeper via Docker. You may use the provided docker file `docker-compose.yml` to set it up in your Docker.
- You may refer to following Python files for example code:
  1. `producer.py` - Minimal Python code to run a Kafka producer, it connects to Kafka on `localhost:9092` and sends messages to the topic: `orders`.
  2. `consumer.py` - Minimal Python code to run the associated Kafka consumer, it connects to Kafka on `localhost:9092` and reads messages from the topic: `orders`. 
  3. `order_producer.py` - This is a producer that produces data for streaming application, by sending "orders" to the topic: `input_orders`.
  4. `streaming_application.py` - This example code demonstrates a Kafka streaming application by reading messages continuously from the topic `input_orders`, processing them, and then sending them to the topic `processed_orders` for further processing. 

## Usage

Follow these steps sequentially for Kafka Streaming Application demo.

1. Create virtual environment an install _kafka-python_: `pip install kafka-python`. Use this virtual environment for running the code. 
2. Run Streaming application using: `python streaming_application.py` - this will run a consumer that reads messages from the topic `input_orders`.
3. Run order producer to create input orders: `python order_producer.py` - this will create 10 input orders for the streaming application demo. You can change the number in code for a longer demo.

---

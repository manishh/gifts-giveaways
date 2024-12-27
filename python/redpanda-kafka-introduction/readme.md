# Introduction to Apache Kafka Messaging System

This demo code is provided _"as-is"_ to accompany the tutorial **Introduction to Apache Kafka Messaging System**. To run this code successfully, you should have prior experience with **Docker**, **Kafka**, and **Python**.

### Prerequisites

- The Python scripts assume Kafka and Zookeeper are running in Docker containers. Use the provided `docker-compose.yml` file to set them up.
- The following Python files are included as examples:

  1. **`producer.py`**  
     A minimal Kafka producer that connects to Kafka on `localhost:9092` and sends messages to the topic `orders`.

  2. **`consumer.py`**  
     A minimal Kafka consumer that connects to Kafka on `localhost:9092` and reads messages from the topic `orders`.

  3. **`order_producer.py`**  
     A Kafka producer that generates "orders" for a streaming application, sending them to the topic `input_orders`.

  4. **`streaming_application.py`**  
     Demonstrates a Kafka streaming application by:
     - Continuously reading messages from the topic `input_orders`.
     - Processing the messages (by appending `- processed` to each order).
     - Sending the processed data to the topic `processed_orders`.

---

## Usage Instructions for Kafka Streaming Application

Follow these steps to run the Kafka Streaming Application demo:

1. **Set up a Python environment**  
   - Create a virtual environment.  
   - Install the required library:  
     ```bash
     pip install kafka-python
     ```
   - Use this virtual environment to run the demo scripts.

2. **Run the Streaming Application**  
   Start the Kafka streaming application by executing:  
   ```bash
   python streaming_application.py
   ```  
   This script will act as a consumer, reading messages from the topic `input_orders`.

3. **Generate Input Orders**  
   Produce test data for the streaming application by running:  
   ```bash
   python order_producer.py
   ```  
   This script will create 10 sample "orders" and send them to the topic `input_orders`.  
   *Tip:* You can modify the script to generate more orders for a longer demo.

---

> **Kafka Demo:** Manish Hatwalne (December 2024)

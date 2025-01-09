# Introduction to Apache Kafka Messaging System

This demo code is provided _"as-is"_ to accompany the tutorial **Introduction to Apache Kafka Messaging System**. To run this code successfully, you should have prior experience with **Docker**, **Kafka**, and **Python**.

### Prerequisites

- The Python scripts assume Kafka (with Zookeeper o KRaft) is running in Docker containers. Use the provided `docker-compose.yml` file to set them up.
- The following Python files are included as examples:

  1. **`producer.py`**  
     A minimal Kafka producer that connects to Kafka on `localhost:9092` and sends messages to the topic `orders`.

  2. **`consumer.py`**  
     A minimal Kafka consumer that connects to Kafka on `localhost:9092` and reads messages from the topic `orders`.

---

## Running Kafka Producer and Consumer

Follow these steps to run the Kafka Streaming Application demo:

1. **Set up a Python environment**  
   - Create a virtual environment.  
   - Install the required library:  
     ```bash
     pip install kafka-python
     ```
   - Use this virtual environment to run the demo scripts.

2. **Running Kafka Consumer**  
   Run sample Kafka consumer by executing:  
   ```bash
   python consumer.py
   ```  
   This script will read messages from the topic `orders` until interrupted by `CTRL+C`.

3. **Running Kafka Producer**  
   Produce test data for the consumer by running:  
   ```bash
   python producer.py
   ```  
   This script will create 10 sample "orders" and send them to the topic `orders`.  
   *Tip:* You can modify the script to generate more orders for a longer demo.

---


> **Kafka Demo:** Manish Hatwalne (December 2024)

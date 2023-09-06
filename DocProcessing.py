import json

from kafka import KafkaConsumer
from kafka import KafkaProducer
from utils import preprocess_text, coreferencing

DATA_KAFKA_TOPIC = "raw_data"
DATA_RECIEVED_KAFKA_TOPIC = "processed_data"

consumer = KafkaConsumer(
    DATA_KAFKA_TOPIC,
    bootstrap_servers="localhost:9092"
)
producer = KafkaProducer(bootstrap_servers="localhost:9092")

print("Gonna start listening raw data")
cnt =0
while True:
    for message in consumer:
        cnt+=1
        print("Ongoing transaction..")
        consumed_message = json.loads(message.value.decode())
        print(consumed_message)
        user_id = consumed_message["doc_id"]
        clean_data = consumed_message["data"]
        clean_data = preprocess_text(clean_data)
        coref_data = coreferencing(clean_data)
        data = {
            "customer_id": user_id,
            "cleaned_data": coref_data + f"tom_{cnt}",
        }
        print("Successful transaction..")
        producer.send(DATA_RECIEVED_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))

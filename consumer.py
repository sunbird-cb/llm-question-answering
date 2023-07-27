from kafka import KafkaConsumer
import json
import time 

consumer1 = KafkaConsumer(
        "document_data",
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id="Group1_docs")

consumer2 = KafkaConsumer(
        "processed_data",
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id="Group1_processed")


if __name__ == "__main__":
    consumer1 = KafkaConsumer(
        "document_data",
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id="Group1_docs")
    print("starting the consumer")
    for msg in consumer1:
        print("Registered User = {}".format(json.loads(msg.value)))
        time.sleep(1)

    consumer2 = KafkaConsumer(
        "processed_data",
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id="Group1_processed")
    print("starting the consumer")
    for msg in consumer2:
        # is text ko ingest krna hai Database me
        print("Registered User = {}".format(json.loads(msg.value)))
        time.sleep(1)
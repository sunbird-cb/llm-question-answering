from kafka import KafkaProducer
import json
from dataGen import create_metadata
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    while True:
        doc_data = create_metadata()
        print(doc_data)
        producer.send("document_data", doc_data)
        time.sleep(1)

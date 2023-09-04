import json
from utils import vdb
from kafka import KafkaConsumer

DATA_RECIEVED_KAFKA_TOPIC = "processed_data"

consumer = KafkaConsumer(
    DATA_RECIEVED_KAFKA_TOPIC, 
    bootstrap_servers="localhost:9092"
)

print("Gonna start listening processed data")

ingest_data = ""

all_chunks = []
cnt = 0
while True:
    for message in consumer:
        cnt+=1
        print("Updating processed..")
        consumed_message = json.loads(message.value.decode())
        final_data = consumed_message["cleaned_data"]
        all_chunks.append(final_data)
        if(cnt%10==0):
            vdb(all_chunks)
            print("ingested!")
        print(f"final data: {final_data}")
        print(f"all_chunks data len: {len(all_chunks)}")



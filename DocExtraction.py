
import time, json
from utils import get_pdf_text, get_text_chunks
from kafka import KafkaProducer

DATA_KAFKA_TOPIC = "raw_data"
ORDER_LIMIT = 20
PATH = "docs/sunbird_about_us.pdf"

text = get_pdf_text(PATH)
chunks = get_text_chunks(text)

Count = len(chunks)
producer = KafkaProducer(bootstrap_servers="localhost:9092")

print("Going to be generating order after 1 seconds")
print("Will generate one unique order every 1 seconds")
time.sleep(1)

for i in range(0, Count):
    data = {
        "doc_id": i,
        "data" : chunks[i]
    }

    producer.send(DATA_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
    print(f"Done Sending..{i}")
    time.sleep(1)

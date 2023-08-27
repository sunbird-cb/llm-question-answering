from kafka import KafkaProducer, KafkaConsumer
import json
from MilvusDB import *


# Initialize Kafka producer for DocEnrich
producer_enrich = KafkaProducer(bootstrap_servers='localhost:9092')

# Kafka consumer for DocExtractor topic
consumer_extractor = KafkaConsumer("DocExtractor", bootstrap_servers='localhost:9092')

for message in consumer_extractor:
    message_data = json.loads(message.value.decode('utf-8'))
    pdf_path = message_data["docPath"]
    doc_contents = get_pdf_text(pdf_path)
    
    # Enrich the message with docContents and docSnippets
    enriched_message = {
        "docID": message_data["docID"],
        "docPath": pdf_path,
        "docContents": doc_contents,
        "docSnippets": get_text_chunks(doc_contents)  # Modify to suit your needs
    }

    # Publish enriched message to DocEnrich topic
    producer_enrich.send("DocEnrich", value=json.dumps(enriched_message).encode('utf-8'))

producer_enrich.close()  # Close the producer when done

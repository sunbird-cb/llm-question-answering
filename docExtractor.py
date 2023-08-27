from kafka import KafkaProducer
import os
from Helper_Functions import *

folder_path = 'docs'
pdf_files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]

# Initialize Kafka producer for DocExtractor

producer_extractor = KafkaProducer(bootstrap_servers='localhost:9092')

for pdf_file in pdf_files:
    pdf_path = os.path.join(folder_path, pdf_file)

    # Create the message for DocExtractor
    message = {
        "docID": pdf_file,
        "docPath": pdf_path
    }

    # Publish message to DocExtractor topic
    producer_extractor.send("DocExtractor", value=json.dumps(message).encode('utf-8'))

producer_extractor.close()  # Close the producer when done


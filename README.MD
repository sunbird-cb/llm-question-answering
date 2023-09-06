# Project Title: LLM for Question Answering - 1

## Description
The aim of this project is to create a vector store for efficient retrieval of data for providing context to LLM (Language Model) for enhanced question-answering capabilities.

## Installation
Follow these steps to set up the project:

1. **Kafka and Zookeeper**: Install Kafka and Zookeeper by following the [official Kafka documentation](https://kafka.apache.org/documentation/). These components are crucial for data streaming and event processing.

2. **Milvus**: Set up Milvus by referring to the [official Milvus documentation](https://milvus.io/docs/v2.0.0/overview/what-is-milvus). Milvus is used as a vector database for efficient data retrieval.

3. **Clone Repository**: Clone this repository and navigate to the project folder.

4. **Install Dependencies**: Install the required Python dependencies by running the following command:

   ```bash
   pip install -r req.txt


**Note**: Make sure you have Kafka, Zookeeper, and Milvus running and that the dependencies in `req.txt` are installed.

You are now ready to use the project!

## Usage
The major focus should be on the following files:
- `DocExtraction.py`
- `DocProcessing.py`
- `Ingest.py`
- `Infer.py`

The basic flow of our program is as follows:

1. `DocExtraction.py`: This script recovers textual data from PDFs, splitting them into chunks using a sliding window approach. The extracted data is sent to the Kafka topic `raw_data`.

2. `DocProcessing.py`: This script consumes data from the Kafka topic `raw_data` and further processes the text chunks, including applying coreference resolution. The processed text is then sent to another Kafka topic named `processed_data`.

3. `Ingest.py`: This script periodically inserts the processed data into our Milvus vector database.

4. Finally, run `Infer.py` to retrieve context for your queries from the database.

This workflow enables efficient question answering by providing relevant context to the Language Model.






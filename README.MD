# Project Title: LLM for Question Answering - 1 and 2

## Description
This project focuses on harnessing the capabilities of Large Language Models (LLMs) to create an efficient question-answering system for our documents. LLMs, with their advanced natural language processing abilities, can revolutionize how we interact with textual data. By extracting content from documents and utilizing LLMs, we aim to enable direct and insightful question-answering system over documents.

# Aims of the projects 

## LLM for Question Answering 1 
The aim of this project is to create a vector store for efficient retrieval of data for providing context to LLM (Language Model) for enhanced question-answering capabilities.

## LLM for Question Answering 2 
This project's primary goal is to assess different Large Language Models for their suitability in question-answering tasks. We'll establish a structured pipeline to extract the most relevant documents from a vector database, chosen based on their similarity to user queries. These selected documents will act as context for Large Language Models, and produce answers to user queries.

## Installation
Follow these steps to set up the project:

1. **Kafka and Zookeeper**: Install Kafka and Zookeeper by following the [official Kafka documentation](https://kafka.apache.org/documentation/). These components are crucial for data streaming and event processing.

2. **Milvus**: Set up Milvus by referring to the [official Milvus documentation](https://milvus.io/docs/v2.0.0/overview/what-is-milvus). Milvus is used as a vector database for efficient data retrieval.

3. **Clone Repository**: Clone this repository and navigate to the project folder.

4. **Install Dependencies**: Install the required Python dependencies by running the following command:

   ```bash
   pip install -r req.txt


**Note**: Make sure you have Kafka, Zookeeper, and Milvus running and that the dependencies in `req.txt` are installed.
**Note**: Make sure to obtain an API key from Hugging Face and pass it as a function parameter in the Infer.py file.

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

4. Finally, run `Infer.py` to retrieve context for your queries from the vector database and pass it throught the LLM. We can now pose questions to our documents.

This workflow enables efficient question answering on documents by providing relevant context to the Large Language Model. 






# Evaluation Script 
This technical documentation outlines a Python script for evaluating multiple question-answering models using various metrics, such as F1 Score, BLEU Score, ROUGE Score, and Accuracy. The script utilizes the Hugging Face Transformers library for loading pre-trained models and tokenizers and provides insights into the performance of different models on a set of sample questions.

## Dependencies
Before using the script, ensure that you have the following Python libraries installed:

- numpy (for numerical operations)
- pandas (for data manipulation)
- nltk (Natural Language Toolkit for text processing)
- transformers (Hugging Face Transformers library for pre-trained models)
- rouge_score (for computing ROUGE scores)
- csv (for writing evaluation results to a CSV file)
- time (for measuring execution time)

## Script Overview
The script performs the following tasks:

- Imports necessary libraries and sets up NLTK for text processing.
- Defines functions for predicting answers, normalizing text, and computing various evaluation metrics (Exact Match, F1 Score, BLEU Score, ROUGE Scores, and METEOR Score).
- Defines a function to evaluate a given model using a set of sample questions and answers.
- Loads multiple pre-trained question-answering models from the Hugging Face model hub and evaluates their performance.
- Saves the evaluation results in a CSV file.


# Visualization Script 
This technical documentation outlines the Python script for creating and saving bar chart visualizations of model evaluation metrics using the Pandas, Seaborn, and Matplotlib libraries. The script assumes the availability of a CSV file containing model evaluation results and aims to provide insights by visualizing these results.

## Dependencies
**Note** :- Before using the script, ensure that you have the following Python libraries installed:
- pandas (for data manipulation)
- seaborn (for creating appealing visualizations)
- matplotlib (for customizing and saving plots)
- os (for file and folder manipulation)
- 
## Script Overview
The script performs the following steps:
- Reads model evaluation data from a CSV file.
- Sorts the data based on a chosen metric (e.g., 'Avg F1 Score') in descending order.
- Selects the top 20 models based on the sorted metric.
- Sets the Seaborn plot style to the default style.
- Defines a function to create a bar chart for a given metric and save it as an image.
- Creates a folder to store the visualizations.
- Specifies a list of metrics to visualize.
- Iterates through the list of metrics, creates separate bar chart visualizations, and saves them in the output folder.

These visualizations are extremely helpful for better and faster decision making in chossing a suitable LLM. Feel free to experiment with different metrics and design styles. 

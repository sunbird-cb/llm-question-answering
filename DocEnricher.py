import spacy
# from DocExtractor import data

nlp = spacy.load('en_core_web_sm', exclude = ['tagger' , 'parser' , 'ner' , 'lemmatizer' ])


def preprocess_text(text):
    # Step 1: Tokenization and Lowercasing
    doc = nlp(text.lower())
    tokens = [token.text for token in doc]

    # Step 2: Remove stop words
    tokens_without_stopwords = [token.text for token in doc if not token.is_stop]

    return tokens_without_stopwords

# Test the function
input_text = "The quick brown fox jumps over the lazy dog."
preprocessed_tokens = preprocess_text(input_text)
print(preprocessed_tokens)

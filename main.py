from newspaper import Article
from googletrans import Translator
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Step 1: Define the URL of the news article
url = 'https://www.bbc.com/news/articles/c8jlegg242no'  # Replace with the actual URL of the news article

# Step 2: Fetch the article
article = Article(url)
article.download()
article.parse()

# Display the original article text
print("Original Article:")
print(article.text)

# Step 3: Translate the article
source_language = 'auto'  # 'auto' detects the source language automatically
target_language = 'es'    # Replace 'es' with the desired target language code (e.g., 'fr' for French, 'de' for German)

translator = Translator()

try:
    translated = translator.translate(article.text, src=source_language, dest=target_language)
    translated_text = translated.text
    print("\nTranslated Article:")
    print(translated_text)
except Exception as e:
    print("Error during translation:", e)

# Step 4: Summarize the translated article
try:
    parser = PlaintextParser.from_string(translated_text, Tokenizer(target_language))
    summarizer = LsaSummarizer()
    
    # Number of sentences in the summary
    sentences_count = 10
    summary = summarizer(parser.document, sentences_count=sentences_count)
    
    print(f"\nSummary of the Translated Article ({sentences_count} sentences):")
    for sentence in summary:
        print(sentence)
except Exception as e:
    print("Error during summarization:", e)

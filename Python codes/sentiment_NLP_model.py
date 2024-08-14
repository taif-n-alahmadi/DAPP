import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon
nltk.download('vader_lexicon')

# Load your CSV file
df = pd.read_csv('cleaned_reviews.csv')

# Rename the PR column to Product
df.rename(columns={'PR': 'Product'}, inplace=True)

# Initialize the VADER sentiment intensity analyzer
sid = SentimentIntensityAnalyzer()

# Apply sentiment analysis to each review
def get_sentiment_label(review):
    scores = sid.polarity_scores(review)
    compound = scores['compound']
    if compound > 0:
        return 'POSITIVE'
    elif compound < 0:
        return 'NEGATIVE'
    else:
        return 'NEUTRAL'

# Use the correct column name 'reviews'
df['sentiment_label'] = df['reviews'].apply(get_sentiment_label)

# Save results to CSV (excluding the 'sentiment' column)
df.to_csv('electronics_reviews_with_vader_sentiment.csv', index=False, columns=['reviews', 'Product', 'sentiment_label'])

# Save results to TXT with headers
with open('electronics_reviews_with_vader_sentiment.txt', 'w') as f:
    f.write('review\tproduct\tsentiment\n')
    for _, row in df.iterrows():
        f.write(f"{row['reviews']}\t{row['Product']}\t{row['sentiment_label']}\n")

print("Sentiment analysis completed and results saved.")

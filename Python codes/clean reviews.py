import csv
import re
from textblob import TextBlob

def clean_text(text):
    """Clean and preprocess the text while preserving its content."""
    text = re.sub(r'^[\'"]+|[\'"]+$', '', text)  # Remove leading and trailing quotes
    text = re.sub(r'^[^\w\s]*[\d\s]*', '', text)  # Remove unwanted leading characters and numbers
    text = re.sub(r'\.{2,}', '.', text)  # Replace multiple dots with a single dot
    text = re.sub(r'\!{2,}', '!', text)  # Replace multiple exclamation marks with one
    text = re.sub(r'\?{2,}', '?', text)  # Replace multiple question marks with one
    text = re.sub(r'\b(\w)\1{2,}\b', r'\1', text)  # Reduce repeated letters
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)  # Remove URLs
    text = re.sub(r'[^\x00-\x7F]+', '', text)  # Remove non-printable characters
    text = re.sub(r'[^\w\s.,!?\'"]', '', text)  # Remove special characters but keep spaces and basic punctuation
    text = re.sub(r'\s+', ' ', text).strip()  # Normalize whitespace
    return text

def is_valid_review(review):
    """Check if the review is valid based on custom rules."""
    # Check if the review is not empty and not numeric or boolean
    return review and not review.isdigit() and review not in {'TRUE', 'FALSE'}

# Define file paths
input_txt_file_path = 'e-reviw.txt'
temp_csv_file_path = 'temp_reviews.csv'
output_csv_file_path = 'cleaned_reviews.csv'
output_txt_file_path = 'cleaned_reviews.txt'

# Read the TXT file and determine headers
with open(input_txt_file_path, 'r', encoding='utf-8') as txt_file:
    lines = txt_file.readlines()

if not lines:
    raise ValueError("Input TXT file is empty or unreadable.")

# Extract headers from the first line
headers = lines[0].strip().split('\t')

# Write data to a temporary CSV file
with open(temp_csv_file_path, 'w', encoding='utf-8', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    for line in lines[1:]:  # Skip the header line
        line = line.strip()
        if not line or re.match(r'^[\-\_=]+$', line):
            continue

        parts = re.split(r'\t+', line)
        if len(parts) < 2:
            continue

        review_part = parts[0].strip()
        product_part = parts[1].strip() if len(parts) > 1 else ''

        if review_part and product_part:
            csv_writer.writerow([review_part, product_part])

# Initialize lists for cleaned data
cleaned_reviews = []
products = []

# Read the temporary CSV file and process it
with open(temp_csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    seen_rows = set()  # To track and remove duplicate rows
    
    for row in csv_reader:
        if len(row) < 2:
            continue

        review_part = row[0].strip()
        product_part = row[1].strip() if len(row) > 1 else ''

        # Check if review is valid
        if not is_valid_review(review_part):
            continue

        # Clean review part
        cleaned_review = clean_text(review_part)
        if cleaned_review and len(cleaned_review) > 0:  # Ensure review part is not empty
            # Use a tuple of (review, product) to track duplicates
            row_tuple = (cleaned_review, product_part)
            if row_tuple not in seen_rows:
                seen_rows.add(row_tuple)
                cleaned_reviews.append(cleaned_review)
                products.append(product_part)

# Write cleaned data to CSV file with headers
with open(output_csv_file_path, 'w', encoding='utf-8', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)  # Write headers
    for review, product in zip(cleaned_reviews, products):
        csv_writer.writerow([review, product])

# Write cleaned data to TXT file with headers
with open(output_txt_file_path, 'w', encoding='utf-8') as txt_file:
    txt_file.write('\t'.join(headers) + '\n')  # Write headers
    for review, product in zip(cleaned_reviews, products):
        txt_file.write(f'{review}\t{product}\n')

print("Conversion, cleaning, and saving completed successfully.")

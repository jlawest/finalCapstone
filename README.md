# Amazon Product Review Analysis

This project aims to analyse sentiment and compare similarities between Amazon product reviews using natural language processing (NLP) techniques. The code provided utilises Python and several libraries for text processing and analysis.

## Modules Required

Before running the program, ensure you have the following modules installed:

- **spaCy**: A library for advanced natural language processing in Python.
- **pandas**: A fast, powerful, and flexible data analysis and manipulation tool.
- **spacytextblob**: A library that extends spaCy's capabilities with textblob's sentiment analysis.

You can install these modules via pip using the following commands:

```bash
pip install spacy
pip install pandas
pip install spacytextblob
```

## Usage

1. **Downloading the Data**: Head to this link to download the dataset - https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products 
2. **Loading Data**: The program reads Amazon product review data from a CSV file. Make sure to provide the correct file path to the data.

3. **Cleaning Data**: Null values in the 'reviews.text' columns are removed to ensure data quality.

4. **Sentiment Analysis**: The sentiment of each review is analyzed using spaCy and TextBlob. Reviews are classified as Positive, Negative, or Neutral based on their polarity.

5. **Review Comparison**: Two random reviews are selected from the dataset, and their similarity is compared using spaCy's similarity function. The result indicates whether the reviews are similar, not similar, or inconclusive.


## Note

- This project assumes you have access to Amazon product review data in CSV format. Adjust the file path accordingly.
- The provided code is a basic implementation. You may need to customize it based on your specific requirements or dataset structure.

Enjoy analyzing Amazon product reviews with this simple yet effective tool!

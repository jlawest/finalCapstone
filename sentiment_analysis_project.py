import spacy
import pandas as pd
from spacytextblob.spacytextblob import SpacyTextBlob
import random

# select spacy's 'sm' model for nlp and add it to text blob. 
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe("spacytextblob")

# grab the file path of the csv file and store in variable called data. 
data = 'archive/Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products.csv'

# Read the CSV file into a pandas DataFrame.
df = pd.read_csv(data)

# Using the dropna() function from pandas and with the subset parameter for what to clean ip if there are rows of data
# that return null.
cleaned_df = df.dropna(subset=['reviews.text']) 

# select the column of data we want to use from the df using the title name.  
review_data = cleaned_df['reviews.text']

# create function that will take the review as an argument, put this through nlp and textblob library to return polarity and sentiment
# data which is then contextualised using an if/else statement. 
def analyse_sentiment(review):
    # run the review through spacy's nlp, and store this in variable. 
    nlp_review = nlp(review)
    # Using the polarity attribute from the textblob library. 
    polarity = nlp_review._.blob.polarity
    # using the sentiment attribute.
    sentiment = nlp_review._.blob.sentiment
       
    print(review)
    print(sentiment)
    
    # if else statement helps to contextualise the data to a positive, negative or neutral sentiment in the review.  
    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

   
# creates a for loop to iterate through each row in the reviews columns, perform sentiment analysis via the function created earlier 
# which will in turn print out the review, the sentiment data and the polarity interpretation from the if/else statement.  
for review in review_data.head(10):
    print("---------------")
    print(analyse_sentiment(review))

    
print("""
      ------------------------------------------------------------------------------------------------------------------------------------
      """)
# Looking at the similarity of two reviews, using spacy's similarity function and random_int generator so the result is a different comparison each time. 
# 

random_num1 = random.randint(1, 4999)
random_num2= random.randint(1, 4999)


nlp = spacy.load('en_core_web_sm')
review_1 = nlp(review_data[random_num1])
print(f"Review 1: {review_data[random_num1]}")
review_2 = nlp(review_data[random_num2])
print(f"Review 2: {review_data[random_num2]}")


# spacy's comparison function. 

similarity_score = review_1.similarity(review_2)

# function that compares the similarity score and return a statement summarising if it's similar, not similar or 'inconclusive')
def similar():
    if similarity_score > 0.75:
        return 'Similar'
    elif similarity_score < 0.5:
        return 'Not Similar'
    else:
        return 'Inconclusive'

print(f"Similarity Score:, {similarity_score} - {similar()}")






    




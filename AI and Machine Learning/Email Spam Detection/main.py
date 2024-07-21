# Email Spam Detection

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
# Assuming you have a CSV file 'emails.csv' with two columns: 'label' (spam/ham) and 'text' (email content)
# You can find datasets online, such as the 'spam.csv' from the UCI Machine Learning Repository
df = pd.read_csv('emails.csv')

# Preprocess the data
df['label'] = df['label'].map({'spam': 1, 'ham': 0})

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Vectorize the text data
vectorizer = CountVectorizer(stop_words='english')
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train_counts, y_train)

# Predict on the test data
y_pred = clf.predict(X_test_counts)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Example usage: predicting a single email
def predict_email(text):
    text_counts = vectorizer.transform([text])
    prediction = clf.predict(text_counts)
    return 'spam' if prediction[0] == 1 else 'ham'

# Test the function with a new email
new_email = "Congratulations! You've won a $1000 gift card. Click here to claim your prize."
print(f"The email is classified as: {predict_email(new_email)}")

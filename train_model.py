import pandas as pd
import sys

# LOAD THE DATA
try:
    # Try different encodings
    encodings_to_try = ['utf-8', 'latin1', 'ISO-8859-1', 'cp1252']
    
    for encoding in encodings_to_try:
        try:
            data = pd.read_csv("C:\\Users\\surya\\OneDrive\\Desktop\\Django\\Scripts\\smsdetection\\resources\\spam.csv", 
                             encoding=encoding)
            print(f"Successfully loaded the file with {encoding} encoding")
            break
        except UnicodeDecodeError:
            continue
    else:
        raise Exception("Could not read the file with any of the attempted encodings")

    # Print original columns
    print("\nOriginal columns:", data.columns.tolist())
    
    # Remove last 3 columns
    columns_to_keep = data.columns[:2]  # Keep only first 2 columns
    data = data[columns_to_keep]
    
    print("Columns after removal:", data.columns.tolist())
    
    # CLEAN DATA
    initial_rows = len(data)
    data.dropna(inplace=True)
    rows_after_cleaning = len(data)
    if initial_rows != rows_after_cleaning:
        print(f"Removed {initial_rows - rows_after_cleaning} rows with missing values")
    
    data.rename(columns={"v1":"label","v2":"message"}, inplace=True)
    
    # Print basic statistics
    print("\nDataset Statistics:")
    print(f"Total number of messages: {len(data)}")
    print(f"Number of unique labels: {data['label'].nunique()}")
    print("\nFirst few rows of the dataset:")
    print(data.head())
    print(data.tail())
    
except FileNotFoundError:
    print("Error: Could not find the CSV file. Please check the file path.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred: {str(e)}")
    sys.exit(1)

# convert labels
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

#TEXT PREPROCESSING
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = re.sub(r'\W', ' ', text)  # Remove non-alphanumeric characters
    text = text.lower()
    text = text.split()
    text = [ps.stem(word) for word in text if word not in stop_words]
    return ' '.join(text)

data['cleaned_message'] = data['message'].apply(preprocess_text)





# MODEL TRAINING
 #1. Splitting the dataset
from sklearn.model_selection import train_test_split

X = data['cleaned_message']
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  

#2. Vectorization(converting text to vectors)
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=5000)
X_train = vectorizer.fit_transform(X_train).toarray()
X_test = vectorizer.transform(X_test).toarray()

#3. Training the model
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(X_train, y_train)

#4. Testing the model(evaluating the model)
from sklearn.metrics import accuracy_score

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

#5. Saving the model
import joblib

joblib.dump(model, 'spam_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')





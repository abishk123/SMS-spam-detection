# Standard library import for handling file paths
import os

# Imports joblib for loading machine learning models
import joblib

# Django imports for rendering templates and accessing settings
from django.shortcuts import render
from django.conf import settings

# Gets the absolute path to the project's root directory
# This is used to locate model files regardless of where the script is run from
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Loads the trained spam detection model from spam_model.pkl
# This model was trained to classify messages as spam or ham
model = joblib.load(os.path.join(BASE_DIR, 'spam_model.pkl'))

# Loads the text vectorizer that converts messages into numerical features
# This must be the same vectorizer used during model training
vectorizer = joblib.load(os.path.join(BASE_DIR, 'vectorizer.pkl'))

# Main view function that handles both GET and POST requests
def classify_message(request):
    # If it's a POST request (user submitted a message)
    if request.method == 'POST':
        # Get the message from the POST data
        message = request.POST['message']
        
        # Transform the message into numerical features using the vectorizer
        transformed_message = vectorizer.transform([message])
        
        # Use the model to predict if message is spam (1) or ham (0)
        prediction = model.predict(transformed_message)[0]
        
        # Convert numerical prediction to human-readable label
        label = 'Spam' if prediction == 1 else 'Ham'
        
        # Render result.html template with the prediction label
        return render(request, 'result.html', {'label': label})
    
    # If it's a GET request, just show the input form
    return render(request, 'index.html')
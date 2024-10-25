import os
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
from flask import jsonify
from sklearn.exceptions import NotFittedError

application = Flask(__name__)

@application.route("/")
def index():
    return "Your Flask App Works! V1.0"

@application.route('/predict', methods=['POST'])
def load_model():
    try:
        # Check if model files exist
        if not os.path.exists('basic_classifier.pkl') or not os.path.exists('count_vectorizer.pkl'):
            return jsonify({'error': 'Model files not found'}), 500

        # Load the model
        try:
            with open('basic_classifier.pkl', 'rb') as fid:
                loaded_model = pickle.load(fid)
        except (pickle.UnpicklingError, AttributeError, EOFError, ImportError, IndexError) as e:
            return jsonify({'error': f'Error loading model: {str(e)}'}), 500

        # Load the vectorizer
        try:
            with open('count_vectorizer.pkl', 'rb') as fid:
                vectorizer = pickle.load(fid)
        except (pickle.UnpicklingError, AttributeError, EOFError, ImportError, IndexError) as e:
            return jsonify({'error': f'Error loading vectorizer: {str(e)}'}), 500

        data = request.json
        if 'text' not in data:
            return jsonify({'error': 'Invalid input. "text" field is required'}), 400

        text = data['text']
        if not isinstance(text, str):
            return jsonify({'error': 'Invalid input. "text" must be a string'}), 400

        if not text.strip():  # Check if the string is empty or only whitespace
            return jsonify({'error': 'Invalid input. "text" cannot be empty'}), 400

        # Transform the text
        try:
            transformed_text = vectorizer.transform([text])
        except Exception as e:
            return jsonify({'error': f'Error transforming text: {str(e)}'}), 500

        # Make prediction
        try:
            prediction = loaded_model.predict(transformed_text)[0]
        except Exception as e:
            return jsonify({'error': f'Error making prediction: {str(e)}'}), 500

        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

if __name__ == "__main__":
    application.run(port=5000, debug=True)
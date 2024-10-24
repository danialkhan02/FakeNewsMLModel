from flask import Flask, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
from flask import jsonify

application = Flask(__name__)

@application.route("/")
def index():
    return "Your Flask App Works! V1.0"

@application.route('/predict', methods=['POST'])
def load_model():
    loaded_model = None
    with open('basic_classifier.pkl', 'rb') as fid:
        loaded_model = pickle.load(fid)

    vectorizer = None
    with open('count_vectorizer.pkl', 'rb') as fid:
        vectorizer = pickle.load(fid)

    data = request.json
    if 'text' not in data:
        return jsonify({'error': 'No text provided for prediction'}), 400

    text = data['text']
    transformed_text = vectorizer.transform([text])

    prediction = loaded_model.predict(transformed_text)[0]
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    application.run(port=5000, debug=True)
import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
pickle_in = open("gnb.pkl", "rb")
classifier = pickle.load(pickle_in)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    wheat_labels = {1: 'Kama', 2: 'Rosa', 3: 'Canadian'}
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = classifier.predict(final_features)
    return render_template('index.html', prediction_text='The wheat seed belongs to class {}'.format(wheat_labels[prediction[0]]))


if __name__ == '__main__':
    app.run()

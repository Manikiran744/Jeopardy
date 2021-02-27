from flask import Flask, jsonify, request
from keras.models import load_model
from keras_bert import get_custom_objects
import pickle

import ktrain

app = Flask(_name_)

# loading model 

model = load_model('./tf_model.h5', custom_objects=get_custom_objects())

# Request for a input
@app.route('/predict/<input>', methods=["GET"])
def predict_model(input):
        #Processing input and predicting the value of input
        
        preproc = pickle.load(open('./tf_model.preproc', 'rb'))
        predictor = ktrain.get_predictor(model, preproc)
        pred = predictor.predict(input)
        print(pred)
        prediction = {'input': input, 'prediction': int(pred)}
        return jsonify(prediction)

if _name_ == "_main_":
        app.run(debug=True)

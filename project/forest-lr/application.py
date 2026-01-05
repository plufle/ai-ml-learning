from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

ridge = pickle.load(open('models/ridge.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        data = scaler.transform(np.array([[temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]))
        result = ridge.predict(data)
        return render_template('home_index.html', prediction=result[0])
    else:
        return render_template('home_index.html')
    

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)

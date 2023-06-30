import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from joblib import load
import os

app = Flask(__name__)
model = load('knn2.sav')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/predict', methods = ['POST'])
def predict():

    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    features_name = ['FULL_TIME_POSITION', 'PREVAILING_WAGE', 'YEAR', 'WORK_N', 'SOC_N']

    df = pd.DataFrame(features_value, columns = features_name)
    prediction = model.predict(df)
    prediction = np.argmax(prediction)
    print(prediction)
    
    if prediction==0:
        output="Accepted!"
    else:
        output="Denied!"
    return render_template('analysis.html', prediction_text='   {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)

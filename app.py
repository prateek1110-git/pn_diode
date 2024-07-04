import pickle
from flask import Flask, request, render_template, session
import numpy as np
import pandas as pd

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Secret key for session management

regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def home():
    # Initialize session for storing previous inputs and outputs if not already done
    if 'history' not in session:
        session['history'] = []
    return render_template('web.html', history=session['history'])

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from the form
    data = [float(x) for x in request.form.values()]
    data1 = [float(x) for x in request.form.values()]

    # Replace original values with the log values
    n_doping_log = np.log10(float(data[0]))
    p_doping_log = np.log10(float(data[1]))
    data[0] = n_doping_log
    data[1] = p_doping_log

    final_input = scalar.transform(np.array(data).reshape(1, -1))

    # Predict the output
    output_log = regmodel.predict(final_input)[0]
    output = 10**output_log

    if 'history' not in session:
        session['history'] = []

    session['history'].append({
        'input': data1,
        'output': output
    })

    return render_template("web.html", prediction_text="The predicted Output Current (in Amperes) is {} A".format(output), history=session['history'])

@app.route('/clear', methods=['POST'])
def clear():
    # Clear the history in the session
    session.pop('history', None)
    return render_template('web.html', history=[])

if __name__ == "__main__":
    app.run(debug=True)

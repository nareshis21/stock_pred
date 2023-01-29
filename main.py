from flask import Flask,request,jsonify
import numpy as np
import pickle

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/predict',methods=['POST'])
def predict():
    high = request.form.get('high')
    low = request.form.get('low')
    open = request.form.get('open')
    volume = request.form.get('volume')
    high=float(high)
    low=float(low)
    open=float(open)
    volume=float(volume)
    input_query = np.array([[high,low,open,volume]])
    result = model.predict(input_query)[0]
    return jsonify(str(result))

if __name__ == '__main__':
    app.run(debug=True)
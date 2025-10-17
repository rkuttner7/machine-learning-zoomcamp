# Web service provide predictions for a given customer  

import pickle
from flask import Flask
from flask import request
from flask import jsonify 

app =  Flask('churn') # identity to web service

# parameters

C = 1.0
input_file = f'model_{C}.bin'

### Load model
# Character Meaning:
# 'r'       open for reading the file
with open(input_file, 'rb') as f_in: 
    (dv, model) = pickle.load(f_in)

@app.route('/predict', methods=['POST']) 
def predict():
    # convert json to Python dictionary
    customer = request.get_json()
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5 

    result = {
        # remove numpy class to convert to json without error
        # > TypeError: Object of type bool_ is not JSON serializable
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 9696)

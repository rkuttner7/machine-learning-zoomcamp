from flask import Flask

app =  Flask('ping') # identity to web service

#Turn a python function into a webservice using Flask.
@app.route('/ping', methods=['GET']) # use decorator to add Flask's functionality to our function
def ping():
    return "PONG"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 9696)
# ML Zoomcamp 5.4 - Web Services: serving the churn model with Flask  

* wrap predict script into a Flask app
* Query it with `requests`
* Prepare for production with `gunicorn`
* Run on Windows with `waitress`    

Turn a python function into a webservice using Flask.

## Notes

The web service is coded in `code\predict.py`.

Test the running service using a request with either:  
* `code\predict_test.ipynb`  
* `python code\predict_test.py`  
  
### **Functions and methods:**  

* `request.get_json()` - convert json to Python dictionary from a proxy to the object bound to a context-local object.  
  
* `jsonify` - Flask method converts Python dictionary to JSON. Values must be Python native, must cast numpy to avoid error.  
    > TypeError: Object of type bool_ is not JSON serializable  
  
* `gunicorn [options] [app module]` - a WGSI server for production.  
**Example call**: `gunicorn --bind 0.0.0.0:9696 predict:app`,  
where for `predict:app` the name of python script is `predict.py` and within the script the local variable name for the webservice is assigned to the value `app`.  
  
### **Futher Reading**  
* [Run Python WSGI Web App with Waitress | Dev Dungeon](https://www.devdungeon.com/content/run-python-wsgi-web-app-waitress) a turial on **Waitress** a WSGI server for Windows.  
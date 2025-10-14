# ML Zoomcamp 5.3 - Web Services: Introduction to Flask 

* Write a simple ping/pong app
* Query it with `curl` and browser

Turn a python function into a webservice using Flask.

## Notes

**Web service** - method used to communicate between electronic devices.

`'0.0.0.0'` - local host address, can also be referred using `localhost`

Simple template Flask app on port 9696 `GET` method can be querried using any of:  
* `http://localhost:9696/ping` through the browser
* on the command line:  
    * `curl 0.0.0.0:9696/ping`
    * `curl localhost:9696/ping`

### **Functions and methods:**  

Relevant web service methods:  
* `GET`: retrieves files, For example when we are searching for a cat image in google we are actually requesting cat images with GET method.  
* `POST`: enables sending data to a server to create or update a resource. For example in a sign up process, when we are submiting our name, username, passwords, etc we are posting our data to a server that is using the web service. (Note that there is no specification where the data goes)  
`PUT`: is same as POST but we are specifying where the data is going to.  
`DELETE`: is a request to delete some data from the server.  
  


### **Futher Reading**  
* [HTTP request methods | Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods) short summary of common HTTP methods related to requests.  
* [0.0.0.0 vs localhost](https://stackoverflow.com/a/20778887/861423)  
* [Top-level script enviroment | Python Official documentation](https://docs.python.org/3.9/library/__main__.html)  
* [route decorator | Flask API documentation](https://flask.palletsprojects.com/en/2.2.x/api/#flask.Flask.route)  

# Deploy Machine Learning Models with FastAPI, Docker, and Fly.io  
  
[How to Deploy Machine Learning Models with FastAPI, Docker, and Fly.io | End-to-End Tutorial](https://www.youtube.com/watch?v=jzGzw98Eikk) lecture video.  
  
Coding can be found in directory `workshop-deployment/`.  
  
[Lecture notes](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/05-deployment/workshop)  

The workshop follows the same order as in the module:  
  
* Saving and loading the model with pickle  
* Turning the notebook into a train script  
* Introduction to **FastAPI** (instead of Flask)  
* Serving the model with FastAPI  
* Input validation with **Pydantic** (new)  
* Virtual environment management - **uv** (instead of Pipenv)  
* Containerization - Docker  
* Deployment with **Fly.io**  

### Pipelines

**Scikit-Learn pipelines**: combine multiple data fitting steps into a single call.

```PYTHON
pipeline = make_pipeline(
    DictVectorizer(),
    LogisticRegression(solver='liblinear')
)

pipeline.fit(train_dict, y_train)
```

### Turning the notebook into a script

Convert Jupyter notebook to script:  
```BASH
jupyter nbconvert --to=script workshop-uv-fastapi.ipynb
mv workshop-uv-fastapi.py train.py
```
  
### Serve the model (FastAPI)  
  
* **FastAPI** - 
* **uvicorn** - 

`pip install fastapi uvicorn`

send a request with curl: `curl localhost:9696/ping`.

Run the web application 'ping.py':
 * `uvicorn ping:app --host 0.0.0.0 --port 9696 --reload` - server will update when code changes without restarting server
 * `python ping.py`



All endpoints / methods are documented at `http://localhost:9696/docs`.


* `def predict(customer: Dict[str, Any]):` - type hint that dictionary expected, from library **typing**.

### **input and output validation**

Define required / allowed fields and values for input and output using library **pydantic** and **typing**.
    * from typing:
        * Dict
        * Any
        * Literal
    * from pydantic 
        * BaseModel - 
        * Field - 
        * ConfigDict - raise an error for additional fields
        * model_dump - (replaces deprecated method `dict`)


### **Environment management**  

* `uv init` - initialize project  
* `uv add [python libraries]` - add python library dependencies  

* `uv run` - run something in virtual environment:  
    * `uv run uvicorn predict:app --host 0.0.0.0 --port 9696 --reload`
  
* `uv sync` - install all the dependencies for new project  

# Deployment

* Elastic Beanstalk
* Google CloudRun
* AWS App Runner
* Fly.io

### Further reading:  
* [Pipelines | Scikit-learn User Guide](https://scikit-learn.org/stable/modules/compose.html#pipeline) details on setting up a fixed sequence of steps in processing the data, for example feature selection, normalization and classification.  
* [Tutorial User Guide: First steps | FastAPI official documentation](https://fastapi.tiangolo.com/tutorial/first-steps/#alternative-api-docs) shows you how to use FastAPI with most of its features, step by step.  
* [Quickstart | Uvicorn official documentation](https://uvicorn.dev/#quickstart) webservice
* [Pydantic | homepage](https://docs.pydantic.dev/latest/) the most widely used data validation library for Python.
* [Python type hints | typing  official home](https://docs.python.org/3/library/typing.html)  
* [uv home page](https://docs.astral.sh/uv/) extremely fast Python package and project manager  
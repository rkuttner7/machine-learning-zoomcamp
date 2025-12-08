# 9.1 Introduction to Serverless



### **Notes**:  

**Setting Up a Lambda Function**:  
    Accessing Lambda:  

* Go to the AWS Management Console and search for the `Lambda` service.

Creating a Function:

> Choose option: `Author from scratch`  
> Name your function (e.g., mlzoomcamp-test)  
> Select the runtime environment: **Python 3.9**  
> Select architecture **x86_64**  

Understanding Function Parameters:

    event: Contains the input data passed to the function (e.g., a JSON payload).
    context: Provides details about the invocation, configuration, and execution environment.

Updating the Default Function:

    Edit lambda_function.py with custom logic. Example:

```python
def lambda_handler(event, context):
    print("Parameters:", event) # Print input parameters
    url = event["url"]  # Extract URL from input
    #results = predict(url)
    #return results
    return {"prediction": "clothes"}  # Sample response
```

**Testing and Deployment**

1. Create a Test Event:
    * Define a mock input to simulate real-world data.
2. Deploy Changes:
    * Save and deploy the function to apply updates.
3. Test Your Function:
    * Run the function with the test event to ensure it works as expected.


### Docker Image  

[AWS provided base images for Lambda](https://gallery.ecr.aws/lambda/python) components to run your functions packaged as container images on AWS Lambda  

### **Functions and methods:**  


  
### **Further reading**:  
* [Exporting a PyTorch model to ONNX | Deep Learning with PyTorch: A 60 Minute Blitz](https://docs.pytorch.org/tutorials/beginner/onnx/export_simple_model_to_onnx_tutorial.html) tutorial converting a model defined in PyTorch into the ONNX    
* [Amazon Elastic Container Registry Public Gallery](https://gallery.ecr.aws/) public images  

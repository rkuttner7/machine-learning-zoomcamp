# 8.1 Deep Learning - Classification


* use pre-trained models for general image classification
* **Convolutional layers** let us turn an image into a vector
* **Dense layers** use the vector to make the predictions
* Instead of training a model from scratch, we can use **transfer learning** and re-use already trained convolutional layers
* First, train a small model (150x150) before training a big one (299x299)
* **Learning rate** - how fast the model trians. Fast learners aren't always best ones
* save the best model using `callbacks` and `checkpointing`
* avoid overfitting, use `dropout` and `augmentation`


### **Notes**:  


**How to use Google Colab for Deep Learning?**:  
  
1. Create or import your notebook into Google Colab.
2. Click on the drop-down at the top right-hand side.
3. Click on “Change runtime type.”
4. Choose T4 GPU.


**Convolutional neural network** (CNN or ConvNet): a feed-forward neural network for processing data with grid-like topology, often to analyze visual images to detect and classify objects.  
  

### **Functions and methods:**  

from tensorflow.keras.applications.xception import Xception
from tensorflow.keras.applications.xception import preprocess_input
from tensorflow.keras.applications.xception import decode_predictions
  
### **Further reading**:  
* [CNN Explainer Learn Convolutional Neural Network (CNN)](https://poloclub.github.io/cnn-explainer/) 
* [Lesson: Convolutional Neural Networks (CNNs / ConvNets) | CS231n Deep Learning for Computer Vision - Stanford online course](https://cs231n.github.io/convolutional-networks/) part of 10-week course, learn to implement and train neural networks and understand research in computer vision.  
* [Commonly used activation functions | CS231n Deep Learning for Computer Vision - Stanford online course](https://cs231n.github.io/neural-networks-1/#actfun)   
* [Machine Learning for Intelligent Systems | Kilian Weinberger, Cornell](https://www.cs.cornell.edu/courses/cs4780/2018fa/page18/) recorded lectures and notes on machine learning  
* [TensorFlow tutorial: Load and preprocess images | Colab Google](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/load_data/images.ipynb) how to load and preprocess image datasets using Keras preprocessing layers and utilities.  
* [Imagenet dataset](https://www.image-net.org/)
* [Pre-trained models | Keras](https://keras.io/api/applications/)  
* [Pre-trained models | Pytorch](https://docs.pytorch.org/vision/main/models.html#table-of-all-available-classification-weights)  
* [PyTorch Documentation](https://pytorch.org/docs/)  
* [Learn the basics |PyTorch](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)  



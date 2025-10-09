## 4.6 ROC Area Under the Curve (AUC)


## Notes

*Area under the curver** (AUC): is a measure of how well a model separates positive and negative classes.  
AUC can be interpreted as the probability that a randomly selected positive example has a greater score than a randomly selected negative example.


    
**Functions and methods:** 
  
* `np.repeat([0, 1], repeats = [num_neg, num_pos])` - repeat each element of a numpy array.  
* `roc_curve(x, y)` - `sklearn.metrics` class for calculating the false positive rates, true positive rates, and thresholds, given a target x dataset and a predicted y dataset.  


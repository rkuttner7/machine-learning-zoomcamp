## 4.7 Cross-Validation  

* Evaluating the same model on different subsets of data
* Getting the average prediction and the spread within predictions


## Notes

**Cross-validations** refers to evaluating the same model on different subsets of a dataset, getting the average prediction, and spread within predictions.

    
### **Functions and methods:** 
* `Kfold(k, s, x)` - `sklearn.model_selection` class for calculating the cross validation with `k` folds, `s` boolean attribute for shuffle decision, and an `x` random state  
* `Kfold.split(x)` - `sklearn.Kfold` method for splitting the `x` dataset with the attributes established in the Kfold's object construction.  
  

### **Futher Reading**  
* [Iterators & Generators | Python Practive Book](https://anandology.com/python-practice-book/iterators.html), Python tutorial with lot of examples and practice problems.


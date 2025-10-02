## Notes

Binary classification tasks can have negative (0) or positive (1) target values. The output of these models is the probability of $x_i$ belonging to the positive class.  

**Logistic regression** is similar to linear regression because both models take into account the bias term and weighted sum of features. The difference between these models is that the output of linear regression is a real number, while logistic regression outputs a value between zero and one, applying the sigmoid function to the linear regression formula. 




### **Functions and methods:**   
  
* `np.linspace(start, stop, num)` return evenly spaced numbers over a specified interval. Returns `num` evenly spaced samples, calculated over the interval [`start`, `stop`].  `num` is optional number of samples to generate (Default is 50).
  
* `LogisticRegression(solver='lbfgs')` - class instance of logistic regression model from package **linear_model** in **Scikit-Learn**.  
* `[logistic regression model].fit(X, y)` - fit a logistic regression model on to model instance.  
* `[logistic regression model].intercept_[0]` - return the bias or intercept of the LR model
* `[logistic regression model].coef_[0]` - return the coefficients or weights of the LR model
* `[logistic regression model].predict(x)` - Hard prediction, either {0, 1} on the x dataset
* `[logistic regression model].predict_proba(x) - Soft predictions on the x dataset returning probabilities of being each of outcome categories (eg. probility of being class zero or one) 
  
* `zip(x, y)` - returns a new list with elements from `x` joined with their corresponding elements on `y`
* `_` - carry forward output from previous Juptyter notebook cell as input to next cell (eg. [1,2,3] -> sum(_))
* `array[-1]` - return last element from array using negative numbers.
  
### **Further reading**:  
  
* [`Scale numeric features` | scikit learn user guide](https://scikit-learn.org/stable/modules/preprocessing.html#standardization-or-mean-removal-and-variance-scaling) to help logistic regression models converge, also a common requirement for many machine learning estimators.  
  
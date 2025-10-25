# 6.1 Decision Trees 


## Notes

The decision trees make predictions based on the bunch of if/else statements by splitting a node into two or more sub-nodes.

With versatility, the decision tree is also prone to **overfitting**. One of the reasons why this algorithm often overfits is its depth.

**Decision Tree Learning Algorithm**:
* At a node, find the best split.
* Stop if max depth is reached.
* For each child node, if the node is sufficiently large and not pure, repeat the process from the beginning.


**Random forest**: 
* each model is a decision tree and their predictions are aggregated to identify the most popular result. Randomness decorrelate the trees, preventing overfitting and promoting generalization to unseen data.. The 'randomness' in Random Forest stems from two key aspects:  
    * each tree is trained on bootstrapped sample of the original data  
    * random subset of features is considered for splitting. This feature randomness helps 
       
**Bootstrapping** is a resampling technique where numerous subsets of the data are created by sampling the original data with replacement.  
   
**Ensemble learning** is a machine learning paradigm where multiple models, often referred to as 'weak learners', are strategically combined to solve a particular computational intelligence problem.  
  
### **Functions and methods:**  

* `numpy.[series].map` - Substitute each value in a Series with another.  
* `numpy.[series].replace(to_replace, value` - Replace values given in `to_replace` with `value`.
    * Examples:
```python
df = pd.DataFrame(
    {'A': [0, 1, 2, 3, 4],
    'B': [5, 6, 7, 8, 9],
    'C': ['a', 'b', 'c', 'd', 'e']})

>>> df.replace(0, 5)
|  A  B  C
0  5  5  a
1  1  6  b
2  2  7  c
3  3  8  d
4  4  9  e

>>> df.replace({'A': {0: 100, 4: 400}})
|    A  B  C
0  100  5  a
1    1  6  b
2    2  7  c
3    3  8  d
4  400  9  e
```
  
* `pandas.DataFrame(data, columns = [column labels])` - Construct DataFrame from numpy ndarray:  
```python
>>> df2 = pandas.DataFrame(
    numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    columns=['a', 'b', 'c'])
>>> df2
   a  b  c
0  1  2  3
1  4  5  6
2  7  8  9 
```
  
* `DecisionTreeClassifier`: classification model from `sklearn.tree` class.  
    * `max_depth`: hyperparameter to control the maximum depth of decision tree algorithm.  
* `export_text`: method from `sklearn.tree` class to display the text report showing the rules of a decision tree.  

* `pandas.[data frame].pivot(index=<field(s) for rows>, columns=<field for columns>, values=<field for values>) - reshape data  

* `pyplot.plot(x, y, label, color)`: draw line plot for the values of y against x values, from library `matplotlib`.  
    * `pyplot.legend()` - generate legend based on the `labels` and optionally `color`.  

* `seaborn.heatmap(<dataframe>, annot=[bool], fmt=[str])` - draw the heatmap into the
currently-active Axes  
    * `annot` - If `True`, write the data value in each cell  
    * `fmt` - formatting code to use when adding annotations (eg `".3f"`)  
  
  
* `from sklearn.ensemble import RandomForestClassifier`: random forest classifier   
    * `RandomForestClassifier(n_estimators=n, random_state=1)` - arguments:  
        * `n_estimators` - number of trees in the forest  
        * `max_depth` - maximum depth of each decision tree
        * `min_samples_leaf` - A split point at any depth will only be considered if it leaves at
 least the minimum number of samples required in each branch.  
        * `random_state` - random seed  
  
### Further reading:
* [Decision Trees | scikit learn User Guide](https://scikit-learn.org/stable/modules/tree.html) short summary on model and its benefits / disadvanates.
    * [Decision Trees: Complexity | scikit learn User Guide](https://scikit-learn.org/stable/modules/tree.html#complexity) details on classification criteria options.
* [Intro to Decision Trees | All Models Are Wrong: Concepts of Statistical Learning](https://allmodelsarewrong.github.io/trees.html) chapter on statistical theory behind trees, with motivating examples in R.  
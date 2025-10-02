## Notes

**Churn rate**: Difference between global mean of the target variable and mean of the target variable for categories of a feature. The larger differences are indicators that a variable is more important than others.
  
**Risk ratio**: Ratio between mean of the target variable for categories of a feature and global mean of the target variable. If this ratio is greater than 1, the category is more likely to churn, and if the ratio is lower than 1, the category is less likely to churn. It expresses the feature importance in relative terms.
  
**Mutual information** is a concept from information theory, which measures how much we can learn about one categorical variable if we know the value of another. In this project, we can think of this as how much do we learn about churn if we have the information from a particular feature. So, it is a measure of the importance of a categorical variable.  
  
**Correlation coefficient** measures the degree of dependency between two continuous variables. This value is negative if one variable grows while the other decreases, and it is positive if both variables increase. Depending on its size, the dependency between both variables could be low, moderate, or strong. It allows measuring the importance of numerical variables.
  
**Functions and methods:**   
  
* `df.groupby('x').y.agg([mean()])` - returns a dataframe with mean of y series grouped by x series  
    **Details:** [Group by: split-apply-combine | User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)  
* `display(x)` displays an output in the cell of a jupyter notebook, from package `IPython`.  
* `mutual_info_score(x, y)` - Scikit-Learn class for calculating the mutual information between the x target variable and y feature.  
* `df[x].apply(y)` - apply a function `y` to the series `x` of the dataframe `df.  
* `df.sort_values(ascending=False).to_frame(name='x')* - sort values in desending order and called the column as x.
* `df[x].corrwith(y)` - returns the correlation between x and y series. This is a function from pandas.

  
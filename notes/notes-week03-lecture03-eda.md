## Notes

The EDA for this project consisted of: 
* Checking missing values 
* Looking at the distribution of the target variable (churn)
* Looking at numerical and categorical variables 

**Functions and methods:** 

* `df.x.value_counts()` returns the number of values for each category in x series. The `normalize=True` argument retrieves the percentage of each category. In this project, the mean of churn is equal to the churn rate obtained with the value_counts method. 
* `df[x].nunique()` - returns the number of unique values in x series 
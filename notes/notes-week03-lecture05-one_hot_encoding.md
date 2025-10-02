## Notes

**One-Hot Encoding** allows encoding categorical variables in numerical ones. This method represents each category of a variable as one column, and a 1 is assigned if the value belongs to the category or 0 otherwise.  
  
  
### **Functions and methods:**   
  
* `df[x].to_dict(orient='records')` - convert x series to dictionaries, oriented by rows.  
* `DictVectorizer(sparse = False)` - `Scikit-Learn`, `feature_extraction` class for one-hot encoding.
* `fit_transform(x)` - vectorizer method converts dictionaries into a sparse matrix, each category getting a binary indicator colums. It does not affect the numerical variables.  
* `transform(x)` - takes the categories fit prior within the vectorizer and converts the dictionary to a matrix. Used for validation data to avoid data leakage out of training.  
* `DictVectorizer().get_feature_names_out()` - return the names of the columns in the sparse matrix.  

### **Further reading**:  

* Alternatively, use [`OneHotEncoding` | scikit learn user guide](https://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features) class to implement one-hot encoding.   
  
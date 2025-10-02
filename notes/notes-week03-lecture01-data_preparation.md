## Notes

**Pandas attributes and methods:** 

* `df.head().T` - take a look of the transposed dataframe 
* `pd.to_numeric()` - convert a series values to numerical values. The `errors='coerce'` argument allows making the transformation despite some encountered errors. 
* `df.fillna()` - replace NAs with some value 
* `(df.x == "yes").astype(int)` - convert x series of yes-no values to numerical values. 
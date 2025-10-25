# 6.7 Gradient boosting and XGBoost

**boosting** - models are combined sequentially, where each model takes the prediction errors made by the previous model and then tries to improve the prediction.   
  
### **Notes**:  

Other useful parameter are:
* `subsample` (default=1) - Subsample ratio of the training instances. Setting it to 0.5 means that model would randomly sample half of the training data prior to growing trees. range: (0, 1]  
* `colsample_bytree` (default=1)- This is similar to random forest, where each tree is made with the subset of randomly choosen features.  
* `lambda` (default=1) - Also called reg_lambda. L2 regularization term on weights. Increasing this value will make model more conservative.  
* `alpha` (default=0) - Also called reg_alpha. L1 regularization term on weights. Increasing this value will make model more conservative.  
  

### **Functions and methods:**  

* `xgboost.DMatrix(data, label = <outcome array>, feature_names=<list of field names>)` - an internal data structure that is used by XGBoost, which is optimized for both memory efficiency and training speed.  
  
* `xgboost.train(params = <dictionary>, dtrain = <xgboost.core.DMatrix>, num_boost_round=[default 10])`  
    * `params` - Booster params.  
        * `eta` - learning rate (default 0.3)  
        * `max_depth` - maximum depth of a tree default (6).  
        * `min_child_weight`- minimum observations in a leaf node  
        * `objective`: specify which problem we are trying to solve (eg. "binary:logistic" for binary classification, "reg:squarederror" for regression)  
        * `nthread`: cores available for parallelized training.  
        * `seed`: set for reproducibility  
        * `verbosity`: controls log messaging (eg. `1` to show warnings)  
        * `eval_metric`: Evaluation metrics for validation data. User can add multiple.
    * `evals`: List of validation sets for which metrics will evaluated during training. Validation metrics will help us track the performance of the model.  
    * `evals_result`: output evaluation results to an empty dictionary  
  
* `%%capture output` - captures the standard output and standard error of a cell of a jupyter notebook, from package `IPython`.   
  
* `[dictionary].keys()` - list keys in dictionary  
  
### **Further reading**: 
* [XGBoost Parameters | official documentation](https://federated-xgboost.readthedocs.io/en/latest/parameter.html) describes types of parameters for training {general parameters, booster parameters and task parameters}  
* [XGBoost for Survival Analysis (Cox Model) | xgboosting](https://xgboosting.com/xgboost-for-survival-analysis-cox-model/) example of training a boosted Cox-Proportional hazards model using XGboost.  
* [How to predict survival curves using xgboost | stackExchange](https://datascience.stackexchange.com/questions/65266/how-do-i-predict-survival-curves-using-xgboost?rq=1) XGBoost only outputs risk scores. To predict survival need to estimate the baseline hazard(s).  
* [Gradient Boosted Models Survival models | scikit-survival](https://scikit-survival.readthedocs.io/en/stable/user_guide/boosting.html) description of boosted survival regression model possible using library extension to scikit-learn.  
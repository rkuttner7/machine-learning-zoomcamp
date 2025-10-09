## 4.5 ROC curves


## Notes

**Receiver Operating Characteristic** (ROC) compares the relative strength of the **False Positive Rate** (FPR) and **True Postive Rate** (TPR).  

**True Postive Rate** (or, **TPR** / **recall** / **sensitivity**) is the proportion of actual events correctly identified.
  * `TP / (TP + FN) = P(TP | actual 1)`

**False Positive Rate**  (**FPR**) is the proportion of actual non-events **incorrectly** predicted. This is equivalent to one minus the **Specificity** `P(TN | actual 0)`.
  * `FP / (FP + TN) = P(FP | actual 0) = 1 - P(TN | actual 0)`
    
  
<table>
  <tr>
    <th></th>
    <th></th>
    <th colspan="2" style="text-align: center;">Actual</th>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>1</td>
    <td>0</td>
  </tr>
  <tr>
    <td rowspan="2">Predictions</td>
    <td>Positive</td>
    <td style="text-align: center;">TP</td>
    <td style="text-align: center;">FP</td>
  </tr>
  <tr>
    <td>Negative</td>
    <td style="text-align: center;">FN</td>
    <td style="text-align: center;">TN</td>
  </tr>
</table>  
    
**Functions and methods:** 
  
* `np.repeat([0, 1], repeats = [num_neg, num_pos])` - repeat each element of a numpy array.  
* `roc_curve(x, y)` - `sklearn.metrics` class for calculating the false positive rates, true positive rates, and thresholds, given a target x dataset and a predicted y dataset.  


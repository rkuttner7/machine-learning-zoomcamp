## 4.4 Precision and Recall


## Notes

**Precision** (or, **Positive predictive value**) is the proportion of positive predictions that are correct.
  * How many **pre**dicted positives were right?
  * `TP / (TP + FP) = P(TP | +)`.  
  

**Recall** (or, __sensitivity__) is the proportion of actual events that are predicited as positive.
  * How many **re**(c) **al** positives
  * `TP / (TP + FN) = P(TP | actual 1)`
  
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
    
### Further Reading
* `F1 score` Precision and recall are conflicting - when one grows, the other goes down. That's why they are often combined into the F1 score - a metrics that takes into account both.  
This is the formula for computing F1:  
$$F_1 = 2 \cdot \cfrac{P \cdot R}{P + R}$$  
  Where $P$ is precision and $R$ is recall.= `2 * P * R / (P + R)`    
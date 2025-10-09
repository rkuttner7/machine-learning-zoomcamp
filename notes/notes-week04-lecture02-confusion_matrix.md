## 4.3 Confusion table

## Notes

**Confusion table** is a way of measuring different types of errors and correct decisions that binary classifiers can make. Considering this information, it is possible to evaluate the quality of the model by different strategies.  
  
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
    

The **accuracy** corresponds to the sum of **TN** and **TP ** divided by the total of observations.
  
**False Postives**: lose money by giving money to those that are not planning to leave.  
**False Negative**: lose customers by not giving a discount to customers that do leave.  
  
# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model              |   Weight |
|:-------------------|---------:|
| 10_LightGBM        |        3 |
| 12_LightGBM        |        1 |
| 14_CatBoost        |        2 |
| 16_CatBoost        |        2 |
| 2_Default_Xgboost  |        1 |
| 3_Default_CatBoost |        5 |
| 7_Xgboost          |        1 |
| 8_Xgboost          |        1 |

### Metric details:
| Metric   |        Score |
|:---------|-------------:|
| MAE      |   101.189    |
| MSE      | 17634.8      |
| RMSE     |   132.796    |
| R2       |     0.770571 |
| MAPE     |     0.160786 |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)

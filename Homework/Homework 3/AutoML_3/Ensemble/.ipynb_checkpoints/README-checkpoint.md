# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                             |   Weight |
|:----------------------------------|---------:|
| 10_LightGBM                       |        1 |
| 11_LightGBM                       |        1 |
| 14_CatBoost_GoldenFeatures        |        7 |
| 15_CatBoost                       |        1 |
| 27_CatBoost_GoldenFeatures        |        3 |
| 29_CatBoost                       |        2 |
| 2_Default_Xgboost                 |        1 |
| 31_LightGBM_GoldenFeatures        |        5 |
| 32_Xgboost                        |        1 |
| 33_Xgboost                        |        1 |
| 34_Xgboost                        |        3 |
| 3_Default_CatBoost                |        3 |
| 3_Default_CatBoost_GoldenFeatures |        1 |
| 8_Xgboost                         |        1 |

### Metric details:
| Metric   |        Score |
|:---------|-------------:|
| MAE      |   106.231    |
| MSE      | 19301.1      |
| RMSE     |   138.929    |
| R2       |     0.748892 |
| MAPE     |     0.167287 |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)

# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                      |   Weight |
|:---------------------------|---------:|
| 11_LightGBM                |       12 |
| 14_CatBoost_GoldenFeatures |        6 |
| 15_CatBoost                |        6 |
| 17_CatBoost                |       16 |
| 37_NeuralNetwork           |        1 |
| 3_Default_CatBoost         |        1 |
| 44_CatBoost                |        1 |
| 4_Default_NeuralNetwork    |        2 |
| 56_NeuralNetwork           |        7 |
| 9_Xgboost                  |        2 |

### Metric details:
| Metric   |        Score |
|:---------|-------------:|
| MAE      |   131.866    |
| MSE      | 28809.7      |
| RMSE     |   169.734    |
| R2       |     0.625186 |
| MAPE     |     0.193671 |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)

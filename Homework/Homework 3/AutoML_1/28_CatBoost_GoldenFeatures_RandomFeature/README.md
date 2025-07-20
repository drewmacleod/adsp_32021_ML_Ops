# Summary of 28_CatBoost_GoldenFeatures_RandomFeature

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.05
- **depth**: 8
- **rsm**: 0.8
- **loss_function**: RMSE
- **eval_metric**: RMSE
- **explain_level**: 1

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.9
 - **shuffle**: True

## Optimized metric
rmse

## Training time

6.2 seconds

### Metric details:
| Metric   |        Score |
|:---------|-------------:|
| MAE      |   102.121    |
| MSE      | 17575.2      |
| RMSE     |   132.571    |
| R2       |     0.763023 |
| MAPE     |     0.108899 |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)

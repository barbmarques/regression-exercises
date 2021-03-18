# regression-exercises
This repository will store my work for the Regression Module.


### Repo contents:
| File  | Description |
|-------|-------|
| wrangle.ipynb | This Jupyter notebook contains code, visualizations and takeaways from the Acquire and Prep exercises. |
| scaling.ipynb | This Jupyter notebook contains code, visualizations and takeaways from the Preprocessing: Data Scaling module exercises.|
|explore_zillow.ipynb|This Jupyter notebook contains code, visualizations and takeaways from the Explore Stage module exercises.|
|evaluate.ipynb| This Jupyter notebook contains code, visualizations and takeways from the Evaluate module exercises.|
|feature-engineering.ipynb|This Jupyter notebook contains code, visualizations and takeaways from the Feature Engineering module exercises.|
| acquire.py | This file contains the functions: get_telco_charges and clean_telco which acquire data from Codeup's Telco database and return a dataframe containing customer_id, monthly_charges, tenure, and total_charges for all customers with 2 year contracts. Also includes the function train_validate_test_split which splits the data for scaling or modeling
|explore.py|This file contains the functions plot_variable_pairs() and plot_categorical_and_continuous_vars() which return exploration visualizations on categorical and quantitative variables.|
|evaluate.py| Contains the code that defines the following functions: ```plot_residuals(y, yhat)```: creates a residual plot, ```regression_errors(y, yhat)```: returns the following values: sum of squared errors (SSE), explained sum of squares (ESS), total sum of squares (TSS), mean squared error (MSE), root mean squared error (RMSE), ```baseline_mean_errors(y)```: computes the SSE, MSE, and RMSE for the baseline model, ```better_than_baseline(y, yhat)```: returns true if your model performs better than the baseline, otherwise false, ```model_significance(ols_model)```: that takes the ols model as input and returns the amount of variance explained in your model|
|feature_engineering.py| This file contains the functions select_kbest() and rfe() which take in a list of independent variables, or predictors (x), the target variable (y) and the number of features to select (k), fits X_train_scaled and returns (prints) the names of the top k selected features based on the SelectKBest and RFE class.|
| prepare.py | This file contains the function scale() which accepts train, validate and test data splits from the telco_clean data and returns the scaled versions of each.
| wrangle.py | This contains the function wrangle_telco() which accepts train, validate and test data splits from the telco_clean data and returns the scaled versions of each.

***

import numpy as np
import pandas as pd

import statsmodels.api as sm

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def ohe_concat(cat_data, cont_data, cat_list, column):
    '''
    takes categorical, continuous data, and the target feature column. The categorical features are
    one_hot_encode and then concatenated with the continusous features. The new dataset is then split
    into the target feature, y, and the explanatory variables, X. 
    Returns X, y
    '''
    cat_data_ohe = pd.get_dummies(cat_data, columns=cat_list, drop_first=False)
    preprocessed = pd.concat([cat_data_ohe, cont_data], axis=1)
    X = preprocessed.drop(column, axis=1)
    y = preprocessed[column]
    return X, y

def ols_summary(X_train, y_train, X):
    model = sm.OLS(y_train, sm.add_constant(pd.DataFrame(X_train, columns=X.columns, index=X_train.index)))
    results = model.fit()
    return results.summary()

def predictions(model, X_train, X_test, y_train, y_test):
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    R2_train = r2_score(y_train, y_train_pred)
    R2_test = r2_score(y_test, y_test_pred)
    mae_test = mean_absolute_error(y_test, y_test_pred)
    mae_train = mean_absolute_error(y_train, y_train_pred)
    rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
    rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
    print(f'Training Scores: R2 {R2_train:.5f}, Mean Absolute Error {mae_train:.2f}, Root Mean Squared Error {rmse_train:.2f}')
    print(f'Testing Scores: R2 {R2_test:.5f}, Mean Absolute Error {mae_test:.2f}, Root Mean Squared Error {rmse_test:.2f}')


    
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error



def predictions(model, X_train, X_test, y_train, y_test):
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    R2_train = r2_score(y_train, y_train_pred)
    R2_test = r2_score(y_test, y_test_pred)
    mae_test = mean_absolute_error(y_test, y_test_pred)
    rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
    rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
    print(f'Training Scores: R2 {R2_train:.5f}, Mean Absolute Error {mae_train}, Root Mean Squared Error {rmse_train}')
    print(f'Testing Scores: R2 {R2_test}, Mean Absolute Error {mae_test}, Root Mean Squared Error {rmse_test}')
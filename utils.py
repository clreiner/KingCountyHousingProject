
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error



def predictions(model, X_train, X_test, y_train, y_test):
	y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    R2_train = round(r2_score(y_train, y_train_pred), 5)
    R2_test = round(r2_score(y_test, y_test_pred), 5)
    mae_test = round(mean_absolute_error(y_test, y_test_pred), 2)
    rmse_train = round(np.sqrt(mean_squared_error(y_train, y_train_pred)), 2)
    rmse_test = round(np.sqrt(mean_squared_error(y_test, y_test_pred)), 2)

    print(f'Training Scores: R2 {R2_train}, Mean Absolute Error {mae_train}, Mean Squared Error {rmse_train}')
    print(f'Testing Scores: R2 {R2_test}, Mean Absolute Error {mae_test}, Mean Squared Error {rmse_test}')
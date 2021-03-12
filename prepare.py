import sklearn.preprocessing

def scale():
    '''
    This function accepts train, validate and test data splits from the 
    telco_clean data and returns the scaled versions of each.
    '''
    
    x_train = train.drop(columns = ['customer_id'],axis=1)
    x_validate = validate.drop(columns = ['customer_id'],axis=1)
    x_test = test.drop(columns = ['customer_id'],axis=1)
    
    scaler = sklearn.preprocessing.MinMaxScaler()
    scaler.fit(x_train)

    x_train_scaled_inv = scaler.inverse_transform(x_train)
    x_validate_scaled_inv = scaler.inverse_transform(x_validate)
    x_test_scaled_inv = scaler.inverse_transform(x_test)
    
    return train_scaled, validate_scaled, test_scaled
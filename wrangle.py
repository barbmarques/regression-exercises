import pandas as pd
import numpy as np
import env
from sklearn.model_selection import train_test_split

# Define helper function to create connection url
def get_connection(db, user=env.user, host=env.host, password=env.password):
    '''
    This function uses information from env to create
    a url to connect and access the Codeup database.'''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# Employs a helper function and sql query to obtain telco data
def get_telco_charges():
    '''
    This function reads data from Codeup's Telco database and 
    returns a dataframe containing customer_id, monthly_charges,
    tenure, and total_charges for all customers with 2
    '''
    telco_sql = "SELECT customer_id, tenure, monthly_charges, total_charges \
                 FROM customers \
                 WHERE contract_type_id = 3"
    return pd.read_sql(telco_sql, get_connection('telco_churn'))

# Cleans telco_data 
def clean_telco(df):
    '''
    clean the two year contract data, replacing missing total_charges with zeros 
    '''
    df['total_charges'] = df['total_charges'].replace(r'^\s*$', np.nan, regex=True)
    df.assign(total_charges=df.total_charges.fillna(0))
    df.total_charges=pd.to_numeric(df.total_charges, errors='coerce').astype('float64')
    return df

def train_validate_test_split(df, target, seed=123):
    
    '''
    This function splits the telco data into train, 
    validate and test data sets to use in classification
    modeling
    
    '''
    train_and_validate, test = train_test_split(
        df, test_size=0.2, random_state=seed)
    train, validate = train_test_split(
        train_and_validate,
        test_size=0.3,
        random_state=seed)
    
    # split train into X (dataframe, drop target) & y (series, keep target only)
    X_train = train.drop(columns=[target])
    y_train = train[target]
    
    # split validate into X (dataframe, drop target) & y (series, keep target only)
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]
    
    # split test into X (dataframe, drop target) & y (series, keep target only)
    X_test = test.drop(columns=[target])
    y_test = test[target]

    return X_train, y_train, X_validate, y_validate, X_test, y_test

def create_dummies(df, object_cols):
    '''
    This function takes in a dataframe and list of object column names,
    and creates dummy variables of each of those columns. 
    It then appends the dummy variables to the original dataframe. 
    It returns the original df with the appended dummy variables. 
    '''
    
    # run pd.get_dummies() to create dummy vars for the object columns. 
    # we will drop the column representing the first unique value of each variable
    # we will opt to not create na columns for each variable with missing values 
    # (all missing values have been removed.)
    dummy_df = pd.get_dummies(object_cols, dtype=int)
    
    # concatenate the dataframe with dummies to our original dataframe
    # via column (axis=1)
    df = pd.concat([df, dummy_df], axis=1)

    return df

def wrangle_telco():
    '''
    wrangle_telco will read in our telco data via a sql query, clean the data
    down to monthly_charges, total_charges, tenure, and customer_id, 
    replace whitespace values in total_charges with zeros where appropriate

    return: train, validate, and test sets of telco data
    '''
    df = clean_telco(get_telco_charges())
    return train_validate_test_split(df)
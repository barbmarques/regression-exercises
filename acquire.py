import pandas as pd
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

def train_validate_test_split(df, seed=123):
    
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
    return train, validate, test


def wrangle_telco():
    '''
    wrangle_telco will read in our telco data via a sql query, clean the data
    down to monthly_charges, total_charges, tenure, and customer_id, 
    replace whitespace values in total_charges with zeros where appropriate

    return: train, validate, and test sets of telco data
    '''
    df = clean_telco(wrangle.get_telco_charges)
    df = train_validate_test_split(df)
    return
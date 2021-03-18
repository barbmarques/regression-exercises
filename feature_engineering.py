from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.feature_selection import SelectKBest, f_regression

def select_kbest(predictors, target, k): 

    '''
    This function takes in a list of independent variables, or predictors (x), the target
    variable (y) and the number of features to select (k), fits  X_train_scaled and returns
    (prints) the names of the top k selected ffeatures based on the SelectKBest class.
    ''' 

    # parameters: f_regression stats test, return k number of features
    f_selector = SelectKBest(f_regression, k=k)

    # find the top k X's correlated with y
    f_selector.fit(X_train_scaled, y_train)

    # boolean mask of whether the column was selected or not. 
    feature_mask = f_selector.get_support()
    
    # get list of top K features. 
    f_feature = X_train_scaled.iloc[:,feature_mask].columns.tolist()
    
    print(f'The {k} best predictors of {target}, according to k best are: {f_feature}.')
    return
# _________________________________________________________________________________________

def rfe(predictors, target, k): 
    
    '''
    This function takes in a list of independent variables, or predictors (x), the target
    variable (y) and the number of features to select (k), fits X_train_scaled
    and returns (prints) the names of the top k selected features based on the RFE class.
    ''' 

    # initialize the ML algorithm
    lm = LinearRegression()

    # create the rfe object, indicating the ML object (lm) and the number of features I want to end up with. 
    rfe = RFE(lm, k)

    # fit the data using RFE
    rfe.fit(X_train_scaled,y_train)  

    # get the mask of the columns selected
    feature_mask = rfe.support_

    # get list of the column names. 
    rfe_feature = X_train_scaled.iloc[:,feature_mask].columns.tolist()

    print(f'The {k} best predictors of {target}, according to recursive feature elimination are: {rfe_feature}.')
    return


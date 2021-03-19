def plot_residuals(y, yhat):
    
    '''
    This function takes in  y and yhat values and returns 
    a residual plots.
    '''
    
    # calculating residuals
    df['residual'] = y - df.yhat
    df['baseline_residual'] = y - df.baseline
    
    # plot residuals of model
    mplot = plt.scatter(x, df.residual)
    plt.axhline(y = 0, ls = ':')
    plt.title('OLS model residuals');

    return 



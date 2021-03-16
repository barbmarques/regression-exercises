import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from scipy import stats


def plot_variable_pairs(df):
    '''
    
    This function will take in a data frame and return a pair plot with lines of
    regression comparing variable pairs of the data set.
    
    '''
    
    g = sns.PairGrid(df)
    g.map_diag(plt.hist)
    g.map_offdiag(sns.regplot)
    return g
    
def plot_categorical_and_continuous_vars(df, cat_vars, quant_vars):
        
    '''
    
    This function will take in a dataframe, categorical and quantitative variables and
    return a boxplot and a jointplot comparing variables, as well as a heatmap showing correlation
    coefficients.
    
    '''

    #create boxplot
    bp = sns.boxenplot(x = cat_vars, y = quant_vars, data=df) 
    plt.show  

    # create heatmap
    corr = df.corr()
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    f, ax = plt.subplots(figsize=(12, 10))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    hm = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.9, center=0, square=True, linewidths=.5, annot=True)

    #create jointplot
    jp = sns.jointplot(x=cat_vars, y=quant_vars, data=df,kind='resid')
    plt.show
  
    return 
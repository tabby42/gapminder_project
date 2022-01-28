import numpy
import matplotlib.pyplot as plt
import pandas as pd

def get_num_countries(datasets, names):
    for i, val in enumerate(datasets):
        print('Number of countries in {}: {}'.format(names[i], val.country.nunique()))

def get_missing(data):
    #save num of missing values in new column 
    data['missing'] = data.iloc[:, 1:].apply(lambda x: x.isna().sum() if numpy.any(x.isna()) else 0, axis=1)
    #filter for values < 0 
    filtered = data['missing'][data['missing'] != 0]
    ctries = data['country'][data['missing'] != 0]
    #drop 'missing' column
    data.drop(columns=['missing'], inplace=True)
    return (filtered, ctries)

def plot_missing(data, x_values, x_labels, set_name):
    #plot bar chart
    x_values.plot(kind='bar', color=(0.2, 0.4, 0.6, 0.6))
    plt.xticks(numpy.arange(0, len(x_values)), x_labels)
    #label the axes and set title 
    plt.xlabel('Country')
    plt.ylabel('Number of missing values')
    plt.title(('Missing values per country in {} data').format(set_name), fontsize=13, fontweight='bold')
    
def cut_suffix_tonumber(x):
    #check last char, cut last char, convert to float, 
    #multiply depending if last char is 'M', 'k' or 'B'
    #if no letter-suffix, just convert to float 
    if x[-1:] == 'M':
        return pd.to_numeric(x[:-1]) * 1000000
    elif x[-1:] == 'k':
        return pd.to_numeric(x[:-1]) * 1000
    elif x[-1:] == 'B':
        return pd.to_numeric(x[:-1]) * 1000000000
    else:
        return pd.to_numeric(x[:-1])
import numpy
import matplotlib.pyplot as plt

def get_num_countries(datasets, names):
    for i, val in enumerate(datasets):
        print('Number of countries in {}: {}'.format(names[i], val.country.nunique()))

def get_missing(data):
    #save num of missing values in new column 
    data['missing'] = data.iloc[:, 1:].apply(lambda x: x.isna().sum() if numpy.any(x.isna()) else 0, axis=1)
    #filter for values < 0 
    filtered = data['missing'][data['missing'] != 0]
    ctries = data['country'][data['missing'] != 0]
    #return filtered data
    return (filtered, ctries)

def plot_missing(data, x_values, x_labels, set_name):
    #plot bar chart
    x_values.plot(kind='bar', color=(0.2, 0.4, 0.6, 0.6))
    plt.xticks(numpy.arange(0, len(x_values)), x_labels)
    #label the axes and set title 
    plt.xlabel('Country')
    plt.ylabel('Number of missing values')
    plt.title(('Missing values per country in {} data').format(set_name), fontsize=13, fontweight='bold')
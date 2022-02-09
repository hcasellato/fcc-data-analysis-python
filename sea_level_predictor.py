import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('data/epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    plt.plot(np.arange(1880, 2051, 1), [slope*i + intercept for i in np.arange(1880, 2051, 1)], 'r')

    # Create second line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x=(df['Year'][df['Year'] >= 2000]), y=(df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000]))
    plt.plot(np.arange(2000, 2051, 1), [slope*i + intercept for i in np.arange(2000, 2051, 1)], 'g')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Ran 4 tests in 0.639s ºoº
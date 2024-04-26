import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epsa-seas-level.csv')


    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Original Data')


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    plt.plot(data['Year'], intercept + slope*data['Year'], 'r', label='Best Fit Line (All Data)')
    plt.plot(range(1880, 2051), intercept + slope*range(1880, 2051), 'r--')


    # Create second line of best fit
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    plt.plot(recent_data['Year'], intercept_recent + slope_recent*recent_data['Year'], 'g', label='Best Fit Line (2000 onwards)')
    plt.plot(range(2000, 2051), intercept_recent + slope_recent*range(2000, 2051), 'g--')
    


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
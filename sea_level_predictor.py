import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.5, label='Observed Data')


    slope_all, intercept_all, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended_all = np.arange(df["Year"].min(), 2051)
    sea_level_pred_all = intercept_all + slope_all * years_extended_all

    # Create first line of best fit
    plt.plot(years_extended_all, sea_level_pred_all, color="red", label="Best Fit Line (1880-2050)")
    df_2000 = df[df["Year"] >= 2000]    
    slope_2000, intercept_2000, _, _, _ = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    years_extended_2000 = np.arange(2000, 2051)
    sea_level_pred_2000 = intercept_2000 + slope_2000 * years_extended_2000

    # Create second line of best fit
    plt.plot(years_extended_2000, sea_level_pred_2000, color="green", label="Best Fit Line (2000-2050)")


    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
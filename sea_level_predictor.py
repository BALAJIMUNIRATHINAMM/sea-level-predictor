import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import os

def draw_plot():
    """
    Reads the sea level data, creates a scatter plot, fits two linear regressions 
    (1880-2050 and 2000-2050), and saves the plot.
    """

    # Load dataset
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "epa-sea-level.csv")
    df = pd.read_csv(data_path)

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Sea Level Data")

    # Line of best fit for entire dataset (1880 - 2050)
    slope, intercept, _, _, _ = stats.linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = np.arange(1880, 2051)
    sea_levels = slope * years_extended + intercept
    plt.plot(years_extended, sea_levels, 'r', label="Best Fit (1880-2050)")

    # Line of best fit for recent data (2000 - 2050)
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = stats.linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = np.arange(2000, 2051)
    sea_levels_recent = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, sea_levels_recent, 'g', label="Best Fit (2000-2050)")

    # Labels, title, and legend
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save the plot
    output_path = os.path.join(os.path.dirname(__file__), "..", "sea_level_plot.png")
    plt.savefig(output_path)

    return plt

if __name__ == "__main__":
    draw_plot()

##############################################
# Title: Exponential Smooth Moving Average (SMA)
# Date: 05/22/2017
# Author: Christopher Ried
# Purpose: The algorithm generates a time series (TS) visual
# that defines the degree of movement within the data.
# Essentially the algorithm give us a double derivative
# of the TS providing a signal that can be analyzed.
##############################################

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def generate_exponential_sma(data, window):
    """
    Generates eSMA from data

    Parameters
    ----------
    data : DataFrame object
        ts Series object 
        
    window : int 
        sliding window function

    Returns
    -------
    DataFrame
        ts exponential SMA result
    """
    return data.ewm(span=window).mean()


def import_clean_ts(filename):
    """Read and selects ts data"""
    ts_data = pd.read_csv(filename)

    # Sort data for clarity
    ts_data['Date'] = pd.to_datetime(ts_data['Date'])
    return ts_data.sort_values(by='Date')


def collect_user_input(window_default):
    """Collect window from user or default """
    user_input = input(format('Enter Long Term Window or Enter to Default ({0} Weeks):'.format(window_default)))
    if user_input == '':
        user_input = window_default

    return int(user_input * 5)  # Generate window by days


def main():
    stock = import_clean_ts("data/goog.csv")  # TODO: Input from ARGV
    data = pd.Series(np.float32(stock['Close']), index=stock['Date'])

    lt_av = generate_exponential_sma(data, collect_user_input(4))  # Generate eSMA
    st_av = generate_exponential_sma(data, collect_user_input(2))

    diff_ltst = lt_av - st_av  # First Derivative
    diff_ltst_av = generate_exponential_sma(diff_ltst, 7.5)
    diff_av_diff = diff_ltst_av - diff_ltst  # Second Derivative

    # Display plot to user
    plt.show(diff_av_diff.plot(style='k', title="2nd Derivative GOOG Close Price"))


if __name__ == '__main__':
    main()

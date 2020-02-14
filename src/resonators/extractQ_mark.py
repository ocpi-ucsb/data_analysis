import numpy as np
import scipy.optimize
import os
import sys

import pandas as pd

def import_data(path):
    # import from path
    # path can just depend on the "established user" example Andrei
    # establish the fields
    # create a pandas data frame
    df = 0 # pandas dataframe
    return df


def analyze_data(df):
    # import the dataframe
    # do a quality factor fit
    
    results = 0 # dictionary of the extracted values and the uncertainties
    plotObj = 0 # plot object that is used to represent the data and/or the fit results
    return results, plotObj

def plotting(plotObj, df, style, fit_or_data, fudge):
    # plot using matplotlib
    # user can choose if plot data and/or fitted curves
    # style is a package that will nicely plot the data
    # fudge are other random things that the user can make specific

if __name__ == "__main":
    path = 'default_path'
    
    df = import_data(path)

    results, plotObj = analyze_data(df)

    plotting(plotObj, df, style='andrei', fit_or_data = 'fit_and_data', fudge = 'IEEE_colors')

    # end

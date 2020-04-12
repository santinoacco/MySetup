#!/usr/bin/env python3

# here I will store my useful functions

import numpy as np
import pandas as pd
#import ROOT as r
#import SwanImports


import argparse
def config_Parse():
    """
    Set all the configuration to your parser object.

    # Args::None

    # Returns::parser object.
    """
    parser = argparse.ArgumentParser('<Name>')
    parser.add_argument('-I', '--Input', required=True, help='<Input folder or file/s>' )
    parser.add_argument('-O', '--Output', required=True, help='<Output folder or files/s>')
    parser.add_argument('-D','--Debug', required=False, help='Debug flag', action='store_true')
    parser.add_argument('-M','--MaxEvents', required=False, help='Set maximum of events. Default -1 == all', type=int, default=-1)
    return parser

# == create dir
from os import mkdir
from os.path import join
def build_dir(Dir_name,File_name,Extension):
    assert type(Dir_name) == str, 'Dir_name must be a string'
    assert type(Extension) == str, 'Extension must be a string'
    try: mkdir(Dir_name)
    except: pass
    outfile = join(Dir_name,File_name+Extension)
    return outfile

# == Plots
import matplotlib.pyplot as plt
import seaborn as sns
def my_seaborn_style():
    pass

def my_plt_style(plot_obj):
    pass
    #assert(type(plot_obj) == plt.figure.Figure), 'check plot_obj type'
    #plot_obj.set_xlabel 
    #return

#def my_plotter_2D(plot_name, x_data, y_data, param_dict):
def my_plotter_2D(ax, x_data, y_data, param_dict):
    """
        A helper function to make a graph

        Parameters
        ----------
        ax : Axes
            The axes to draw to

        data1 : array
           The x data

        data2 : array
           The y data

        param_dict : dict
           Dictionary of kwargs to pass to ax.plot

        Returns
        -------
        out : list
            list of artists added
    """
    #common_plots = {
    #        'plot':ax.plot, 'scatter':ax.scatter,
    #        'errorbar':ax.errorbar, 'date':ax.plot_date,
    #        'hist':ax.hist
    #        }

    #out = common_plots[plot_name](x_data, y_data, **param_dict)
    out = ax.plot(x_data, y_data, **param_dict)
    #ax = out.gca()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()

    return out
# ===== ROOT ===== #


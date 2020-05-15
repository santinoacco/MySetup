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

_default_cmap = plt.get_cmap('tab20c')

_default_style={
        'plot':{
            'marker':'o',
            'mfc':'none',
            'color':'blue',
            'linestyle':'--'
            },
        'date':{
            'marker':'H',
            'mfc':'none',
            'color':'green',
            'linestyle':'--',
            'linewidth':3,
            },
        'hist':{
            'density':True,            #--> normalized histogram
            'align':'mid',             #--> place ticks in the middle
            'histtype':'stepfilled',   #--> type
            'color':'DarkBlue',        #--> linecolor
            'linestyle':'-',
            'linewidth':2,
            'alpha':0.5,               #--> how strong the shading of the filling is
            'edgecolor':'DarkBlue',
            'facecolor':'LightBlue',   #--> color of the shading
            },
        'pie':{
            'shadow':True,
            'autopct':'%1.1f%%',
            'radius':1.0,
            'wedgeprops':{'width':0.75,'edgecolor':'w'}
            },
        }

def mplotter_2D(plot_name, ax, x_data, y_data, xlabel=None, ylabel=None,title=None, param_dict=None):
    """
        A helper function to make a graph

        Parameters
        ----------
        ax : Axes

        x_data : array
           The data along the x-axis

        data2 : array
           The data along the y-axis

        param_dict : dict
           Dictionary of kwargs to pass to ax.plot

        Returns
        -------
        out : list
            list of artists added
    """
    if param_dict == None:
        param_dict = m_default_param_dict[plot_name]

    common_plots = {
           'plot':ax.plot,
           'scatter':ax.scatter,
           'errorbar':ax.errorbar,
           'date':ax.plot_date,
           'hist':ax.hist,
           }
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set(title=title)
    ax.legend()
    out = common_plots[plot_name](x_data, y_data, **param_dict)

    return out

def mplot(ax,x,y,label,yerr=np.nan,xerr=0,style_dict=None):
    if style_dict==None:
        style_dict = _default_style['plot']
    out = ax.errorbar(
            x=x,
            y=y,
            label=label,
            yerr=yerr,
            #xerr=xerr,
            **style_dict,
            )

    return out

def mpie(ax,data, labels, title, colors=None,style_dict=None):
    if type(colors) == None:
        colors = _default_cmap(np.arange(len(labels)))
    if style_dict==None:
        style_dict = _default_style['pie']
    out_pie = ax.pie(
            data,
            labels=labels,
            colors=colors,
            **style_dict
                    )
    ax.set(title=title)

    return out_pie

def mhist(ax,x,label,bins=None,bin_num=None,yerr=None,xerr=None,style_dict=None):
    """My default histogram"""
    if type(bin_num)==None:
        bin_num=10

    if type(bins)==None:
        max_bin = max(x)
        min_bin = min(x)
        step = (max_bin - min_bin)/bin_num
        bins = np.arange(start=min_bin,stop=max_bin,step=int(step))

    if style_dict==None:
        style_dict = _default_style['hist']

    # -- Build histogram
    entries,bins,patches = ax.hist(x=x,label=label,bins=bins,**style_dict)

    # -- Add errorbar
    bin_centers = 0.5*(bins[:-1] + bins[1:])
    ax.errorbar(
            bin_centers, entries, yerr=yerr,xerr=xerr,
            label='Error bar',
            fmt='r.',
            ecolor='Orange',
            )


    return entries,bins,patches

def plot_multiple():
    pass

# == Interactive Plots
# import altair as alt


# ===== ROOT ===== #

# ===== add to Excel ===== #
def append_to_excel(dict_of_DF, file_to_write, sheetname, last_month_loaded):
    '''
    Save data from a dict_of_DF to an Excel file

    Parameters
    ----------
    dict_of_DF : dict
        keys are months in Spanish, contains pd.DataFrame.
    file_to_write : str
        Excel file path to write data on.
    sheetname : str
        Excel sheet name to write data on.
    last_month_loaded : int
        number of the last month with records.

    Returns
    -------
    None.

    '''
    writer = pd.ExcelWriter(
            file_to_write,
            engine='openpyxl',
            mode='a',
            date_format='DD/MM/YYYY'
            )

    # -- Read workbook from file
    book = load_workbook(file_to_write)
    writer.book = book
    # -- Get the info of the existing sheets
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)


    from_month = Meses[last_month_loaded]
    col_step = len(dict_of_DF[from_month].columns) + 1
    init_col = last_month_loaded*col_step

    sub_key_list = [k for k in dict_of_DF.keys()][last_month_loaded:]


    for month in sub_key_list:
        assert len(dict_of_DF[month])!=0, f'month {month} is empty'
        dict_of_DF[month].to_excel(
                writer,
                sheet_name=sheetname,
                startrow=1,
                startcol=init_col
                )

        init_col+=col_step


    writer.save()
    print(f'>>> Successfully loaded data to {file_to_write}')
    return

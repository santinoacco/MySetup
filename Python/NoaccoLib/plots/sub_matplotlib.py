#!/usr/bin/env python3
#=============#
# Author: Santiago Noacco Rosende
# Contact: snoaccor@cern.ch
# GitLab:https://gitlab.cern.ch/snoaccor
# GitHub:https://github.com/santinoacco
#=============#
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


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

def mplotter_2D(plot_name, ax, x_data, y_data,
                xlabel=None, ylabel=None,title=None,
                param_dict=None,
                fontsize=16,):
    """
        A helper function to make a graph

        # Args
            - ax : Axes

            - x_data : (array)
                The data along the x-axis

            - data2 : (array)
                The data along the y-axis

            - param_dict : (dict)
                Dictionary of kwargs to pass to ax.plot

        # Returns
            - out : (list)
                list of artists added
    """
    if param_dict == None:
        # param_dict = m_default_param_dict[plot_name]
        param_dict = _default_style[plot_name]

    common_plots = {
           'plot':ax.plot,
           'scatter':ax.scatter,
           'errorbar':ax.errorbar,
           'date':ax.plot_date,
           'hist':ax.hist,
           }
    ax.set_xlabel(xlabel,fontsize=fontsize)
    ax.set_ylabel(ylabel,fontsize=fontsize)
    ax.set(title=title,fontsize=fontsize+2)
    ax.legend(fontsize=fontsize)
    out = common_plots[plot_name](x_data, y_data, **param_dict)

    return out

def mplot(ax,x,y,label,yerr=np.nan,xerr=np.nan,**style_dict):
# def mplot(ax,x,y,label,yerr=np.nan,xerr=np.nan,**kwargs):
# def mplot(ax,x,y,label,yerr=np.nan,xerr=np.nan,style_dict=None):
    if style_dict is None:
        style_dict = _default_style['plot']
    # if kwargs is None:
        # kwargs = _default_style['plot']
    out = ax.errorbar(
            x=x,
            y=y,
            label=label,
            yerr=yerr,
            xerr=xerr,
            **style_dict,
            )

    return out

def mpie(ax, data, labels, colors=None, style_dict=None):
    if colors is None:
        colors = _default_cmap(np.arange(len(labels)))
    if style_dict is None:
        style_dict = _default_style['pie']
    out_pie = ax.pie(
            data,
            labels=labels,
            colors=colors,
            **style_dict
                    )
    ax.set(title=title,fontsize=16)

    return out_pie

def mhist(ax,x,label,bins=None,bin_num=None,yerr=None,xerr=None,style_dict=None):
    """
    My default histogram

    # Returns:
        - entries:
        - bins:
        - patches:
    """
    if bin_num is None:
        bin_num=10

    if bins is None:
        max_bin = max(x)
        min_bin = min(x)
        step = (max_bin - min_bin)/(bin_num+1)
        bins = np.arange(start=min_bin,stop=max_bin,step=int(step))

    if yerr is None:
        # -- Asume Poisson dist. for bins
        yerr = np.sqrt(len(x))

    if style_dict==None:
        style_dict = _default_style['hist']

    # -- Build histogram
    entries,bins,patches = ax.hist(x=x,label=label,bins=bins,**style_dict)

    # -- Add errorbar
    bin_centers = 0.5*(bins[:-1] + bins[1:])
    ax.errorbar(
            bin_centers, entries, yerr=yerr,xerr=xerr,
            # label='Error bar',
            fmt='r.',
            ecolor='Orange',
            )
    return entries,bins,patches

def plot_multiple():
    pass


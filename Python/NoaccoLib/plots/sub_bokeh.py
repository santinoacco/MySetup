#!/usr/bin/env python3
#=============#
# Author: Santiago Noacco Rosende
# Contact: snoaccor@cern.ch
# GitLab:https://gitlab.cern.ch/snoaccor
# GitHub:https://github.com/santinoacco
#=============#
import bokeh

g_fig_sty = dict(x_axis_type='datetime',plot_width=800,
                #  tools=['pan,wheel_zoom',hover],
                 tools=['pan,wheel_zoom']
                 )

class Errorbars(object):
    pass

class Compound_plots(object):
    """Handles templates plots with multiple figures"""
    def __init__(self,):
        self.ind_num = number_individual_figs;
        self.fig_arr = self._init_figures()

    def _init_figures(self):
        fig_arr = [bokeh.plotting.figure() for f in range(self.ind_num)]
        return fig_arr


class TwoOnCol(Compound_plots):

    @property
    def top(self):
        return top_figure
    @property
    def bottom(self):
        return bottom_figure
    def show(self):
        show(bokeh.layouts.column(self.top,self.bottom))

class ScatterAndHist(TwoOnCol):
    pass

fig_top = figure(title="AMD", plot_height=350,**g_fig_sty)
# -- Add 'above' and 'right' axes to xaxis and yaxis list respectively.
fig_top.add_layout(LinearAxis(axis_label=None),"above")
fig_top.add_layout(LinearAxis(axis_label=None,),"right")
# -- Make them label-less
fig_top.xaxis[0].formatter = bokeh.models.PrintfTickFormatter(format="")
fig_top.yaxis[1].formatter = bokeh.models.PrintfTickFormatter(format="")
# -- Configure X-axis
fig_top.xaxis[1].axis_label = 'Time'
fig_top.xaxis[1].formatter.days = "d%m%\n%Y"
# print(fig_top.xaxis[0].__dir__())

# fig_top.xaxis[0].formatter = DatetimeTickFormatter()
# -- Configure Y-axis
fig_top.yaxis[0].axis_label = 'Price'
# -- Configure Grid
fig_top.xgrid.grid_line_color=None
fig_top.ygrid.grid_line_alpha=0.5
# -- Add tendency plot
fig_top.line(x=amd_DF.index, y=amd_DF.MidRangeHL,
             line_dash='dotted',
             line_color='black',
             )
fig_top.triangle(x=amd_DF.index, y=amd_DF.MidRangeHL,
               fill_color='white',
               line_color='black',
               size=5,
               )
# -- Add Max/Min price plot
fig_top.segment(
    x0=amd_DF.index, y0=amd_DF.Low,
    x1=amd_DF.index, y1=amd_DF.High,
    line_color='red'
    )
# -- Add Close price plot
fig_top.circle(x=amd_DF.index, y=amd_DF.Close,
               fill_color='white',
               size=5,
               )
# ref_line = fig_top.line(x=amd_DF.index, y=amd_DF.Close,
#                         line_color='violet')
# fig_top.add_tools(HoverTool(tooltips=None, renderers=[ref_line], mode='hline'))

# -- Add Volume plot
fig_bottom = figure(plot_height=int(350/2),
                    x_range=fig_top.x_range,
                    **g_fig_sty)
fig_bottom.add_layout(LinearAxis(axis_label=None),"above")
fig_bottom.add_layout(LinearAxis(axis_label=None),"right")
fig_bottom.step(x=amd_DF.index, y=amd_DF.Volume)
fig_bottom.yaxis[0].axis_label = 'Volume'


# -- Show them together
show(column(fig_top,fig_bottom))


# moved from NoaccoLibrary.
from bokeh.io import output_notebook, show
from bokeh.plotting import figure
from bokeh.models import LinearAxis, DatetimeTickFormatter
# output_notebook()
def initBokeh(h,w,xlabel,ylabel):
    """
    Description

    # Args::
        h: plots height
        w: plots width

    # Returns::
        fig: bokeh.plotting.figure obj.
    """
    fig = figure(
            title=title,
            plot_height=h,
            plot_width=w,
            )
    # -- Set axes
    # -- Add "above" and "right" axes
    fig.add_layout(LinearAxis(axis_label=None),"above")
    fig.add_layout(LinearAxis(axis_label=None),"right")
    # -- Configure X-axis
    fig.xaxis[1].axis_label = xlabel
    # -- Configure Y-axis
    fig.yaxis[0].axis_label = ylabel

    # -- Add Line
    fig.line(x,y,
            line_dash='dotted',
            line_color='black'
            )
    # -- Add Scatter
    fig.circle(x,y,
            fill_color='white',
            size=5
            )


    return fig


#!/usr/bin/env python3

# here I will store my useful functions

import numpy as np
import pandas as pd
import ROOT as r
from array import array
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


def get_errorbars_from_npHisto(histo,yerr):
    """
    given a NumPy histogram and errors array will return the coordinates ready to be use in a plt.errorbar
    """
    values, bin_edges = histo
    # 20 bins -> 21 edges
    xL = bin_edges[:-1]
    xH = bin_edges[1:]
    # bin center is at (bin[i] + bin[i+1])/2 + bin[i],
    # since it's increasing order.
    xC = bin_edges[:-1] + np.diff(bin_edges)/2
    if len(values)==len(yerr):
        # then errors are simetric.
        yL = values - yerr/2
        yH = values + yerr/2
    else:
        raise NotImplementedError

    Xvalues = (xL,xC,xH)
    Yvalues = (yL,values,yH)
    return Xvalues, Yvalue

# ===== ROOT ===== #
def createT1(name, bins):
    """

    # Returns:
        ROOT.TH1F histogram
    """
    binarray = array('d', bins)
    h = r.TH1F(name,name,len(bins),bins[0],bins[-1])
    h.SetBins(len(bins)-1, binarray)
    return h

def mROOT_style():
    pass

def npHisto2TH1F(np_histo,errors,name,debug=False):
    """takes values(counts) and bin-edges to return a ROOT.TH1F obj"""
    # -- check type
    # assert isinstance(np_histo,np.histogram)
    # get values, bin-edges
    values, bins = np_histo
    nbins = len(bins)
    # -- init TH1F
    out_th1f = ROOT.TH1F(name, # name
                         name, # title
                         nbins,# number of bins
                         bins  # bin edges
                        )
    for b in range(nbins-1):
        out_th1f.SetBinContent(b,values[b])
        if debug:
            print(f"Filling bin {b} with value {th1f_A.GetBinContent(b)}")

    return out_th1f

# IN PROGRESS:
def mTplot(TObject):
    # -- Different behaviour regarding number of TObjects passed
    if len(TObject)>1: pass
    TObject.SetLineColor(r.kBlue-3)
    TObject.SetLineStyle()
    TObject.SetTitle()
    # TObject.Ge

    return

# ===== add to Excel ===== #

def extract_trend(x,method):
    """
    Use the `method` to extract the trend from a TimeSerie x.
    method: "moving_avg", "wgt_moving_avg","center_moving_avg", "fft_decomp"
    """
    pass


def errors_from_covmatrix():
    pass


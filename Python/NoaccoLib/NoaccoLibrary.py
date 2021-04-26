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

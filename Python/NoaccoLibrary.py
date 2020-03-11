#!/usr/bin/env python3

# here I will store my useful functions

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ROOT as r
import SwanImports



def Config_Parse():
     
    parser = argparse.ArgumentParser('<Name>')
    parser.add_argument('-I', '--Input', required=True, help='<Input folder or file/s>' )
    parser.add_argument('-O', '--Output', required=True, help='<Output folder or files/s>')
    parser.add_argument('-D','--Debug', required=False, help='Debug flag', action='store_true')
    parser.add_argument('-M','--MaxEvents', required=False, help='Set maximum of events. Default -1 == all', type=int, default=-1)
    #parser.add_argument('-e','--EtaBins', required=False, help='Eta Bins', type=float,
    #        default=[ -2.37, -2.01, -1.81, -1.52, -1.37, -1.15, -0.8 , -0.6 , 0    , 0.6  , 0.8  , 1.15 , 1.37 , 1.52 , 1.81 , 2.01 , 2.37] )
    #parser.add_argument('-p','--PtBins', required=False, help='Pt Bins', type=float,
    #        default= [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 75, 80])
    return parser



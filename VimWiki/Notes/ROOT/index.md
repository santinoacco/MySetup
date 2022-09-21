# Tips and Tricks on how to use ROOT

-   Documentation to a `<CLASS>`:
    -   root.cern.ch/root/html/<CLASS>.html
-   When using PyRoot, to access an xAOD:
    - You need to set the env as: asetup AnalysisBase,master,latest (you can change the release of course)
    - ROOT.xAOD.Init().ignore()
   
   
https://its.cern.ch/jira/browse/ATR-22875 
 Run3 DQ, TupPhysVal, Hgam:
PowhegPythia8EvtGen_NNLOPS_nnlo_30_ggH125_gamgam no pileup

PowhegPythia8EvtGen_NNLOPS_nnlo_30_ggH125_gamgam with pileup

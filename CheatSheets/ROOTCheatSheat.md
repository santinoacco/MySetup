To get the keys from a file:
--------------------------
f=ROOT.TFile("<filename>")
storage=[]
for k in f.GetListOfKeys():
    kname = k.GetName() # you may have to specify that kname shall be a str type.
    storage.append(f.Get(kname))

**************************
To get objects from a file:
f.Get(<obj name>)

To see whats inside a file:
f.ls()

To set a file as a ROOT Macro:
<file>.C

To run a ROOT Macro:
.x <file>


**************************
Using ROOT in Python3
**************************
to define trees, branches and variables
lib needed
import ROOT as r
from array import array

tree = r.TTree('<name>','<name>')
var = array('var')

#create a TBranch and save data

tree.Branch('<branch_name>',var,'<branch_name>/<type>')


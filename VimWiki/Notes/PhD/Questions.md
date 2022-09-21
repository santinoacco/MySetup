# Questions and Answers

## 
* [DONE] What are the original data samples to the Zllyathderivation

## NTuple
* [ONGOING] What type of files does NTuple accepts? output of Zllyathderivation

* [] What is an "inline void <method>"

* [DONE] What is the "T" parameter stored?
* -> I think it's the time the cell was measured.

* [DONE] Why do you store "X", "Y", "Z"? position coordinates

* [] What is he doing with the fChain->SetBranchAddress and later fChain->Branch? Is he taking the input chain and reshsping it to output it with more information? 

* [] When reshaping the clusters that don't have the expected size, how do you know what cells to chop?

* [] I don't understand if clusters are normalized or not, because NormalizeCluster is commented.

* [] Why is "ph_isIsoTightWP" required for all cluster data?

* [] Where does cell-data come from?

## Array

* [] Why do you need to convert NTuple -> NumPyArray -> NumPyMatrix?

* [] in Array/NTupleToNumpy what is the shape of "data"?https://gitlab.cern.ch/mobelfki/cnn-photon-id/-/blob/master/Array/NTupleToNumpy.py#L44

* [] Not quite sure what `NTupleToNumpy.Execute` does. Seems that saves each cell in a np.array and then that flat cluster in one of 3 containers X1, X2 or X3. But what is the argument to divide into 3 arrays? (lines 50 - 64). In particular, what is going on in line 58 when setting the array slice to "-48", why??

* [] I think that CellsToImage should be part of this module because it preforms a transformation on the output files of Array, that must be in the same output folder as Array output in order to the training to Work. The issue is that Data and CNNData load the files from the same and unique Dir source, therefore the output Dirs of Array and CellsToImage must be the same, and in such case why should be CellsToImage a different module?

## DataProcessing

* [] Perhaps this module should be global, meaning same level as Array, NTuple, etc

* [DONE] What are the SSVar? ShowerShape variables

* [DONE] What is Data.Dir used for? path to dir to load data from

* [DONE] What is "convertY" doing? Is it used anywhere? NO

## Val

* [] I need more detail on what `computeTightEff` is doing. 

## "train.py"

* [DONE] Where are the labels stored? in data.Y

* [DONE] How are Labels they defined? either "GammaJet"(Signal) of "DiJet"(Background)

* [] What does it mean to "train the model on Generator"?

* [] Is he using roc or auc as a metric when training?

## others
* [ONGOING] What is "Fudge Factor"? Correction factors applied to variables such as SS or pT.
* [] What are these "decorators" attributes in EGamma objects?

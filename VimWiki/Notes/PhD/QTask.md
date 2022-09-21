# Understanding Zllyathderivation - Mohamed Belfkir Code -
link: https://gitlab.cern.ch/mobelfki/zllyathderivation

* It's a Ath Derivation framework
* He gets the data of the cells from a different way of mine. He uses some *auxdata* variables, check here: https://gitlab.cern.ch/mobelfki/zllyathderivation/-/blob/master/source/MyAnalysis/Root/MyxAODAnalysis.cxx#L1410
* I think this auxdata variables is what he refers to as a "decoration" and they seem to be define here:https://gitlab.cern.ch/mobelfki/zllyathderivation/-/blob/master/source/MyAnalysis/Root/MyxAODAnalysis.cxx#L1922 .Yeah this is where he gets the cell info!!
* badcell() data quality of the obj.
* TODO: add level2 photon cluster (eta,phi,e) decoration to Zllyathderivation
* TODO: add selection cut on phs level2.
* He implemented some trigger tools here: https://gitlab.cern.ch/mobelfki/zllyathderivation/-/blob/master/source/MyAnalysis/Root/MyxAODAnalysis.cxx#L149
* He checks the trigger only when sample is NOT MC: https://gitlab.cern.ch/mobelfki/zllyathderivation/-/blob/master/source/MyAnalysis/Root/MyxAODAnalysis.cxx#L411
* What id `Photon_tightCaloOnly_tool` doing?


# Understanding CNN photon Id offline - Mohamed Belfkir Code - 

Defines 'Strategies': this sets how to deal with unhealty/corrupted clusters, and also the range in $\eta$ one wants to consider. 

* [Questions](Questions)

## NTuple

* Gets the data

* to setup:
    > NTuple works inside RootCore in lxplus for that in the first time you should set up RootCore in the cnn-photon-id directory as the following :
    ```bash
    setupATLAS
    cd AnalysisCode
    lsetup 'rcsetup Base,2.5.1'
    rc find_packages
    rc compile

    this will generate the runCleanAndGet executable. Then every time you want to use NTuple you source rcSetup.sh.

    If you modify the NTuple code you should compile it by :
    rc compile
    ```

* to run you need to pass 6 arguments to _runCleanAndGet.cxx_, which calls an instance of _CleanAndGet_
 
* CleanAndGet is a module defined in CleanAndGet.h holding all classes.
    > includes 4 public methods: ~CleanAndGet(destructor), initialize, finalize and runCleanAndGet.
    > In _LinkInputBranches_ he links: $E$, $\eta$, $\phi$, the coordinates $X,Y,Z$, $T$??, and $isBAD$. And he does this for the 3 different layers (and presample layers), and different sizes of clusters(7x11, 3x7, 5x5)

* When saving data for clusters there is one global condition: "ph_isIsoTightWP" required... why is this?

* There is a method CleanAndGet::CompleteCluster() where he defines how to deal with cluster that don't have the "expected" size. In here he also takes into account the strategy involved. He pads with zeros when too small and he chops the cluster when too big. How does he know that he is not errasing important data? I think he just gets rid of the hold cluster.

* In this instance he also divedes the sample in 3: 50% for training, 25% for validation and 25% for testing. This samples are saved in different TTrees, and also there is a 4th TTree with all data  (for redundancy?)


## Array

* converts NTuple output to NumPyArray

* Uses uproot from ROOT to LOAD TREES: https://pypi.org/project/uproot/

* outputs are Numpy objects: NPY format


## CellsToImage


* Basically calls an instance of "DataProcessing.Data", which handles a lot of things but basically loads all data setting what is Signal and Background.

* with "setData" creates de matrix with the expected dimensions ex. 7x11 for Lr2. This uses the class Data mentioned above.

* saves this matrices in NPY format files. 

## Train

* In principle I should only use Lr2_Train, Lr2_Val and Lr2_Test npy files only from `CellsToImage`

* holds two routines "reweighting.py" and "train.py"

### `train.py`

* add an args.add_argument for `isHLT` to divide the code for training with other model
* then add to `main` if isHLT: train my model.
* create a class HLTCNNClasifier in Models.models ... we can actually use the existing `CNNClasifier` with some twiks
* NOTE: some models use tf.keras.Sequential others are built with tf.keras.Model and tf.keras.layers.Input
* I think that in Y he stores the Labels

### DataProcessing

* loads into a "Data" object all the numpy arrays (saved in npy files) in different attributes for easy handling.
* `Data.GetName` takes attributes: a=<Target Label>, t=<TTree>, x=<Xn or Y or Z case>
* I think that the idea behind here is to take both the Sig data and the Bkg data saved as the format given by Array and format the sample in different containers for the training process. The thing is that here we don't have matrices yet

### Models

### Val


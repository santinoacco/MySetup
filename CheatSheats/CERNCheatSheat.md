ssh snoaccor@lxplus.cern.ch
>password
logear una screen
escribir nro host

antes de ejecutar un archivo:
$ setupATLAS
$ asetup AnalysisBase,21.2.70 #release

-   para instalar paquetes de python en lxplus:
$python3 -m pip install <pkg> (--user)

-   traer archivo de cern
scp snoaccor@lxplus.cern.ch:~/private/ParaSanti/Output.root

-   para ver path archivo
$PWD/<file>

-   para ver clases:
root.cern.ch/root/html/CLASE.html

link dinamicos:
$ ln -s <origin> <destination>
conviene que <origin> sean Path absolutos.

-   Workflow en lxplus:
programas (dentro de una screen) y corres el codigo en esa plataforma.
Luego los Outputs los guardas en SWAN_Proyects (un directorio dentro de lxplus)
para poder levantarlos desde tu maquina local a traves de SWAN.

## Mailing Lists:
    -   ML: https://e-groups.cern.ch/e-groups/EgroupsSearchForm.do

-   Compilar:
$ make -j 8 2>&1 | less ## para cuando la compilaci'on tira muchas cagadas.
$ make -j 8 #compila normal.

-   Correr archivos:
> supongamos que tienen 2 Decorators, o atributos tipo Bla1 y Bla2:
$ athena -c "Bla1=value; Bla2=value;"

Nota:
el disco 'eos/' es el que tiene mas memoria en lxplus

Para cambiar/averiguar version de paquetes:
http://lcginfo.cern.ch/
en lxplus: showVersions <pkg> python
lsetup "<pkg> <version>"

example:
`
showVersions <pkg> python
lsetup "python 3.7.4-x86_64-centos7"
`

Para setear pkg en lxplus con LCG
lsetup "lcgenv -p LCG_97python3 x86_64-centos7-clang8-opt"

To set entire LCG release:
lsetup "views"
`lsetup "views LCG_97a x86_64-centos7-clang10-opt"`

## Athena Packages
follow this Tutorial: https://atlassoftwaredocs.web.cern.ch/gittutorial/branch-and-change/


## Run python on the grid
1. check your package runs successfully @lxplus.
2. `setupATLAS; lsetup panda`
3. `prun --exec "python3 <pkg> -i %IN -args"`
I tried:
$> `prun --exec "python3 NTupleToImage.py -i %IN -s 'samples_grid.txt' -f 'features_ex.txt' -o %OUT" --inDS input/Bkg/output_Strategy_IsoTight_1_DiJet_500000.root --outputs output --outDS user.snoaccor.NTupleToImageTest`
ERROR?> `	pending due to DDM problem. VO=atlas listDatasets pid=23773 <datasetName=input/Bkg/output_Strategy_IsoTight_1_DiJet_500000.root> : An unknown exception occurred. Details: no error information passed (http status code: 404 ('not_found', '-o-'))`


ANDUVO:
"
prun --outDS user.snoaccor.prunTestwInPut --exec "python3 HelloWorld_input.py -I output_Strategy_IsoTight_1_DiJet_500000.root -O %OUT -m 'pandas test'" --extFile output_Strategy_IsoTight_1_DiJet_500000.root
"

DUDAs pendientes:
Aunque todavia me quedan un par de dudas:1. el "--inDS" DataSet de grid, tiene que presentar alguna característica? O digamos si quiero mandar una carpeta que tengo en lxplus con archivos `.npy` tengo que mandarla tipo "-i %IN" --inDS [path_folder/*] --extFile [path_folder/*]?
2. 

APRENDIZAJE HASTA AHORA DE PRUN
"--inDS": tiene que ser un path a un directorio, no a un archivo!



# RUCIO:

    >> quiero subir un dataset que se encuentra en /eos/.../mobelfki/.../Bkg, contiene los archivos que voy a usar para obtener eventos de Background para entrenar.
    Esto lo estaria guardando en mi espacio personal bajo el nombre 'user.snoaccor.NewPhotonIDSamples_FF.Bkg'
    " rucio upload --rse MY_SCRATHDISK /eos/user/m/mobelfki/NewPhotonIDSamples_FF/Bkg/ --scope user.snoacor.NewPhotonIDSamples_FF.Bkg "

    rucio upload --rse AGLT2_SCRATCHDISK /eos/user/m/mobelfki/NewPhotonIDSamples_FF/Bkg/ --scope user.snoaccor:NewPhotonIDSamples_FF.Bkg

    > then close it:
    rucio close user.snoaccor:NewPhotonIDSamples_FF.Bkg

    > to show all your DIDs
    rucio list-dids user.snoaccor:*



    TESTS ON RUNNING NTUPLE AT GRID:
    "
    prun --exec "NTuple/run/run.sh" --inDS=user.snoaccor:NewPhotonIDSamples_FF.Bkg --outDS=user.snoaccor.NTupleGridRun_Test
    " --> failed to upload source files iwth 255
    "
    source rcSetup.sh;
    cd src/NTuple/run;
    prun --exec "runCleanAndGet %IN %OUT 1 0 0 DiJet" --inDS=user.snoaccor:NewPhotonIDSamples_FF.Bkg --outDS=user.snoaccor.NTupleGridRun_Test
    "--> build successfully, run failed!
    id:22941360

    TESTS ON RUNNING NTUPLETOIMAGE AT GRID:
    "
    prun --exec "python3 NTupleToImage.py -i /eos/user/s/snoaccor/Projects/cnn_ph_id/outputs/NTuple/Bkg/output_Strategy_IsoTight_1_DiJet.root -o %OUT -f features_ex.txt -s samples.txt" --outDS user.snoaccor.CnnPhID_DataProcessing_singlefile_Bkgtest --extFile /eos/user/s/snoaccor/Projects/cnn_ph_id/outputs/NTuple/Bkg/output_Strategy_IsoTight_1_DiJet.root
    "-->
    "
    INFO : gathering files under /afs/cern.ch/work/s/snoaccor/projects/cnn-photon-id/src/DataProcessing
    INFO : upload source files
    ERROR: Could not check Sandbox duplication with 7
    ERROR : failed to upload source files with 255
    "

    "
    cd DataProcessing/NTupleToImage;
    cp <file.root> .;
    prun --exec "python3 NTupleToImage.py -i <file.root> -o %OUT -f features_ex.txt -s samples.txt" \
    --outDS user.snoaccor.CnnPhID_DataProcessing_singlefile_Bkgtest --extFile <file.root>
    "--> job failed, it also ran python2 instead of 3.

    TODO TEST
    "
    cd DataProcessing/NTupleToImage;
    cp <file.root> .;
    prun --exec "python3 NTupleToImage.py -i <file.root> -o %OUT -f features_ex.txt -s samples.txt" \
    --outDS user.snoaccor.CnnPhID_DataProcessing_singlefile_Bkgtest --extFile <file.root> --outputs Lr1.npy,Lr2.npy,Lr3.npy,Y.npy,Z.h5 --forceStaged
    "--> job failed, it also ran python2 instead of 3.

    also test the use of --inOutDsJson: where you can use a json file to specify the input and output files

    "
    [snoaccor@lxplus719 cnn-photon-id]$ prun --exec "python3 src/DataProcessing/NTupleToImage.py -i src/DataProcessing/ -o %OUT -s src/DataProcessing/samples.txt -f src/DataProcessing/features_ex.txt" --outDS user.snoaccor.CnnPhID_DataProcessing_singlefile_Bkgtest --extFile output_Strategy_IsoTight_1_DiJet_500000.root --outputs Lr1.npy,Lr2.npy,Lr3.npy,Y.npy,Z.h5 --forceStaged
    "

     TODO test using a bash script
 
 
 
 # Setup Environment
 To set up an LCG release you first need to:
 ```shell
 export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase;
 alias setupATLAS="source $ATLAS_LOCAL_ROOT_BASE/user/atlasLocalSetup.sh";
 setupATLAS
 
 lsetup "views <LCG_release> <compiler>" 
 ```
 
 # SWAN
 
 Para poder hacer instalaciones locales y que las levante SWAN automaticamente,
 es necesario crear un archivo .sh que sea levantado con cada nueva secion.
 En ese archivo debe agregarse el path local al the CERNBOX.
 El archivo debe alojarse en $EOS_HOME
 
 # xAOD
 
 -  file format
 -  need to set a release to read them.
 -  can't edit red objects in the file
 -  EventLoop is a built in module that scales better with Athena when looping the xAODs.

 # The ATLAS Framework
 
 -  Provide:
     -  Algorithm
     -  Config File.
 -  Use the framework instead of:
     - write main() function
     - loop through events
     - create output files

 -  ANA_CHECK:
     -  it's used instead of Exceptions, so use them!.
 -  To ReBuild a Release:
     - `cd ../build && make`, note that it depends on the dir location.
     - `cmake --build ../build/`
 -  EVERY LOGING:
     - `setupATLAS`
     - `cd ../build && asetup --restore && source x86_64-*/setup.sh`
 
 ## Create Package
 ```
cd ../source/
mkdir MyAnalysis
mkdir MyAnalysis/MyAnalysis         # HERE: header (.h) files
mkdir MyAnalysis/Root               # HERE: C++ source (.cxx) files (optional private headers)
mkdir MyAnalysis/src                # HERE: athena sources.
mkdir MyAnalysis/src/components
mkdir MyAnalysis/share              # HERE: config files + small data files
 ```

 ## Using Tools
 
 ## Systematics Handling
 
 For a statistical point of view check:
 basically we add a Likelihood term for each noisanse parameter.
 -  template histograms: histograms for some relev. vars from the full simulation at a couple of points in the parameter space.
 1. -   make a list of all systematics, these usually depend on the CP tools used.
 2. -   make a list of nuisance parameter to eval. Generally arround 1 sigma (for Run2 +-5sigma is possible).
 PATInterfaces package
 1. -   make NTuples for dif nuisance parameters; likely on the grid.
 2. -   make histograms at each nuisance parameter point.
 3. -   combine the histograms into a RooStats workspace.
 4. -   use RooStats workspace to produce plots, limits, measurments,..
 5. -   update the list of nuisance parameters points and repeat from step 1-2.

## DAODs

-   File format O(~TB).
-   Tailor for an specific analysis avoiding the use of the whole Reconstructed data.
-   event data model stored is the same as in AODs.
-   Run2: designed by individual analysis teams and produced centrally on request. Run3:
-   Four process:
    -   Slimming
    -   Thinning
    -   Slicing:
    -   Augmentation
-   Changes Run3:
    -   OBJECTIVE: change the fact that many DAODs overlap same events.
    -   most DAODS will be replaced by a DAOD_PHYS (https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/DAODPhys), it is unskimmed: contains all vars for analysis including calib/systematics.
    -   From those, when requested they will be skim to output a D2AODs.
    -   So essentially AODS -> DAOD_PHYS and DAODs -> D2AODs.
    -   new pre-calibrated format DAOD_PHYSLITE as prototype for Run4

# Git

## Sparce checkout
Tutorials:
    - https://atlassoftwaredocs.web.cern.ch/gittutorial/git-atlas/
    - https://atlassoftwaredocs.web.cern.ch/gittutorial/git-atlas/

- Make sure you have enough space, for instance go to \eos dir

### build
```shell

cd build;
cmake ../athena/Projects/WorkDir/
make -j10
source x86_64*-opt/setup.sh
```

## Checkout a nightly build
Lets say you want to use the code to dev of this nightly "2021-06-11T2101" from master,
to create your own branch in your fork you need to:
1. checkout master
2. git fetch upstream
3. asetup master,Athena,2021-06-11T2101
4. git checkout "$AtlasReleaseType/$AtlasBuildBranch/$AtlasBuildStamp"
5. git switch -c <new-branch-name>      # so that you make a new branch for your changes with that reklease.



# Panda

- To retry a given task with ID: X, for example 2453221:
    - lsetup panda
    - pbook
    - retry(X)
- To force to retry avoiding an specific site:
    - find the site where it failed:
        - go to MyBigPanda
        - select the job that failed, click the taskID.
        - in the table look at the columns Build and Run.
        - where it failed should be a '1', click that '1'.
        - in the poped window look for 'computingsite'.
        - that site is the one to exclude, we will call it <site_to_exclude>.
    - retry(X,, newOpts={'excludedSite':['<site_to_exclude_1>','<site_to_exclude_2>']})

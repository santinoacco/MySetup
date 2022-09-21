# Python tips and tricks

## How pip should be call
> python3 -m pip <other/s>
ex, you upgrade it like:
> python3 -m pip --upgrade pip

## Set up an venv
Create a new virtual env with python3.x version
> python3.x -m  venv <proyect_env_name>
Activate fish:
> .<proyect_env_name>/bin/activate/fish
Activate bash:
> source 

### save pkgs in `requirements.txt`
1. set a new venv
2. upgrade pip
3. check no 3rd party pkgs are install:
    1.  > `pip list`
4. install all necesary dependencies for your pkg.
5. save pkgs to file:
    1. > `pip freeze -l > requirements.txt`

## Build a python Pkg
1. create a `setup.py` in the root dir of your pkg.
2. add the following lines to `setup.py`:
    ```python
    from glob import glob
    from os.path import basename, splitext
    from setuptools import find_packages, setup

    setup(
        name=<'my_package'>,
        version='0.1',
        packages=find_packages(where='src'),
        package_dir={'': 'src'},
        py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    )
    ```
3. Then the pkg skeleton should look like:
    `src/`
        `my_package/`
            `__init__.py`
            `...`
4. Then go to the root dir of the pkg and:
    1. `pip install -e .`
            
## Module auto reloading in notebooks.
```python
%load_ext autoreload
%autoreload 2
```

## Install a second version of python
1) Donwload .tgz of source version from official site
I followed this link:
https://stackoverflow.com/a/52934964/11486987
and this
https://stackoverflow.com/a/2547577/11486987

## Install tensorflow inside venv
> TMPDIR="/var/tmp" pip install tensorflow==x

## Numba
> The subroutines should be all written in numpy format for the numba.njit decorator to work smoothly.

## Security

-   passwords and sensible data can be store in "ENV" variables an be access like:
    -   os.environ.get(<ENV_NAME>).

## PySpark

-   always init a SparkSession:
     ```python
     spark = SparkSession().builder.appName(<name>).getOrCreate()
     df = spark.read.csv()
     ```
-   to get columns from df:
    `df.select([<cols>])`
-   note slicing doesn't work

## Multiprocessing

### concurrency package

```python
import concurrent.futures

def foo(args):
    pass
    
with concurrent.futures.ProcessPoolExecutor() as executor:
    some_args = [];
    results = executor.map(foo,some_args)
```

### multiprocessing package

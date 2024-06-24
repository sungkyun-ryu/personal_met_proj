# Personal Meteorological Project
+ 1st Step: Handling grib and netCDF data with Python libraries
+ 2nd Step: Getting ideas about what benefits can be produced and how(e.g. for Energy, Quantification...)
+ 3rd Step: Using ML/DL, implement the ideas.

## Installing the environment_Ubuntu WSL (in 1st Step) 
+ Installing Ubuntu 20.04 on WSL : DONE!
+ WSL version upgrade from 1 to 2 (kernel and other needed files downloaded)
  - wsl.exe --install , wsl.exe --update, wsl --set-version Ubuntu-20.04 2 : DONE!
+ On Ubuntu, install pip and then libraries: numpy, matploblib, pandas, xarray, cfgrib and eccodes - (eccodes through pip install ecmwflibs) : DONE!
+ THE MOST IMPORTANT : sudo apt install python3-ecmwflibs (when pip install ecmwflibs not working) : DONE!
+ some libraries required virtual environment for installing.
+ pip install cftime, pip install pygrib, python -m pip install basemap: DONE!

### Use miniconda (for eccodes, cfgrib) 
+ Download Miniforge3 and install it.
+ % conda install -c conda-forge eccodes
+ % conda install -c conda-forge python-eccodes
+ $ conda install -c conda-forge cfgrib

### For using api_key from .env
+ installed: conda install conda-forge::python-dotenv (python-dotenv)


## What is research for? Which parameters? (draft, first thought) 
+ precipitation (radar)
+ clouds (satellite images)
+ From a forecaster's perspective: comparing model outputs with real-time weather data
            to QUANTIFY the reliability of the model outputs. 

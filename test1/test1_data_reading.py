## 기상자료개방포털 LDAPS / 수치모델 / LDAPS(국지지역)/GRIB2, 단일면, 00시,h000 / 20240612

import matplotlib.pyplot as plt 
import xarray as xr 
import cfgrib
import cartopy.crs as ccrs 
import cartopy.feature as cfeature 

path = '/home/skryubar61/weather/l015v070erlounish000.2024061200.gb2'

filters_by_keys_to_try = [
    {'stepType': 'avg', 'typeOfLevel': 'heightAboveGround'},
    {'stepType': 'instant', 'typeOfLevel': 'heightAboveGround'},
    {'stepType': 'min', 'typeOfLevel': 'heightAboveGround'},
    {'stepType': 'max', 'typeOfLevel': 'heightAboveGround'},
]

try:
    ds = xr.open_dataset(path, engine='cfgrib', filter_by_keys={'stepType': 'instant', 'typeOfLevel': 'surface'})
    print('Successfully opened dataset:')
    print(ds)
    print('Variables available in the dataset:')
    print(ds.data_vars)
except Exception as e:
    print(f'Failed to open dataset: {e}')

# Assuming 't' represents the variable for mean sea level pressure (adjust accordingly)
if 't' in ds.data_vars:
    data_var = 't'  # Adjust this based on the actual variable name for mean sea level pressure
else:
    data_var = None
    print("Variable 't' (mean sea level pressure) not found in dataset.")


import xarray as xr 
import netCDF4
import os 

file_path = os.path.expanduser('~/output/um_model_2024060300.nc')

ds = xr.open_dataset(file_path, engine='netcdf4')
print(ds)
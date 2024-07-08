import xarray as xr 
import netCDF4
import os 

file_path = os.path.expanduser('~/output/2024060200/final_dataset.nc')

ds = xr.open_dataset(file_path, engine='netcdf4')
print(ds)
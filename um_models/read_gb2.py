import xarray as xr 
import cfgrib 

file_path = './2024/2024_06/2024060200/rhwt/files/l015_v070_rhwt_850.2024060200_0.gb2'

ds = xr.open_dataset(file_path, engine='cfgrib')
ds_var = ds.r
print(ds_var)
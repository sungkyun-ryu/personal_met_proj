import xarray as xr

file_name= './test2_files/g128_v070_ergl_pres_rhwt_p850_h024.2024061000.gb2'

ds= xr.open_dataset(file_name, engine = 'cfgrib')
# print(ds)

rh = ds['r']
print(rh)
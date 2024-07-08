import xarray as xr 
import netCDF4
import os

date = 2024_0602_00
vars_to_check = ['r', 't', 'u', 'v', 'gh', 'wz']

file_path = os.path.expanduser(f'~/output/{date}/final_dataset.nc')

ds = xr.open_dataset(file_path, engine= 'netcdf4')

for i in range(49):
    r_0 = ds['wz'].isel(step= i)
    print(f'step= {i}:  {r_0.size}')

# for var in vars_to_check: 
#     missing_count = ds[var].isnull().sum(dim=('step', 'y', 'x'))
#     print(f"{var} missed {missing_count}")    
    # num_values = ds[var].size
    # print(f"배리어블 숫자 {var} = {num_values}")


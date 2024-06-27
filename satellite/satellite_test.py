import os 
import requests
import xarray as xr 
import netCDF4
import kma_files as kma

my_key = os.getenv('kma_api_key')

file_name = './files/gk2a_ami_le1b_sw038_ko020lc_202406260000.nc'
file_name1 = './files/gk2a_ami_le2_ci_ela020ge_202210272350.nc'

dateTime = '202406250900'
dataType = 'CLA'
areaRange = 'KO'

save_path= f'./files/{dataType}_{areaRange}_{dateTime}.nc'
url= f'https://apihub.kma.go.kr/api/typ05/api/GK2A/LE2/{dataType}/{areaRange}/data?date={dateTime}&authKey={my_key}'


###################### Reading Url - Writing File ###################

# kma.download_file(url, save_path)

ds = xr.open_dataset(save_path, engine='netcdf4')
print(ds)

# ds1 = xr.open_dataset(file_name1, engine='netcdf4')
# print(ds1)

################ in the dataset, CA:cloud amount, CLL: height #################
var = ds.CLL
print(var)


import matplotlib.pyplot as plt 
import cartopy.crs as ccrs 


fig = plt.figure(figsize=(10,10))
# ax = plt.axes(projection = ccrs.PlateCarree())
# pcm = ax.pcolormesh(ds.dim_x, ds.dim_y, ds.image_pixel_values, cmap='viridis', transform= ccrs.PlateCarree())
# ax.coastlines()
ax = plt.pcolormesh(ds.dim_y, ds.dim_x, var, cmap = 'viridis')
# ax = plt.pcolormesh(ds1.xdim, ds1.ydim, var1, cmap = 'viridis')
plt.show()








############################## projection, KMA Tutorial #############
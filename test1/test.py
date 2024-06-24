## 수치모델 경량화 다운로드 (기상청 API) 

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import eccodes 
import cfgrib 
import xarray as xr 
import torch 
import tqdm
import requests
from pathlib import Path
import os
import seaborn as sns
import cartopy.crs as ccrs 




file_path = '/home/skryubar61/weather/g128_v070_ergl_pres_tmpr_p850_h024.2021081012.gb2'
try:
    ds = xr.open_dataset(file_path, engine= 'cfgrib')
    print(ds)
except Exception as e : 
    print('failed!!!!!')

print("variables available in the dataset::")
print(ds.data_vars)

lats = ds.latitude.data 
lons = ds.longitude.data
temp = ds.t.data 

extent = [115, 130, 30, 45]

# lon, lat = np.meshgrid(lons, lats)

# plt.figure(figsize=(12, 6))

# # Plot using pcolormesh
# plt.pcolormesh(lon, lat, temp, shading='auto')

# # Add colorbar
# plt.colorbar(label='Temperature (units)')

# # Add title and labels
# plt.title('Temperature Map')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')

# # Show the plot
# plt.show()

# Create a figure and axes with a specific map projection
fig, ax = plt.subplots(figsize=(12, 8), subplot_kw={'projection': ccrs.PlateCarree()})

# Plot temperature data using pcolormesh
pcm = ax.pcolormesh(lons, lats, temp, transform=ccrs.PlateCarree(), shading='auto')

# Add coastlines for better geographical context
ax.coastlines()

# # Set map extent to Korean Peninsula
# ax.set_extent(extent, crs=ccrs.PlateCarree())

# Add colorbar
cbar = plt.colorbar(pcm, ax=ax, orientation='vertical', label='Temperature (units)')

# Add title
plt.title('Temperature Map with Cartopy')

# Show the plot
plt.show()

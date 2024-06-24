## 기상자료개방포털 LDAPS / 수치모델 / LDAPS(국지지역)/GRIB2, 단일면, 00시,h000 / 20240612

import matplotlib.pyplot as plt 
import xarray as xr 
import cfgrib
import cartopy.crs as ccrs 
import cartopy.feature as cfeature 

path = '/home/skryubar61/weather/files/l015v070erlounish000.2024061200.gb2'

filters_to_try = [
    {'typeOfLevel': 'surface'},
    {'typeOfLevel': 'heightAboveGround'},
    {'typeOfLevel': 'nominalTop'},
    {'typeOfLevel': 'unknown'},
    {'typeOfLevel': 'depthBelowLandLayer'},
    {'typeOfLevel': 'meanSea'},
    {'typeOfLevel': 'isothermZero'}
]

filters_by_keys_to_try = [
    {'stepType': 'avg', 'typeOfLevel': 'heightAboveGround'},
    {'stepType': 'instant', 'typeOfLevel': 'heightAboveGround'},
    {'stepType': 'min', 'typeOfLevel': 'heightAboveGround'},
    {'stepType': 'max', 'typeOfLevel': 'heightAboveGround'},
]

try:
    # ds = xr.open_dataset(path, engine='cfgrib', filter_by_keys=filters_by_keys_to_try[0], decode_times=False)
    ds = xr.open_dataset(path, engine='cfgrib', filter_by_keys=filters_by_keys_to_try[0])
    print(f'Successfully opened dataset with filter:')
    print(ds)
    print(ds.data_vars)
except Exception as e:
    print(f'Failed to open dataset : {e}')


# Select the data at the surface level (heightAboveGround = 2.0)
data = ds.sel(heightAboveGround=2.0)

# Define the region for the Korean Peninsula
lon_min, lon_max = 124, 132
lat_min, lat_max = 33, 43

# Create a figure
plt.figure(figsize=(10, 8))
ax = plt.axes(projection=ccrs.PlateCarree())

# Add coastlines and other features
ax.coastlines()
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAND, edgecolor='black')

# Plot the data
plot = ax.pcolormesh(data.longitude, data.latitude, data.unknown,
                     transform=ccrs.PlateCarree(), cmap='coolwarm')

# Add colorbar and title
plt.colorbar(plot, ax=ax, orientation='horizontal', pad=0.05, label='Unknown Variable')
plt.title('Unknown Variable at Height 2.0')

# Set the extent to the Korean Peninsula
ax.set_extent([lon_min, lon_max, lat_min, lat_max], crs=ccrs.PlateCarree())

plt.show()
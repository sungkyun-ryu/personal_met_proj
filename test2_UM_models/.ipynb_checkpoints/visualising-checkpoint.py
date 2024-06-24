import xarray as xr 
import matplotlib.pyplot as plt 
import cartopy.crs as ccrs 

file = './test2_files/g128_v070_ergl_pres_rhwt_p850_h024.2024061000.gb2'

ds = xr.open_dataset(file, engine='cfgrib') 
print(ds)

data_variable = ds.r
data_time = ds.time.values 
print(f'시간 = {data_time}')
data_step = ds.step.values
print(f'타임랩 = {data_step}')
# print(data_variable)

# # Visualising the variable with the coordinates 

# plt.figure(figsize = (10, 6))
# plt.contourf(ds.longitude, ds.latitude, data_variable, cmap = 'viridis')
# plt.colorbar(label='Value')
# plt.title('Contour Plot of RH')
# plt.xlabel('Longitude'); plt.ylabel('Latitude')
# plt.grid(True)
# plt.show()

# On the MAP(using Cartopy)

plt.figure(figsize=(14, 7))
ax = plt.axes(projection=ccrs.PlateCarree())
pcm = ax.pcolormesh(ds.longitude, ds.latitude, data_variable, cmap='viridis', transform=ccrs.PlateCarree())
plt.colorbar(pcm, ax=ax, orientation='vertical', label='RH')
plt.title('RH at time = ?')
ax.coastlines()
ax.gridlines(draw_labels=True)
plt.show()

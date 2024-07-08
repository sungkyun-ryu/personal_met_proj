import xarray as xr 
import cfgrib 
import matplotlib.pyplot as plt 
import cartopy.crs as ccrs 
import os 

# var_ch = 'ghgt'
# dateTime = 2024_0630_00
# month = '06'


# fileName = f'l015_v070_{var_ch}_850.{dateTime}_{i}.gb2'
# path= f'./2023/2023_{month}/{dateTime}/{var_ch}/files/{fileName}'



def create_image(time_step, img_path, file_name):
    ds = xr.open_dataset(file_name, engine='cfgrib')
    met_var = ds.v 
    plt.figure(figsize=(15,7))
    ax = plt.axes(projection = ccrs.PlateCarree())
    pcm = ax.pcolormesh(ds.longitude, ds.latitude, met_var, transform=ccrs.PlateCarree())
    plt.colorbar(pcm, ax=ax, orientation='vertical', label='Cloud(RH)')
    plt.title(f"Cloud at {time_step}")
    ax.coastlines()
    # plt.savefig(img_path)
    plt.show()
    # plt.close()
    
    # print('image saved')


var_ch= 'vgrd'
dateTime = 2024063000

ds = xr.open_dataset('./dzdt/files/l015_v070_dzdt_850.2023123200_0.gb2', engine= 'cfgrib')
print(ds)
print(ds.coords['time'].values)

# # for i in range(49):
# i=0
# os.makedirs(f"./{var_ch}/img", exist_ok=True )
# fileName = f'./vgrd/files/l015_v070_{var_ch}_850.{dateTime}_{i}.gb2'
# img_path = f'./vgrd/img/l015_v070_{var_ch}_850.{dateTime}_{i}.png'
# create_image(i, img_path, fileName )
# print(f"num= {i}")
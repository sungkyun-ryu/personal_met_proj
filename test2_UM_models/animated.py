## 수치모델 경량화 다운로드(예측시간+변수+고도별) 20240610

import xarray as xr 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import cartopy.crs as ccrs 

file_path = './test2_files/g128_v070_ergl_pres_rhwt_p850_h024.2024061000.gb2'

ds = xr.open_dataset(file_path, engine='cfgrib')
time = ds.coords['time']
print(time)
step = ds.coords['step']
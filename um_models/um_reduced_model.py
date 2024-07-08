import os 
import requests
import xarray as xr 
import cfgrib 
import matplotlib.pyplot as plt 
import cartopy.crs as ccrs 
from wakepy import keep

def download_file(url, save_path): 
    with open(save_path, 'wb') as f: 
        resp = requests.get(url)
        if resp.status_code == 200:
            f.write(resp.content)
            print("Success ::::: ", end= ' ')
        else:
            print("Fail ===== ", end= '')

def create_image(time_step, img_path, file_name):
    ds = xr.open_dataset(file_name, engine='cfgrib')
    met_var = ds.r 
    plt.figure(figsize=(15,7))
    ax = plt.axes(projection = ccrs.PlateCarree())
    pcm = ax.pcolormesh(ds.longitude, ds.latitude, met_var, cmap='viridis', transform=ccrs.PlateCarree())
    plt.colorbar(pcm, ax=ax, orientation='vertical', label='Cloud(RH)')
    plt.title(f"Cloud at {time_step}")
    ax.coastlines()
    plt.savefig(img_path)
    plt.close()
    print('image saved')

# my_key = os.getenv('kma_api_key1')
# my_key= os.getenv('kma_api_key2')
my_key= os.getenv('kma_api_key3')
# my_key= os.getenv('kma_api_key4')

var = {
    'rh' : 'rhwt',
    'temp' : 'tmpr', 
    'u_wind' : 'ugrd', 
    'v_wind' : 'vgrd', 
    'vv' : 'dzdt',
    'geop' : 'ghgt'
}

months = [ '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
months_last_date = { '01' : [2024_0101_00, 31], 
                    '02' : [2024_0201_00, 28], 
                    '03' : [2024_0301_00, 31], 
                    '04' : [2024_0401_00, 30], 
                    '05' : [2024_0501_00, 31], 
                    '06' : [2024_0601_00, 30], 
                    '07' : [2024_0701_00, 31], 
                    '08' : [2024_0801_00, 31], 
                    '09' : [2024_0901_00, 30], 
                    '10' : [2024_1001_00, 31], 
                    '11' : [2024_1101_00, 30], 
                    '12' : [2024_1201_00, 31],
                    }

# var_ch = var['geop']
vars = ['ghgt']


# with keep.running() : 
for ch in vars:
    var_ch = ch
    dateTime= 2023_1001_00
    n = 15
    month = '10'    
    # for l in range(1,2):
    #     month= months[l+1]
    #     dateTime = months_last_date[month][0]
    #     n= months_last_date[month][1]
    for j in range(n):    
        os.makedirs(f"./2023/2023_{month}/{dateTime}/{var_ch}/files", exist_ok=True)
        failed = []
        for i in range(49):
            fileName = f'l015_v070_{var_ch}_850.{dateTime}_{i}.gb2'
            url = f'https://apihub.kma.go.kr/api/typ06/url/nwp_vars_down.php?nwp=l015&sub=pres&vars={var_ch}&pres=850&tmfc={dateTime}&ef={i}&dataType=GRIB&authKey={my_key}'
            path= f'./2023/2023_{month}/{dateTime}/{var_ch}/files/{fileName}'
            download_file(url, path)
            if os.stat(path).st_size < 900000: 
                print(f'===================== File size is SMALL ===================== fileNum{i}')
                failed.append(i)
            print(f'fileNum= {i}, {dateTime}, var= {var_ch}, size = {os.stat(path).st_size}, laps=({j+1}/{n})', end=' ')
            if i%2 == 0:
                print('>>>>>')
            else: 
                print('     <<<<<')
        if len(failed) > 0:     
            for k in failed: 
                fileName = f'l015_v070_{var_ch}_850.{dateTime}_{k}.gb2'
                url = f'https://apihub.kma.go.kr/api/typ06/url/nwp_vars_down.php?nwp=l015&sub=pres&vars={var_ch}&pres=850&tmfc={dateTime}&ef={k}&dataType=GRIB&authKey={my_key}'
                path= f'./{dateTime}/{var_ch}/files/{fileName}'
                download_file(url, path)            
        dateTime= dateTime + 100


os.system('powershell.exe /s /t')



# for i in range(49):
#     os.makedirs(f"{dateTime}/{var_ch}/img", exist_ok=True )
#     fileName = f'./rhwt/files/l015_v070_{var_ch}_850.{dateTime}_{i}.gb2'
#     img_path = f'./rhwt/img/l015_v070_{var_ch}_850.{dateTime}_{i}.png'
#     create_image(i, img_path, fileName )
#     print(f"num= {i}")


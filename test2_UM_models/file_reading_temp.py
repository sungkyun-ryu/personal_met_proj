## 1. 수치모델 경량화 다운로드(예측시간+변수+고도별)
## url 생성기에 변수 입력 안돼 manually 추가
## -> vars=tmpr&pres=850&
## 날짜변경 202406100000
## url 파일 읽기 실패, downloaded file로 진행 https://apihub.kma.go.kr/api/typ06/url/nwp_vars_down.php?nwp=g128&sub=pres&vars=tmpr&pres=850&tmfc=202406100000&ef=24&dataType=GRIB&authKey=op3tPE72Tf6d7TxO9p3-Eg
## var=tmpr --> temperature, pres=850 --> 850 hPa

import cfgrib 
import requests 
import os

# print(os.getcwd())

# url ='https://apihub.kma.go.kr/api/typ06/url/nwp_vars_down.php?nwp=g120&sub=pres&tmfc=202406100000&ef=24&dataType=GRIB&authKey=op3tPE72Tf6d7TxO9p3-Eg'

# resp = requests.get(url) 
# file_name = 'reduced_models.gb2'
file_downloaded = './test2_files/g128_v070_ergl_pres_tmpr_p850_h024.2024061000.gb2'

# if resp.status_code == 200: 
#     print("getting data success!")

# with open(file_name, 'wb') as file: 
#     file.write(resp.content)

ds = cfgrib.open_dataset(file_downloaded)
print(ds)

# ds1 = cfgrib.open_dataset(f'../{file_name}')
# print(ds1)

# file_size = os.path.getsize(file_name)
# if file_size < 1024:
#     raise ValueError("it is too small.")

# temp_data = ds['t'].values

#finding min and max of temperature: 

# min_t_value = ds['t'].min().item()
# max_t_value = ds['t'].max().item()

# min_t_location = ds['t'].where(ds['t'] == min_t_value, drop=True)
# max_t_location = ds['t'].where(ds['t'] == max_t_value, drop=True)

# print(f"Minimum t value: {min_t_value} at location:")
# print(min_t_location)

# print(f"Maximum t value: {max_t_value} at location:")
# print(max_t_location)
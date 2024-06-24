import os 
import requests 
import numpy as np 
import matplotlib.pyplot as plt
import zipfile
import geopandas as gpd


# 분포도에서 색상표 위치, 크기를 조절하는 함수
from mpl_toolkits.axes_grid1 import make_axes_locatable


os.environ["kma_api_key"] = 'op3tPE72Tf6d7TxO9p3-Eg'
my_api_key = os.environ['kma_api_key']
# print(f'api = {my_api_key}')

# api_url = 'https://apihub.kma.go.kr/api/typ06/url/nwp_vars_down.php'

# nwp= 'l015'

# file_separator = {
#     'sub': 'pres',
#     'vars': 'tmpr'
# }

# pres_levels = [
#     1000, 975, 950, 925, 900, 875, 850, 800, 750, 700, 650,
#     600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100, 70, 50
# ]

# tmfc_utc = '2024051412'

# ef = 24

# data_type = 'GRIB' 

# file_name_list = np.array([
#     f"{nwp}_v070_erlo_{file_separator['sub']}_{file_separator['vars']}_"
#     f"{file_separator['sub'][0]}{(level % 1000):03d}_"
#     f"h{ef:03d}.{tmfc_utc[:10]}.gb2" for level in pres_levels]
# )

# # print(f'filename= {file_name_list}')

# file_exists_list = np.vectorize(os.path.exists)(file_name_list)


# # 각 파일의 존재 여부를 확인합니다.
# file_exists_list = np.vectorize(os.path.exists)(file_name_list)

# # 저장된 파일이 없는 경우에만 API를 요청해 파일을 다운로드합니다.
# if not file_exists_list.all():
#     # API 요청인자들을 묶어 dictionary로 정의합니다.
#     api_parameters = {
#         'nwp': nwp,
#         'tmfc': tmfc_utc,
#         'ef': ef,
#         'dataType': data_type,
#         'authKey': my_api_key,
#         **file_separator
#     }
#     # 파일 다운로드를 위한 세션을 만듭니다.
#     with requests.Session() as session:
#         # 존재하지 않는 파일에 대해서 반복합니다.
#         for idx in np.where(~file_exists_list)[0]:
#             # API 요청인자에 레벨을 입력합니다.
#             api_parameters[file_separator['sub']] = pres_levels[idx]

#             # API 요청인자와 함께 API 요청
#             response = session.get(api_url, params=api_parameters)

#             # 잘못된 응답을 받거나 짧은 에러메세지를 응답으로 받은 경우 에러 메세지 출력
#             if response.status_code != 200 or len(response.content) < 500:
#                 raise requests.RequestException(
#                     response.content.decode('utf-8')
#                 )
#             else:
#                 # 그 외의 올바른 응답에 대해서만 파일로 저장합니다.
#                 with open(file_name_list[idx], 'wb') as f:
#                     f.write(response.content)
#                 print(f'{file_name_list[idx]} 파일 다운로드 완료')

#                 import matplotlib.pyplot as plt # 이미지 표출에 사용되는 라이브러리




# 국토지리정보원의 대한민국주변도 shape 파일 다운로드 url
shp_url = 'https://www.ngii.go.kr/other/file_down.do?sq=107951'

# shape 파일은 압축파일 형태로 제공됩니다.
shape_file_name = 'korea_shp.zip'
extract_directory = 'korea_shape'

# shape 압축파일이 없는 경우에만 API를 요청해 파일을 다운로드합니다.
if not os.path.exists(shape_file_name):
    # url에 대해 GET 요청을 보냅니다.
    response = requests.get(shp_url)

    # 받은 응답을 zip 파일 형태로 저장합니다.
    with open(shape_file_name, 'wb') as f:
        f.write(response.content)
    print(f'{shape_file_name} 파일 다운로드 완료')

    # 다운로드 받은 압축 파일을 korea_shape 폴더 아래에 압축 해제합니다.
    with zipfile.ZipFile(shape_file_name, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            file_info.filename = file_info.filename.encode('cp437').decode('euc-kr')
            zip_ref.extract(file_info, extract_directory)

# 국가 경계를 구분한 shp파일은 ARD_NAION_AS으로
# 이 파일을 읽어 수치모델이 갖는 좌표계인 LCC 도법으로 변환합니다.
lcc_crs =(
    "+proj=lcc +lat_1=30 +lat_2=60 +lat_0=38 +lon_0=126 "
    "+x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"
)
gdf = gpd.read_file(
    os.path.join(extract_directory, 'ARD_NAION_AS.shp')
).to_crs(lcc_crs)

# 1m 단위의 도법에서 수치모델의 해상도 단위(1.5km)에 맞춥니다.
# 참고자료에 따르면 기준점 위치의 경우 x: 389.478893km, y: 618.363966km이며
# 각 격자마다 1.5km의 간격을 가집니다.
resolution = 1500
origin_x = 389.478893/1.5
origin_y = 618.363966/1.5
gdf.geometry = gdf.geometry.scale(
    xfact=1/resolution, yfact=1/resolution, zfact=1.0,
    origin=(origin_x, origin_y)
)

# # 이미지를 그릴 크기를 지정합니다.
# fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# # 이미지의 제목을 지정합니다.
# fig.suptitle(f"Forecast after {ef} hours from {tmfc_utc}")
# axes[0].set_title(f"Temperature at 1000hPa")
# axes[1].set_title(f"Temperature at 50hPa")

# # 국가간의 경계선을 검정색으로 그립니다.
# gdf.boundary.plot(ax=axes[0], color='black', linewidth=0.5)
# gdf.boundary.plot(ax=axes[1], color='black', linewidth=0.5)

# # 이미지를 각 영역에 그립니다.
# im1 = axes[0].imshow(grb_message_1000.data()[0], cmap='turbo', origin='lower')
# im2 = axes[1].imshow(grb_message_50.data()[0], cmap='turbo', origin='lower')

# # 색상표의 크기와 위치를 조절합니다.
# divider1 = make_axes_locatable(axes[0])
# cax1 = divider1.append_axes('right', size='5%', pad=0)
# divider2 = make_axes_locatable(axes[1])
# cax2 = divider2.append_axes('right', size='5%', pad=0)

# # 색상표에 표시될 글자 크기 및 제목을 설정합니다.
# cbar1 = fig.colorbar(im1, cax=cax1)
# cbar2 = fig.colorbar(im2, cax=cax2)
# cbar1.ax.tick_params(labelsize=8)
# cbar1.ax.set_title('K', fontsize=8)
# cbar2.ax.tick_params(labelsize=8)
# cbar2.ax.set_title('K', fontsize=8)

# # 그린 이미지를 표출합니다.
# plt.show()
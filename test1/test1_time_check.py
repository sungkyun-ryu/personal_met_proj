import xarray as xr

path = '/home/skryubar61/weather/l015v070erlounish000.2024061200.gb2'
try:
    ds = xr.open_dataset(path, engine='cfgrib', filter_by_keys={'stepType': 'instant', 'typeOfLevel': 'surface'})
    print("Dataset loaded successfully.")
    print(ds)
except Exception as e:
    print(f"Failed to open dataset: {e}")

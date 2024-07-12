import xarray as xr 
import cfgrib 
import netCDF4
import os

## Loading all 49 files of SINGLE variable. 
def load_a_variable(issue_date_folder, variable, date): 
    datasets= []
    variable_folder = f'{variable}/files'
    variable_path = os.path.join(issue_date_folder, variable_folder) 

    for timestep in range(49): 
        filepath= os.path.join(variable_path, f'l015_v070_{variable}_850.{date}_{timestep}.gb2')
        ds= xr.open_dataset(filepath, engine='cfgrib')
        datasets.append(ds)
    return datasets 

## Load ALL 6 variables in a given date 
def load_all_variables(issue_date_folder, variables, date):

    data_by_timestep = {t: [] for t in range(49)}

    for variable in variables: 
        datasets= load_a_variable(issue_date_folder, variable, date)
        for timestep, ds in enumerate(datasets): 
            data_by_timestep[timestep].append(ds)
    
    return data_by_timestep

def combined_variables(data_by_timestep):
    combined_datasets = []
    for t, datasets in data_by_timestep.items(): 
        combined_ds = xr.merge(datasets)
        combined_datasets.append(combined_ds)
    return combined_datasets


##
def concat_timestep(combined_datasets) : 
    concatenated_ds = xr.concat(combined_datasets, dim = 'step')
    return concatenated_ds



year= 2024
month = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
date = 2024061300
variables = ['rhwt', 'tmpr', 'ugrd', 'vgrd', 'ghgt', 'dzdt']



for i in range(18):
    issue_date_folder = f"./{year}/{year}_{month[6]}/{date}"
    data_by_timestep = load_all_variables(issue_date_folder, variables, date)
    combined_dataset = combined_variables(data_by_timestep)
    final_dataset = concat_timestep(combined_dataset)

    ## home/skryubar폴더에서만 만들어지는 문제 해결하기 
    outdir = os.path.expanduser(f'~/output/')
    os.makedirs(outdir, exist_ok=True)

    outpath = os.path.join(outdir, f'um_model_{date}.nc')
    final_dataset.to_netcdf(outpath, format='NETCDF4', mode='w', encoding={'step': {'zlib': True, 'complevel': 4}})

    print(f'Final dataset saved to {outpath}')
    date += 100

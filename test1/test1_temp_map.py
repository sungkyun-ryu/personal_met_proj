import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.animation import FuncAnimation

# File path to your GRIB file
file_path = '/home/skryubar61/weather/files/g128_v070_ergl_pres_tmpr_p850_h024.2021081012.gb2'

# Load the dataset
try:
    ds = xr.open_dataset(file_path, engine='cfgrib')
    print(ds)
except Exception as e:
    print(f'Failed to open dataset: {e}')

# Print available variables
print("Variables available in the dataset:")
print(ds.data_vars)

# Ensure the dataset has a valid_time dimension
if 'valid_time' not in ds.coords:
    raise ValueError("The dataset does not contain a 'valid_time' coordinate.")

# Define the region for the Korean Peninsula
lon_min, lon_max = 124, 132
lat_min, lat_max = 33, 43

# Subset the data for the Korean Peninsula region
ds_subset = ds.sel(latitude=slice(lat_max, lat_min), longitude=slice(lon_min, lon_max))

# Extract the necessary data
lats = ds_subset.latitude.data
lons = ds_subset.longitude.data
times = ds_subset.valid_time.values  # Extract the valid_time coordinate as values
temp = ds_subset.t.data  # Extract temperature data

# Debugging print statements
print(f"Type of times: {type(times)}")
if isinstance(times, np.ndarray):
    print(f"First few times: {times[:5]}")
else:
    print(f"Times: {times}")

# Ensure times is a numpy array of datetime objects
if not isinstance(times, np.ndarray):
    times = np.array([times])

# Create a figure and axes with a specific map projection
fig, ax = plt.subplots(figsize=(12, 8), subplot_kw={'projection': ccrs.PlateCarree()})

# Function to update the plot for each frame
def update(frame):
    ax.clear()
    pcm = ax.pcolormesh(lons, lats, temp, transform=ccrs.PlateCarree(), shading='auto', cmap='coolwarm')
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.set_extent([lon_min, lon_max, lat_min, lat_max], crs=ccrs.PlateCarree())
    plt.title(f'Temperature Map with Cartopy\nTime: {times[frame]}')
    return pcm,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(times), blit=False, repeat=True)

# Save the animation (optional)
# ani.save('temperature_animation.mp4', writer='ffmpeg', fps=2)

# Show the plot
plt.show()



#### explanation from chatGPT 

# The error you're encountering, ValueError: not enough values to unpack (expected 2, got 1), typically occurs when there is an issue with the dimensions or shape of the data passed to pcolormesh in Matplotlib. This can happen if the data arrays (lons, lats, temp) are not structured as expected for plotting.

# Possible Causes and Solutions:
# Data Shape Mismatch: Ensure that lons, lats, and temp have the correct shapes and dimensions. They should match each other in terms of their grid dimensions.

# Temporal Dimension Handling: If you're animating over time (frames=len(times)), ensure that temp[frame] corresponds correctly to the shape expected by pcolormesh.

# Coordinate Systems: Verify that lons and lats are in the correct format (2D arrays or grids) that pcolormesh expects.

# Revised Approach:
# Let's refine the code to ensure the data dimensions are correct and that the plotting function (pcolormesh) receives the expected input:

# Explanation and Fixes:
# Data Extraction: Ensure temp is extracted correctly from ds_subset.t.data. It should be a 2D array matching the dimensions of lats and lons.

# Update Function: The update function now directly uses temp for pcolormesh, assuming it's a 2D array. Adjust if temp is structured differently.

# Animation Setup: The animation should now iterate over times, assuming times is correctly structured as an array of datetime objects.

# Further Debugging Steps:
# Print Statements: Use additional print statements to verify the shapes and values of lons, lats, and temp.

# Check Dataset: Ensure ds_subset contains valid data for the specified region and time range.

# If you continue to encounter issues, further inspection of the data's dimensions and shapes (lons, lats, temp) should help diagnose and resolve the ValueError related to pcolormesh. Adjust the update function accordingly to match the expected input for pcolormesh.
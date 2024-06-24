import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import cartopy.crs as ccrs
import xarray as xr

# Define the path to your GRIB2 file
path = '/home/skryubar61/weather/l015v070erlounish000.2024061200.gb2'

try:
    # Open the dataset with filter_by_keys for surface data
    ds = xr.open_dataset(path, engine='cfgrib', filter_by_keys={'stepType': 'instant', 'typeOfLevel': 'surface'})
    print("Dataset loaded successfully.")
    print(ds)
except Exception as e:
    print(f"Failed to open dataset: {e}")

# Assuming 'time' is the variable representing time steps
time_var = ds['time']  # Accessing the time variable from the dataset

# Assuming 'surface_data' is the variable containing data for visualization
surface_data = ds['unknown']  # Accessing the variable for visualization

# Extract latitude and longitude coordinates from the dataset
lon_values = ds.longitude.values
lat_values = ds.latitude.values

# Calculate extent values
lon_min, lon_max = lon_values.min(), lon_values.max()
lat_min, lat_max = lat_values.min(), lat_values.max()

# Define the plot function to update for each frame of animation
def update(frame):
    plt.clf()  # Clear previous plot

    # Extract data for the current frame/time step
    current_data = surface_data[frame]

    # Create the plot
    plt.figure(figsize=(10, 8))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()

    # Plot the data
    plot = ax.pcolormesh(lon_values, lat_values, current_data, transform=ccrs.PlateCarree(), cmap='coolwarm')
    plt.colorbar(plot, ax=ax, orientation='horizontal', pad=0.05, label='Data Variable')

    plt.title(f'Data at Time Step {frame}')
    ax.set_extent([lon_min, lon_max, lat_min, lat_max], crs=ccrs.PlateCarree())

# Create an animation
num_frames = len(time_var)  # This line assumes time_var is a valid iterable
ani = FuncAnimation(plt.gcf(), update, frames=num_frames, blit=False, repeat=True)

# Show the animation
plt.show()

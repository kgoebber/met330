from datetime import datetime

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from metpy.units import units
import numpy as np
import xarray as xr

# Bring in metadata and set up for bringing in the data
ds = xr.open_dataset('http://psl.noaa.gov/thredds/dodsC/Datasets/'
                     'ncep.reanalysis/pressure/hgt.1993.nc')

# Grab the actual air temperature data
date = datetime(1993, 2, 2, 12)
hght_data = ds.hgt.sel(time=date)
print(ds.hgt)



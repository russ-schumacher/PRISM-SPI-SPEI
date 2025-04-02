#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xarray as xr
import pandas as pd

path_to_files = "/data/rschumac/prism/monthly/PRISM_tmean_*_bil.nc"

def extract_date(ds):
    grid_time = pd.to_datetime(ds.encoding['source'].split('_')[4],format="%Y%m")

    print(grid_time)
    return ds.assign(time=grid_time)

data_comb = xr.open_mfdataset(path_to_files,
                       concat_dim='time',
                       combine='nested',
                       preprocess=extract_date)
                       #engine='pynio')


data_sub = data_comb.sel(lat=slice(36.0,42.0),lon=slice(-110.,-101.0))
data_sub = data_sub.rename({'Band1':'tavg'})
data_sub.tavg.attrs['units'] = "degree_Celsius"
## sort by time because they might get out of order
data_sub = data_sub.sortby('time')
### reorder dimensions
data_sub['tavg'] = data_sub['tavg'].transpose("lat","lon","time")


# In[40]:

print("writing file")
data_sub.to_netcdf("PRISM_tavg_monthly_CO_all.nc")




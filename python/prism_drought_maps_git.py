#!/usr/bin/env python
# coding: utf-8

# In[2]:

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('agg')
import xarray as xr
import pandas as pd
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.dates as mdates 
import numpy as np
import os

from metpy.plots import USCOUNTIES
from matplotlib.offsetbox import AnchoredText


# In[ ]:


## SPEI

months = [1,2,3,4,6,9,12,24,48,60]

## loop over the months
for month in months:
    
    print("working on month "+str(month))
    month2d = "{:02d}".format(month)
    
    # file
    infile = "PRISM_CO_spei_pearson_"+month2d+".nc"
    
    ## read it
    data_in = xr.open_dataset(infile)
    data = data_in['spei_pearson_'+month2d].sel(lat=slice(37,41),lon=slice(-109,-102))[:,:,-1] ## get last month in file
    
    ## make a map
    crs = ccrs.LambertConformal(central_longitude=-105.0, central_latitude=37.5)
    #crs = ccrs.LambertConformal(central_longitude=-100.0, central_latitude=42.0)

    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(1,1,1,projection=crs)

    ## Colorado versions
    lonmin=-109.5
    lonmax=-101.5
    latmin=36.4
    latmax=41.5

    #ax.set_extent([235., 290., 20., 55.])
    #ax.set_extent((-109.5,-101.5,36.4,41.5))
    ax.set_extent([lonmin,lonmax,latmin,latmax])
    ax.add_feature(cfeature.LAND)
    ax.add_feature(USCOUNTIES.with_scale('5m'), edgecolor="gray", linewidth=0.4)
    ax.add_feature(cfeature.STATES)
    ax.add_feature(cfeature.BORDERS)

    #levels and colors to match USDM cats
    levs = [-3,-2, -1.6,-1.3,-0.8,-0.5,0,0.5,0.8,1.3,1.6,2,3]
    cols = ["#730000","#E60000","#FFAA00","#FCD37F","#FFFF00","white","white","green","darkgreen","cyan","purple","magenta"]

    ## SPEI
    cf1 = ax.contourf(data['lon'], data['lat'], data, 
                             levs,colors=cols, extend='both', transform=ccrs.PlateCarree())

    ax.set_title(str(month)+"-month SPEI based on PRISM data, end of "+data.time.dt.strftime('%B %Y').values, fontsize=13)

    cb1 = fig.colorbar(cf1, ax=ax, orientation='horizontal', aspect=30, shrink=0.65, pad=0.01)
    cb1.set_label('SPEI', size='large')
    
    # Add a text annotation 
    text = AnchoredText("source: PRISM Climate Group, Oregon State University\nPearson distribution trained on 1901-2020",
                        loc='lower left', prop={'size': 8}, frameon=True)
    ax.add_artist(text)

    #plt.show()

    plt.savefig("spei_"+str(month)+"month_"+data.time.dt.strftime('%Y%m').values+"_CO.png", bbox_inches='tight', dpi=200, transparent=False, facecolor='white')
    plt.close('all')


## repeat for SPI

months = [1,2,3,4,6,9,12,24,48,60]

## loop over the months
for month in months:
    
    print("working on month "+str(month))
    month2d = "{:02d}".format(month)
    
    # file
    infile = "PRISM_CO_spi_pearson_"+month2d+".nc"
    
    ## read it
    data_in = xr.open_dataset(infile)
    data = data_in['spi_pearson_'+month2d].sel(lat=slice(37,41),lon=slice(-109,-102))[:,:,-1] ## get last month in file
    
    ## make a map
    crs = ccrs.LambertConformal(central_longitude=-105.0, central_latitude=37.5)
    #crs = ccrs.LambertConformal(central_longitude=-100.0, central_latitude=42.0)

    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(1,1,1,projection=crs)

    ## Colorado versions
    lonmin=-109.5
    lonmax=-101.5
    latmin=36.4
    latmax=41.5

    #ax.set_extent([235., 290., 20., 55.])
    #ax.set_extent((-109.5,-101.5,36.4,41.5))
    ax.set_extent([lonmin,lonmax,latmin,latmax])
    ax.add_feature(cfeature.LAND)
    ax.add_feature(USCOUNTIES.with_scale('5m'), edgecolor="gray", linewidth=0.4)
    ax.add_feature(cfeature.STATES)
    ax.add_feature(cfeature.BORDERS)

    #levels and colors to match USDM cats
    levs = [-3,-2, -1.6,-1.3,-0.8,-0.5,0,0.5,0.8,1.3,1.6,2,3]
    cols = ["#730000","#E60000","#FFAA00","#FCD37F","#FFFF00","white","white","green","darkgreen","cyan","purple","magenta"]

    ## SPEI
    cf1 = ax.contourf(data['lon'], data['lat'], data, 
                             levs,colors=cols, extend='both', transform=ccrs.PlateCarree())

    ax.set_title(str(month)+"-month SPI based on PRISM data, end of "+data.time.dt.strftime('%B %Y').values, fontsize=13)

    cb1 = fig.colorbar(cf1, ax=ax, orientation='horizontal', aspect=30, shrink=0.65, pad=0.01)
    cb1.set_label('SPI', size='large')
    
    # Add a text annotation 
    text = AnchoredText("data source: PRISM Climate Group, Oregon State University\nPearson distribution trained on 1901-2020",
                        loc='lower left', prop={'size': 8}, frameon=True)
    ax.add_artist(text)

    #plt.show()

    plt.savefig("spi_"+str(month)+"month_"+data.time.dt.strftime('%Y%m').values+"_CO.png", bbox_inches='tight', dpi=200, transparent=False, facecolor='white')
    plt.close('all')




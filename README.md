# PRISM-SPI-SPEI
code to calculate standardized precipitation index (SPI) and standardized precipitation-evapotranspiration index (SPEI) from PRISM monthly temperature and precipitation data

At the Colorado Climate Center, we calculate [SPI and SPEI each month over Colorado using gridded climate data](https://climate.colostate.edu/spi_monthly_maps.html), specifically from the [PRISM climate group](https://prism.oregonstate.edu) and [NOAA's nClimGrid dataset](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00332)

This repository includes the general workflow, which includes shell scripts to download and process the data, and then python code to calculate SPI/SPEI and make maps. We rely on the [climate-indices](https://github.com/monocongo/climate_indices) python package to make the calculations. 

The workflow is:
- Download and process PRISM data, using download_prism_monthly_prov_noregrid.bash and download_prism_tavg_monthly_prov_noregrid.bash scripts. Requires gdal (specifically gdal_translate, which converts the native GIS file format into netcdf)
- Aggregate and subset the PRISM data, using the aggregate_subset_* python scripts. The provided code subsets to Colorado, but it would be easy to adjust to a different region of interest.
- Run `process_climate_indices` to calculate SPI, PET, and SPEI, following [the instructions](https://climate-indices.readthedocs.io/en/latest/) for that package. For example, to calculate SPI, we use `process_climate_indices --index spi --periodicity monthly --netcdf_precip PRISM_prcp_monthly_CO_all.nc --var_name_precip prcp --output_file_base PRISM_CO --scales 1 2 3 4 5 6 9 12 24 48 60 --calibration_start_year 1901 --calibration_end_year 2020 --multiprocessing all_but_one`
- Make the maps, using prism_drought_maps.py. This requires xarray and standard python plotting packages (matplotlib, cartopy, metpy)
- An example output map looks like this:


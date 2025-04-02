#!/bin/bash

## download PRISM daily data

export year=2025

   for month in 01 02 03 04 05 06 07 08 09 10 11 12 ; do

     echo "working on "${year}${month}

     ### remove existing file for this month
     rm /data/rschumac/prism/monthly/PRISM_ppt_*_${year}${month}*.nc
 
      wget --no-check-certificate ftp://prism.nacse.org/monthly/ppt/${year}/PRISM_ppt_stable_4kmM3_${year}${month}_bil.zip

      unzip PRISM_ppt_stable_4kmM3_${year}${month}_bil.zip

      ## convert to netcdf

      if [ -f "PRISM_ppt_stable_4kmM3_${year}${month}_bil.bil" ] ; then

         gdal_translate -of netCDF PRISM_ppt_stable_4kmM3_${year}${month}_bil.bil PRISM_ppt_stable_4kmM3_${year}${month}_bil.nc
      ## apply the same grid from a file for consistency with xarray (see https://sourceforge.net/p/nco/discussion/9830/thread/a57c18c50a/?limit=25)
         if [ -f "PRISM_ppt_stable_4kmM3_${year}${month}_bil.nc" ] ; then
            ncks -A -v lat,lon grid_spec_file.nc PRISM_ppt_stable_4kmM3_${year}${month}_bil.nc
         fi

         #mv PRISM_ppt_stable_4kmM3_${year}${month}_bil.nc /schumacher-scratch/shared/precip_data/prism/monthly/.
         mv PRISM_ppt_stable_4kmM3_${year}${month}_bil.nc /data/rschumac/prism/monthly/.
         rm PRISM_ppt_stable_4kmM3_${year}${month}_bil.*  ## remove original files

      else 
   
         wget --no-check-certificate ftp://prism.nacse.org/monthly/ppt/${year}/PRISM_ppt_provisional_4kmM3_${year}${month}_bil.zip
         unzip PRISM_ppt_provisional_4kmM3_${year}${month}_bil.zip
     
         gdal_translate -of netCDF PRISM_ppt_provisional_4kmM3_${year}${month}_bil.bil PRISM_ppt_provisional_4kmM3_${year}${month}_bil.nc
      ## apply the same grid from a file for consistency with xarray (see https://sourceforge.net/p/nco/discussion/9830/thread/a57c18c50a/?limit=25)
         if [ -f "PRISM_ppt_provisional_4kmM3_${year}${month}_bil.nc" ] ; then
            ncks -A -v lat,lon grid_spec_file.nc PRISM_ppt_provisional_4kmM3_${year}${month}_bil.nc
         fi

         #mv PRISM_ppt_provisional_4kmM3_${year}${month}_bil.nc /schumacher-scratch/shared/precip_data/prism/monthly/.
         mv PRISM_ppt_provisional_4kmM3_${year}${month}_bil.nc /data/rschumac/prism/monthly/.
         rm PRISM_ppt_provisional_4kmM3_${year}${month}_bil.*  ## remove original files

      fi  

     done

